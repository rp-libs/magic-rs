use std::path::Path;
use pyo3::prelude::*;
use infer::{get, Type, MatcherType, get_from_path};
use pyo3::create_exception;
use pyo3::exceptions::PyValueError;
use pyo3::types::{PyString, PyBytes};

create_exception!(_magic_rs, CantMatchTypeError, PyValueError, "Cant match type error");

#[pyclass]
struct PyMagic {
    infer_type: Type,
}

impl PyMagic {
    fn new(infer_type: Type) -> Self {
        PyMagic { infer_type }
    }
}

#[pymethods]
impl PyMagic {
    pub fn mime_type(&self) -> PyResult<String> {
        Ok(self.infer_type.mime_type().parse()?)
    }
    pub fn extension(&self) -> PyResult<String> {
        Ok(self.infer_type.extension().parse()?)
    }
    pub fn is_image(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Image)
    }
    pub fn is_app(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::App)
    }
    pub fn is_archive(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Archive)
    }
    pub fn is_audio(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Audio)
    }
    pub fn is_book(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Book)
    }
    pub fn is_document(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Doc)
    }
    pub fn is_font(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Font)
    }
    pub fn is_video(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Video)
    }
    pub fn is_text(&self) -> PyResult<bool> {
        Ok(self.infer_type.matcher_type() == MatcherType::Text)
    }
}


#[pyfunction]
#[pyo3(signature = (buf))]
fn from_bytes(_py: Python, buf: &PyBytes) -> PyResult<PyMagic> {
    let buf = buf.as_bytes();
    match _py.allow_threads(|| get(buf)) {
        None => Err(CantMatchTypeError::new_err("Cant match type error")),
        Some(resp) => Ok(PyMagic::new(resp)),
    }
}

#[pyfunction]
#[pyo3(signature = (path))]
fn from_path(_py: Python, path: &PyString) -> PyResult<Option<PyMagic>> {
    let path_str = path.to_str().unwrap();
    let path = Path::new(path_str);
    match _py.allow_threads(|| get_from_path(path)) {
        Ok(None) => Err(CantMatchTypeError::new_err("Cant match type or path error")),
        Ok(Some(resp)) => Ok(Option::from(PyMagic::new(resp))),
        _ => Err(CantMatchTypeError::new_err("Cant match type or path error")),
    }
}

#[pymodule]
fn _magic_rs(_py: Python, module: &PyModule) -> PyResult<()> {
    module.add_class::<PyMagic>()?;
    module.add_function(wrap_pyfunction!(from_bytes, module)?)?;
    module.add_function(wrap_pyfunction!(from_path, module)?)?;
    module.add("CantMatchTypeError", _py.get_type::<CantMatchTypeError>())?;

    #[cfg(not(PyPy))]
    pyo3::prepare_freethreaded_python();

    Ok(())
}
