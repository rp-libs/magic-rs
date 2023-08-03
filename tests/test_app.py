import pytest
from magic_rs import from_path, from_bytes


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        ("sample.exe", "application/vnd.microsoft.portable-executable", "exe"),
        ("sample_mach_x86", "application/x-mach-binary", "mach"),
        ("sample_mach_x64", "application/x-mach-binary", "mach"),
        ("sample_mach_ppc", "application/x-mach-binary", "mach"),
        ("sample_mach_fat", "application/x-mach-binary", "mach"),
        ("sample.class", "application/java", "class"),
        ("sample.wasm", "application/wasm", "wasm"),
        ("sample.der", "application/x-x509-ca-cert", "der"),
        ("sample.pem", "application/x-x509-ca-cert", "pem"),
    ],
)
def test_is_app_from_bytes(file_name, mime_type, extension):
    with open(f"testdata/{file_name}", "rb") as f:
        py_magic = from_bytes(f.read())
        assert py_magic.mime_type() == mime_type
        assert py_magic.extension() == extension
        assert py_magic.is_app()
        assert py_magic.is_book() is False
        assert py_magic.is_text() is False
        assert py_magic.is_font() is False
        assert py_magic.is_audio() is False
        assert py_magic.is_document() is False
        assert py_magic.is_video() is False
        assert py_magic.is_archive() is False
        assert py_magic.is_image() is False


@pytest.mark.parametrize(
    ("file_name", "mime_type", "extension"),
    [
        ("sample.exe", "application/vnd.microsoft.portable-executable", "exe"),
        ("sample_mach_x86", "application/x-mach-binary", "mach"),
        ("sample_mach_x64", "application/x-mach-binary", "mach"),
        ("sample_mach_ppc", "application/x-mach-binary", "mach"),
        ("sample_mach_fat", "application/x-mach-binary", "mach"),
        ("sample.class", "application/java", "class"),
        ("sample.wasm", "application/wasm", "wasm"),
        ("sample.der", "application/x-x509-ca-cert", "der"),
        ("sample.pem", "application/x-x509-ca-cert", "pem"),
    ],
)
def test_is_app_from_path(file_name, mime_type, extension):
    py_magic = from_path(f"testdata/{file_name}")
    assert py_magic.mime_type() == mime_type
    assert py_magic.extension() == extension
    assert py_magic.is_app()
    assert py_magic.is_text() is False
    assert py_magic.is_book() is False
    assert py_magic.is_font() is False
    assert py_magic.is_audio() is False
    assert py_magic.is_document() is False
    assert py_magic.is_video() is False
    assert py_magic.is_archive() is False
    assert py_magic.is_image() is False
