import pytest
from magic_rs import from_path, from_bytes


@pytest.mark.parametrize(
    ("mime_type", "extension", "file_name"),
    [
        ("image/jpeg", "jpg", "sample.jpg"),
        ("image/png", "png", "sample.png"),
        ("image/gif", "gif", "sample.gif"),
        ("image/tiff", "tif", "sample.tif"),
        ("image/tiff", "tif", "sample2.tif"),
        ("image/tiff", "tif", "sample3.tif"),
        ("image/tiff", "tif", "sample4.tif"),
        ("image/tiff", "tif", "sample5.tif"),
        ("image/bmp", "bmp", "sample.bmp"),
        ("image/vnd.adobe.photoshop", "psd", "sample.psd"),
        ("image/vnd.microsoft.icon", "ico", "sample.ico"),
        ("image/heif", "heif", "sample.heic"),
        ("image/avif", "avif", "sample.avif"),
        ("image/jxl", "jxl", "spline_on_first_frame.jxl"),
        ("image/openraster", "ora", "sample.ora"),
    ],
)
def test_is_image_from_bytes(mime_type, extension, file_name):
    with open(f"testdata/{file_name}", "rb") as f:
        py_magic = from_bytes(f.read())
        assert py_magic.mime_type() == mime_type
        assert py_magic.extension() == extension
        assert py_magic.is_app() is False
        assert py_magic.is_book() is False
        assert py_magic.is_font() is False
        assert py_magic.is_audio() is False
        assert py_magic.is_document() is False
        assert py_magic.is_video() is False
        assert py_magic.is_archive() is False
        assert py_magic.is_text() is False
        assert py_magic.is_image()


@pytest.mark.parametrize(
    ("mime_type", "extension", "file_name"),
    [
        ("image/jpeg", "jpg", "sample.jpg"),
        ("image/png", "png", "sample.png"),
        ("image/gif", "gif", "sample.gif"),
        ("image/tiff", "tif", "sample.tif"),
        ("image/tiff", "tif", "sample2.tif"),
        ("image/tiff", "tif", "sample3.tif"),
        ("image/tiff", "tif", "sample4.tif"),
        ("image/tiff", "tif", "sample5.tif"),
        ("image/bmp", "bmp", "sample.bmp"),
        ("image/vnd.adobe.photoshop", "psd", "sample.psd"),
        ("image/vnd.microsoft.icon", "ico", "sample.ico"),
        ("image/heif", "heif", "sample.heic"),
        ("image/avif", "avif", "sample.avif"),
        ("image/jxl", "jxl", "spline_on_first_frame.jxl"),
        ("image/openraster", "ora", "sample.ora"),
    ],
)
def test_is_image_from_path(file_name, mime_type, extension):
    py_magic = from_path(f"testdata/{file_name}")
    assert py_magic.mime_type() == mime_type
    assert py_magic.extension() == extension
    assert py_magic.is_app() is False
    assert py_magic.is_book() is False
    assert py_magic.is_font() is False
    assert py_magic.is_audio() is False
    assert py_magic.is_document() is False
    assert py_magic.is_video() is False
    assert py_magic.is_archive() is False
    assert py_magic.is_image()
    assert py_magic.is_text() is False
