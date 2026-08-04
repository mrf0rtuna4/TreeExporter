from pathlib import Path

from tree_exporter.scanner import build_layout
from tree_exporter.models import TreeNode

FONT_SIZE = 14
LINE_HEIGHT = 24
INDENT = 24
PADDING = 16


def generate_svg(
    tree: TreeNode,
    output: str,
) -> None:

    layout = build_layout(tree)

    width = 1000
    height = len(layout) * LINE_HEIGHT + PADDING * 2

    svg: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]

    for item in layout:

        x = PADDING + item.depth * INDENT
        y = PADDING + item.y * LINE_HEIGHT

        label = (
            f"📁 {item.node.name}"
            if item.node.is_directory
            else f"📄 {item.node.name}"
        )

        svg.append(
            f'<text x="{x}" y="{y}" '
            f'font-size="{FONT_SIZE}" '
            f'font-family="monospace">{label}</text>'
        )

    svg.append("</svg>")

    Path(output).write_text(
        "\n".join(svg),
        encoding="utf-8",
    )