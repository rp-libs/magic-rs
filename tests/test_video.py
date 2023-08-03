import pytest
from magic_rs import from_path, from_bytes


@pytest.mark.parametrize(
    ("mime_type", "extension", "file_name"),
    [
        ("video/mp4", "mp4", "sample.mp4"),
        ("video/x-matroska", "mkv", "sample.mkv"),
        ("video/webm", "webm", "sample.webm"),
        ("video/quicktime", "mov", "sample.mov"),
        ("video/quicktime", "mov", "sample2.mov"),
        ("video/x-msvideo", "avi", "sample.avi"),
        ("video/x-flv", "flv", "sample.flv"),
    ],
)
def test_is_video_from_bytes(mime_type, extension, file_name):
    with open(f"testdata/{file_name}", "rb") as f:
        py_magic = from_bytes(f.read())
        assert py_magic.mime_type() == mime_type
        assert py_magic.extension() == extension
        assert py_magic.is_app() is False
        assert py_magic.is_book() is False
        assert py_magic.is_font() is False
        assert py_magic.is_audio() is False
        assert py_magic.is_document() is False
        assert py_magic.is_video()
        assert py_magic.is_archive() is False
        assert py_magic.is_text() is False
        assert py_magic.is_image() is False


@pytest.mark.parametrize(
    ("mime_type", "extension", "file_name"),
    [
        ("video/mp4", "mp4", "sample.mp4"),
        ("video/x-matroska", "mkv", "sample.mkv"),
        ("video/webm", "webm", "sample.webm"),
        ("video/quicktime", "mov", "sample.mov"),
        ("video/quicktime", "mov", "sample2.mov"),
        ("video/x-msvideo", "avi", "sample.avi"),
        ("video/x-flv", "flv", "sample.flv"),
    ],
)
def test_is_video_from_path(file_name, mime_type, extension):
    py_magic = from_path(f"testdata/{file_name}")
    assert py_magic.mime_type() == mime_type
    assert py_magic.extension() == extension
    assert py_magic.is_app() is False
    assert py_magic.is_book() is False
    assert py_magic.is_font() is False
    assert py_magic.is_audio() is False
    assert py_magic.is_document() is False
    assert py_magic.is_video()
    assert py_magic.is_archive() is False
    assert py_magic.is_image() is False
    assert py_magic.is_text() is False
