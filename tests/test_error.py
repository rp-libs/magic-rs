import pytest
from magic_rs import from_path, from_bytes, CantMatchTypeError


def test_error_from_bytes():
    with pytest.raises(CantMatchTypeError):
        from_bytes(b"12")


def test_error_from_path():
    with pytest.raises(CantMatchTypeError):
        from_path("error path")
