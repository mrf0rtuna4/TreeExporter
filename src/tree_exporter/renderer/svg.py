from html import escape
from pathlib import Path

from tree_exporter.models import TreeNode
from tree_exporter.renderer.themes import ThemeName, get_theme
from tree_exporter.scanner import build_layout

FONT_SIZE = 14
LINE_HEIGHT = 24
INDENT = 24
PADDING = 16

def generate_svg(
    tree: TreeNode,
    output: str,
    theme: ThemeName = "light",
    directory_icon: str = "📁",
    file_icon: str = "📄",
) -> None:
    layout = build_layout(tree)
    colors = get_theme(theme)

    width = 1000
    height = len(layout) * LINE_HEIGHT + PADDING * 2

    svg: list[str] = [
        (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'),
        (f'<rect width="100%" height="100%" fill="{colors.background}"/>'),
    ]

    for item in layout:
        x = PADDING + item.depth * INDENT
        y = PADDING + item.y * LINE_HEIGHT

        icon = directory_icon if item.node.is_directory else file_icon
        label = escape(f"{icon} {item.node.name}")

        text_color = colors.directory if item.node.is_directory else colors.file

        svg.append(
            f'<text x="{x}" y="{y}" '
            f'font-size="{FONT_SIZE}" '
            f'font-family="monospace" '
            f'fill="{text_color}">{label}</text>'
        )

    svg.append("</svg>")

    Path(output).write_text(
        "\n".join(svg),
        encoding="utf-8",
    )
