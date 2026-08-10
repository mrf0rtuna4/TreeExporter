from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


ThemeName = Literal[
    "light",
    "dark",
    "github-light",
    "github-dark",
    "dracula",
    "monokai",
    "nord",
    "solarized-light",
    "solarized-dark",
    "one-dark",
]


@dataclass(frozen=True)
class SvgTheme:
    background: str
    text: str
    directory: str
    file: str


THEMES: dict[ThemeName, SvgTheme] = {
    "light": SvgTheme(
        background="#ffffff",
        text="#24292f",
        directory="#0969da",
        file="#24292f",
    ),
    "dark": SvgTheme(
        background="#0d1117",
        text="#e6edf3",
        directory="#58a6ff",
        file="#e6edf3",
    ),
    "github-light": SvgTheme(
        background="#ffffff",
        text="#1f2328",
        directory="#0969da",
        file="#1f2328",
    ),
    "github-dark": SvgTheme(
        background="#0d1117",
        text="#e6edf3",
        directory="#79c0ff",
        file="#e6edf3",
    ),
    "dracula": SvgTheme(
        background="#282a36",
        text="#f8f8f2",
        directory="#8be9fd",
        file="#f8f8f2",
    ),
    "monokai": SvgTheme(
        background="#272822",
        text="#f8f8f2",
        directory="#a6e22e",
        file="#f8f8f2",
    ),
    "nord": SvgTheme(
        background="#2e3440",
        text="#eceff4",
        directory="#88c0d0",
        file="#eceff4",
    ),
    "solarized-light": SvgTheme(
        background="#fdf6e3",
        text="#657b83",
        directory="#268bd2",
        file="#586e75",
    ),
    "solarized-dark": SvgTheme(
        background="#002b36",
        text="#839496",
        directory="#268bd2",
        file="#93a1a1",
    ),
    "one-dark": SvgTheme(
        background="#282c34",
        text="#abb2bf",
        directory="#61afef",
        file="#abb2bf",
    ),
}


def get_theme(name: ThemeName) -> SvgTheme:
    return THEMES[name]