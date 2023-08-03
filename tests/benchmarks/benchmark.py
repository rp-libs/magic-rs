import pytest
import magic_rs
import magic
from pathlib import Path

current_file = Path(__file__)
parent_dir = current_file.parent.parent.parent

num = 10000


# pip install python-magic
# pip install 'pytest-benchmark[histogram]~=4.0.0' magic-rs
# pytest tests/benchmarks/benchmark.py  --benchmark-histogram


@pytest.mark.benchmark(group="from_bytes")
def test_rs_from_bytes(benchmark):
    file_to_open = parent_dir / "testdata" / "sample.jpg"

    def rs_from_bytes():
        with file_to_open.open("rb") as f:
            content = f.read()
            for _ in range(num):
                assert magic_rs.from_bytes(content).is_image()

    benchmark(rs_from_bytes)


@pytest.mark.benchmark(group="from_bytes")
def test_from_bytes(benchmark):
    file_to_open = parent_dir / "testdata" / "sample.jpg"

    def from_bytes():
        with file_to_open.open("rb") as f:
            content = f.read()
            for _ in range(num):
                assert magic.from_buffer(content, mime=True) == "image/jpeg"

    benchmark(from_bytes)


@pytest.mark.benchmark(group="from_path")
def test_rs_from_path(benchmark):
    file_to_open = parent_dir / "testdata" / "sample.jpg"

    def rs_from_bytes():
        for _ in range(num):
            assert magic_rs.from_path(file_to_open.as_posix()).is_image()

    benchmark(rs_from_bytes)


@pytest.mark.benchmark(group="from_path")
def test_from_path(benchmark):
    file_to_open = parent_dir / "testdata" / "sample.jpg"

    def from_bytes():
        for _ in range(num):
            assert magic.from_file(file_to_open, mime=True) == "image/jpeg"

    benchmark(from_bytes)
