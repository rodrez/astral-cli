import enum
from typing import Literal

from core.colors import COLORS


class SYMBOLS(enum.Enum):
    # ANSI Cursor and Screen Control
    ANSI_HIDE_CURSOR = "\033[?25l"
    ANSI_CLEAR_SCREEN = "\033c"

    # Unicode Characters for Symbols
    CIRCLE_FILLED = f"{COLORS.GREEN}●{COLORS.RESET}"
    CIRCLE_EMPTY = "○"
    TRIANGLE_RIGHT = f"{COLORS.BLUE}◇{COLORS.RESET}"
    LINE = f"{COLORS.BLUE}│{COLORS.RESET}"
    LINE_G = f"{COLORS.GREY}│{COLORS.RESET}"

    # Blue line, but could be a different color if needed
    LINE_O = f"{COLORS.BLUE}│{COLORS.RESET}"

    TO_RIGHT = f"{COLORS.BLUE}└{COLORS.RESET}"
    ACTIVE_ICON = f"{COLORS.BLUE}◆{COLORS.RESET}"
    LINE_UNDER = f"{COLORS.BLUE}╷{COLORS.RESET}"
    LINE_ABOVE = f"{COLORS.BLUE}╵{COLORS.RESET}"
    LINE_ABOVE_G = f"{COLORS.GREY}╵{COLORS.RESET}"
    TO_LEFT = f"{COLORS.BLUE}⌜{COLORS.RESET}"

    # Box Icons
    BOX_FULL = f"{COLORS.BLUE}◼{COLORS.RESET}"
    BOX_EMPTY_G = f"{COLORS.GREY}□{COLORS.RESET}"
    BOX_EMPTY = f"{COLORS.BLUE}□{COLORS.RESET}"

    # Loading Symbols
    LOADING_SYMBOLS = ["◐", "◓", "◑", "◒"]
    LOADING_COLOR = "\033[35m"


SP_SET: list[Literal["│", "└", "▴", "◆", "╷", "⌜"]] = ["│", "└", "▴", "◆", "╷", "⌜"]
LOADING_SYMBOLS = ["◐", "◓", "◑", "◒"]
