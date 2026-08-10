from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ThemeName = Literal["light", "dark"]


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
}


def get_theme(name: ThemeName) -> SvgTheme:
    return THEMES[name]
