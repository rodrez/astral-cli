import time


class InteractivePrompt:
    # ANSI Color Codes
    ANSI_RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[34m"
    GREY = "\033[2m"
    # Used for warnings
    YELLOW = "\033[93m"
    # Used for loaders
    MAGENTA = "\033[35m"

    # ANSI Cursor and Screen Control
    ANSI_HIDE_CURSOR = "\033[?25l"
    ANSI_CLEAR_SCREEN = "\033c"

    # Unicode Characters for Icons
    CIRCLE_FILLED = f"{GREEN}●{ANSI_RESET}"
    CIRCLE_EMPTY = "○"
    TRIANGLE_RIGHT = f"{BLUE}◇{ANSI_RESET}"
    LINE = f"{BLUE}│{ANSI_RESET}"
    LINE_G = f"{GREY}│{ANSI_RESET}"
    # Blue line, but could be a different color if needed
    LINE_O = f"{BLUE}│{ANSI_RESET}"
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

    def __init__(self):
        self.add_list = []

    @staticmethod
    def print_with_colors(text, color):
        print(f"{color}{text}{InteractivePrompt.ANSI_RESET}", end="")

    @staticmethod
    def clear_screen():
        print(InteractivePrompt.ANSI_CLEAR_SCREEN, end="")

    def loader(self, name, duration_secs, done_text, ontop=""):
        for i in range(duration_secs):
            symbol = InteractivePrompt.LOADING_SYMBOLS[
                i % len(InteractivePrompt.LOADING_SYMBOLS)
            ]
            print(
                f"{ontop}{InteractivePrompt.LOADING_COLOR}{symbol}"
                f"{InteractivePrompt.ANSI_RESET} {name}{InteractivePrompt.ANSI_RESET}"
            )
            time.sleep(0.065)
            self.clear_screen()

        return (
            f"{InteractivePrompt.TRIANGLE_RIGHT} {done_text}"
            f"{InteractivePrompt.ANSI_RESET}\n{InteractivePrompt.LINE_G}"
            f"{InteractivePrompt.ANSI_RESET}"
        )

    def run(self):
        self.clear_screen()
