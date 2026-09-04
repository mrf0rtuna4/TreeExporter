from pathlib import Path

from tree_exporter.config import ScanConfig
from tree_exporter.scanner import build_layout, scan_repository


def test_scan_builds_sorted_tree_and_excludes_directories(tmp_path: Path) -> None:
    (tmp_path / "z-file.txt").write_text("z")
    (tmp_path / "a-file.txt").write_text("a")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text("")

    result = scan_repository(str(tmp_path), ScanConfig())

    assert result.is_directory
    assert [child.name for child in result.children] == [
        "src",
        "a-file.txt",
        "z-file.txt",
    ]
    assert [item.node.name for item in build_layout(result)] == [
        tmp_path.name,
        "src",
        "main.py",
        "a-file.txt",
        "z-file.txt",
    ]


def test_scan_can_include_a_default_excluded_directory(tmp_path: Path) -> None:
    (tmp_path / "build").mkdir()
    (tmp_path / "build" / "artifact.txt").write_text("")

    result = scan_repository(str(tmp_path), ScanConfig(exclude=set()))

    assert result.children[0].name == "build"
    assert result.children[0].children[0].name == "artifact.txt"
