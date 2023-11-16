# ANSI Color Codes
ANSI_RESET = "\033[0m"
GREEN = "\033[92m"
BLUE = "\033[34m"
GREY = "\033[2m"
YELLOW = "\033[93m"  # Example: used for warnings
MAGENTA = "\033[35m"  # Example: used for loaders

# ANSI Cursor and Screen Control
ANSI_HIDE_CURSOR = "\033[?25l"
ANSI_CLEAR_SCREEN = "\033c"

# Unicode Characters for Icons
CIRCLE_FILLED = f"{GREEN}●{ANSI_RESET}"
CIRCLE_EMPTY = "○"
TRIANGLE_RIGHT = f"{BLUE}◇{ANSI_RESET}"
LINE = f"{BLUE}│{ANSI_RESET}"
LINE_G = f"{GREY}│{ANSI_RESET}"
LINE_O = f"{BLUE}│{ANSI_RESET}"  # Blue line, but could be a different color if needed
SP_SET = ["│", "└", "▴", "◆", "╷", "⌜"]
TO_RIGHT = f"{BLUE}└{ANSI_RESET}"
ACTIVE_ICON = f"{BLUE}◆{ANSI_RESET}"
LINE_UNDER = f"{BLUE}╷{ANSI_RESET}"
LINE_ABOVE = f"{BLUE}╵{ANSI_RESET}"
LINE_ABOVE_G = f"{GREY}╵{ANSI_RESET}"
TO_LEFT = f"{BLUE}⌜{ANSI_RESET}"
BLUE_BACKGROUND = "\033[44m"

# Box Icons
BOX_FULL = f"{BLUE}◼{ANSI_RESET}"
BOX_EMPTY_G = f"{GREY}□{ANSI_RESET}"
BOX_EMPTY = f"{BLUE}□{ANSI_RESET}"

# Loading Symbols
LOADING_SYMBOLS = ["◐", "◓", "◑", "◒"]
LOADING_COLOR = "\033[35m"
