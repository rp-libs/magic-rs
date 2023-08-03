import pytest
from magic_rs import from_path, from_bytes


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        ("sample.doc", "application/msword", "doc"),
        (
            "sample.docx",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "docx",
        ),
        ("sample.xls", "application/vnd.ms-excel", "xls"),
        (
            "sample.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "xlsx",
        ),
        ("sample.ppt", "application/vnd.ms-powerpoint", "ppt"),
        (
            "sample.pptx",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "pptx",
        ),
    ],
)
def test_is_doc_from_bytes(file_name, mime_type, extension):
    with open(f"testdata/{file_name}", "rb") as f:
        py_magic = from_bytes(f.read())
        assert py_magic.mime_type() == mime_type
        assert py_magic.extension() == extension
        assert py_magic.is_app() is False
        assert py_magic.is_book() is False
        assert py_magic.is_font() is False
        assert py_magic.is_audio() is False
        assert py_magic.is_document()
        assert py_magic.is_video() is False
        assert py_magic.is_archive() is False
        assert py_magic.is_image() is False
        assert py_magic.is_text() is False


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        (
            "sample.docx",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "docx",
        ),
        (
            "sample.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "xlsx",
        ),
        (
            "sample.pptx",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "pptx",
        ),
    ],
)
def test_is_doc_from_path(file_name, mime_type, extension):
    py_magic = from_path(f"testdata/{file_name}")
    assert py_magic.mime_type() == mime_type
    assert py_magic.extension() == extension
    assert py_magic.is_app() is False
    assert py_magic.is_book() is False
    assert py_magic.is_font() is False
    assert py_magic.is_audio() is False
    assert py_magic.is_document()
    assert py_magic.is_video() is False
    assert py_magic.is_archive() is False
    assert py_magic.is_image() is False
    assert py_magic.is_text() is False
