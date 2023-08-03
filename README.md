# magic-rs

[![Package version](https://img.shields.io/pypi/v/magic-rs?color=%2334D058&label=pypi%20package)](https://pypi.org/project/magic-rs/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/magic-rs.svg?color=%2334D058)](https://pypi.org/project/magic-rs/)

Use rust [infer](https://github.com/bojand/infer) crate to rewrite python-magic library

---

## Installation

```bash
pip install magic-rs
```

---

## Quickstart

```python
from magic_rs import from_path, from_bytes

with open("testdata/sample.png", 'rb') as f:
    data = f.read()
    py_magic = from_bytes(data)
    print(py_magic.extension())
    print(py_magic.mime_type())
    print(py_magic.is_image())
    print(py_magic.is_app())
    print(py_magic.is_archive())
    print(py_magic.is_audio())
    print(py_magic.is_book())
    print(py_magic.is_document())
    print(py_magic.is_font())
    print(py_magic.is_video())
    print(py_magic.is_text())

py_magic = from_path("testdata/sample.png")
print(py_magic.extension())
print(py_magic.mime_type())
print(py_magic.is_image())
```

---

## Benchmarks
For details, see [benchmark](https://github.com/rp-libs/magic-rs/blob/main/tests/benchmarks/README.md).
