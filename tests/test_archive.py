import pytest
from magic_rs import from_path, from_bytes


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        ("sample.db", "application/vnd.sqlite3", "sqlite"),
        ("sample.tar.zst", "application/zstd", "zst"),
        ("sample.cpio", "application/x-cpio", "cpio"),
        ("sample.skippable.zst", "application/zstd", "zst"),
    ],
)
def test_is_archive_from_bytes(file_name, mime_type, extension):
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
        assert py_magic.is_archive()
        assert py_magic.is_image() is False
        assert py_magic.is_text() is False


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        ("sample.db", "application/vnd.sqlite3", "sqlite"),
        ("sample.tar.zst", "application/zstd", "zst"),
        ("sample.cpio", "application/x-cpio", "cpio"),
        ("sample.skippable.zst", "application/zstd", "zst"),
    ],
)
def test_is_archive_from_path(file_name, mime_type, extension):
    py_magic = from_path(f"testdata/{file_name}")
    assert py_magic.mime_type() == mime_type
    assert py_magic.extension() == extension
    assert py_magic.is_app() is False
    assert py_magic.is_book() is False
    assert py_magic.is_font() is False
    assert py_magic.is_audio() is False
    assert py_magic.is_document() is False
    assert py_magic.is_video() is False
    assert py_magic.is_archive()
    assert py_magic.is_image() is False
    assert py_magic.is_text() is False
