import json
from pathlib import Path

from tree_exporter.models import TreeNode
from tree_exporter.renderer import generate_json, generate_svg, generate_txt


def make_tree(tmp_path: Path) -> TreeNode:
    root = TreeNode("project", tmp_path, True)
    root.add_child(TreeNode("z.txt", tmp_path / "z.txt", False))
    directory = TreeNode("src", tmp_path / "src", True)
    directory.add_child(TreeNode("<main>.py", tmp_path / "src" / "main.py", False))
    root.add_child(directory)
    return root


def test_json_export_is_sorted_and_serializable(tmp_path: Path) -> None:
    output = tmp_path / "tree.json"

    generate_json(make_tree(tmp_path), str(output))

    assert json.loads(output.read_text()) == {
        "name": "project",
        "type": "directory",
        "children": [
            {
                "name": "src",
                "type": "directory",
                "children": [{"name": "<main>.py", "type": "file", "children": []}],
            },
            {"name": "z.txt", "type": "file", "children": []},
        ],
    }


def test_svg_export_uses_custom_icons_and_escapes_labels(tmp_path: Path) -> None:
    output = tmp_path / "tree.svg"

    generate_svg(
        make_tree(tmp_path), str(output), directory_icon="DIR", file_icon="FILE"
    )

    content = output.read_text()
    assert "DIR project" in content
    assert "FILE &lt;main&gt;.py" in content


def test_text_export_renders_tree_branches(tmp_path: Path) -> None:
    output = tmp_path / "tree.txt"

    generate_txt(make_tree(tmp_path), str(output))

    assert output.read_text().splitlines() == [
        "project",
        "+-- src",
        "|   \\-- <main>.py",
        "\\-- z.txt",
    ]
