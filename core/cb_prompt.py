import time
from typing import Literal

from getkey import getkey, keys

from core.symbols import SYMBOLS, SP_SET, LOADING_SYMBOLS
from core.colors import COLORS


class InteractivePrompt:
    def __init__(self):
        self.add_list = []

    @staticmethod
    def print_with_colors(text, color):
        print(f"{color}{text}{COLORS.RESET}", end="")

    @staticmethod
    def clear_screen():
        print(SYMBOLS.ANSI_CLEAR_SCREEN, end="")

    def loader(
        self,
        name,
        duration_secs,
        done_text,
        # TODO: May extend to pass symbols
        style: dict[Literal["LOADING_COLOR"], str] | None = None,
        ontop="",
    ):
        LOADING_COLOR = style.get("LOADING_COLOR", COLORS.LOADING)
        for i in range(duration_secs):
            symbol = LOADING_SYMBOLS[i % len(LOADING_SYMBOLS)]
            print(
                f"{ontop}{LOADING_COLOR}{symbol}" f"{COLORS.RESET} {name}{COLORS.RESET}"
            )
            time.sleep(0.065)
            self.clear_screen()

        return (
            f"{SYMBOLS.TRIANGLE_RIGHT} {done_text}"
            f"{COLORS.RESET}\n{SYMBOLS.LINE_G}"
            f"{COLORS.RESET}"
        )

    def type_in(self, name, pre_text, error_msg, validate_func, ontop=""):
        typed_text = []
        error = COLORS.BLUE
        icon_index = 3  # Default icon index

        while True:
            display_text = (
                COLORS.GREY.value + pre_text if not typed_text else "".join(typed_text)
            )
            print(
                f"{ontop}{error}{SP_SET[icon_index]}{COLORS.RESET} "
                f"{name}\n{error}{SP_SET[4]}{COLORS.RESET}  "
                f"{display_text}{COLORS.RESET}\n{error}"
                f"{SP_SET[1]} {error_msg}"
            )

            key = getkey()

            if key in keys.ENTER:
                if validate_func("".join(typed_text)):
                    break
                else:
                    error = COLORS.YELLOW
                    typed_text = []
                    icon_index = 2
                    error_msg = f"{COLORS.YELLOW}{error_msg}{COLORS.RESET}"
            elif key in [keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT]:
                # Ignore these keys
                pass
            elif key in keys.BACKSPACE:
                if typed_text:
                    typed_text.pop()
            else:
                typed_text.append(key)

            self.clear_screen()

        result_text = (
            f"{SYMBOLS.TRIANGLE_RIGHT} {name}{COLORS.RESET}"
            f"\n{SYMBOLS.LINE_G} {COLORS.GREY}{''.join(typed_text)}"
            f"\n{SYMBOLS.LINE_G}{COLORS.RESET}"
        )
        return "".join(typed_text), result_text

    def group_selection(
        self, title: str, options: list, descriptions: list, ontop: str = ""
    ):
        """
        Allows the user to select an option from a list using UP/DOWN and ENTER keys.

        Parameters
        ----------
        title
            The title for the selection
        options
            A list of options available for selection
        descriptions
            A list of descriptions for each option, if any
        ontop
            ???

        Returns
        -------
            Selected index and the resulting display string.
        """
        current_selection = 0

        while True:
            print(f"{ontop}{SYMBOLS.ACTIVE_ICON} {title}\n{SYMBOLS.LINE_UNDER}")

            for index, option in enumerate(options):
                selection_indicator = (
                    SYMBOLS.CIRCLE_FILLED
                    if index == current_selection
                    else SYMBOLS.CIRCLE_EMPTY
                )

                # Print the description only for the currently selected option
                if index == current_selection and descriptions:
                    print(
                        f"{SYMBOLS.LINE}  {selection_indicator}    {option}"
                        f"{COLORS.GREY}    {descriptions[index]}{COLORS.RESET}"
                    )

                else:
                    print(f"{SYMBOLS.LINE}  {selection_indicator}    {option}")

            print(SYMBOLS.TO_RIGHT)
            key = getkey()

            if key in keys.UP and current_selection > 0:
                current_selection -= 1
            elif key in keys.DOWN and current_selection < len(options) - 1:
                current_selection += 1
            elif key in keys.ENTER:
                break

            self.clear_screen()

        display_text = (
            f"{SYMBOLS.TRIANGLE_RIGHT} {title}{COLORS.RESET}"
            f"\n{SYMBOLS.LINE_G} {COLORS.GREY} "
            f"{options[current_selection]}{COLORS.RESET}"
            f"\n{SYMBOLS.LINE_G}"
        )
        return current_selection, display_text

    def multiple_selection(self, title, options, descriptions, ontop=""):
        current_selection = 0
        # Tracks which options are selected
        selected_options = [False] * len(options)

        while True:
            print(f"{ontop}{SYMBOLS.ACTIVE_ICON} {title}\n{SYMBOLS.LINE_UNDER}")

            for index, option in enumerate(options):
                box_icon = (
                    SYMBOLS.BOX_FULL if selected_options[index] else SYMBOLS.BOX_EMPTY_G
                )
                description = (
                    f" {COLORS.GREY}{descriptions[index]}{COLORS.RESET}"
                    if descriptions
                    else ""
                )
                highlight = COLORS.GREEN if index == current_selection else ""
                print(
                    f"{SYMBOLS.LINE}  {highlight}{box_icon}{COLORS.RESET}    "
                    f"{option}{description}"
                )

            print(SYMBOLS.TO_RIGHT)
            key = getkey()

            if key in keys.UP and current_selection > 0:
                current_selection -= 1
            elif key in keys.DOWN and current_selection < len(options) - 1:
                current_selection += 1
            elif key == "a":  # Toggle selection
                selected_options[current_selection] = not selected_options[
                    current_selection
                ]
            elif key in keys.ENTER:
                break

            self.clear_screen()

        selected_items = [
            options[i] for i, selected in enumerate(selected_options) if selected
        ]
        display_text = (
            f"{SYMBOLS.TRIANGLE_RIGHT} {title}\n{SYMBOLS.LINE_G} "
            f"{COLORS.GREY} {', '.join(selected_items)}{COLORS.RESET}"
            f"\n{SYMBOLS.LINE_G}"
        )
        return selected_items, display_text

    def horizontal_selection(self, title, options, descriptions, ontop=""):
        current_selection = 0

        while True:
            print(f"{ontop}{SYMBOLS.ACTIVE_ICON} {title}\n{SYMBOLS.LINE_UNDER}")
            print(SYMBOLS.LINE, end="")

            for index, option in enumerate(options):
                selection_indicator = (
                    SYMBOLS.CIRCLE_FILLED
                    if index == current_selection
                    else SYMBOLS.CIRCLE_EMPTY
                )
                description = f" {descriptions[index]}" if descriptions else ""
                print(f"  {selection_indicator} {option}{description}", end="")

            print(f"\n{SYMBOLS.TO_RIGHT}")
            key = getkey()

            if key in keys.LEFT and current_selection > 0:
                current_selection -= 1
            elif key in keys.RIGHT and current_selection < len(options) - 1:
                current_selection += 1
            elif key in keys.ENTER:
                break

            self.clear_screen()

        display_text = (
            f"{SYMBOLS.TRIANGLE_RIGHT} {title}\n{SYMBOLS.LINE_G} "
            f"{COLORS.GREY} {options[current_selection]}{COLORS.RESET}"
            f"\n{SYMBOLS.LINE_G}"
        )
        return current_selection, display_text

    def start(self, title):
        """
        Displays the start of a prompt sequence.

        Args:
            title (str): The title of the sequence.

        Returns:
            str: Formatted start string.
        """
        # start_text = (
        #     f"{COLORS.GREY}↱{COLORS.RESET} {COLORS.BLUE_BG} "
        #     f"{title} {COLORS.RESET}\n{COLORS.GREY}{SP_SET[0]}"
        #     f"{COLORS.RESET}"
        # )
        start_text = f"{COLORS.GREY}↱{COLORS.RESET} {COLORS.BLUE_BG} {title} {COLORS.RESET}\n{COLORS.GREY}{SP_SET[0]}{COLORS.RESET}"
        print(start_text)
        return start_text

    def end(self, title, final_text):
        """
        Displays the end of a prompt sequence along with final text.

        Args:
            title (str): The title of the sequence.
            final_text (str): The final text to display.

        Returns:
            None
        """
        print(
            f"{final_text}{COLORS.GREY}↳{COLORS.RESET} {COLORS.BLUE_BG} {title} "
            f"{COLORS.RESET}"
        )
        # Additional text (can be customized or removed)
        extra_text = (
            f"{COLORS.GREY}{SP_SET[0]}"
            f"\n{COLORS.GREY}{SP_SET[0]}{COLORS.RESET}"
            f"Cool right?\n {COLORS.GREY}{SP_SET[0]}{COLORS.RESET} Right\n "
            f"{COLORS.GREY}{SP_SET[0]}{COLORS.RESET}"
            # " "
            # + COLORS.GREY
            # + SYMBOLS.SP_SET[0]
            # + "\n "
            # + COLORS.GREY
            # + SYMBOLS.SP_SET[0]
            # + COLORS.RESET
            # + "Cool right?\n "
            # + COLORS.GREY
            # + SYMBOLS.SP_SET[0]
            # + COLORS.RESET
            # + "Right\n "
            # + COLORS.GREY + SYMBOLS.SP_SET[0] + COLORS.RESET
        )
        print(extra_text)

    def begin(self, name):
        self.clear_screen()
        returned_text = self.start(name)
        self.add_list.append(returned_text + "\n")
        self.clear_screen()
        return self.add_list

    def choice(self, name, content, additions):
        selected_index, return_text = self.group_selection(
            name, content, additions, "".join(self.add_list)
        )
        self.add_list.append(return_text + "\n")
        self.clear_screen()
        return selected_index, self.add_list

    def loading(self, name, times, end_with):
        return_text = self.loader(name, times, end_with, ontop="".join(self.add_list))
        self.add_list.append(return_text + "\n")
        self.clear_screen()
        return self.add_list

    def type_f(self, name, pre_show, error):
        def is_valid_input(input_text):
            # Replace this with your validation logic
            return input_text == "Toad"

        typed_text, return_text = self.type_in(
            name, pre_show, error, is_valid_input, "".join(self.add_list)
        )
        self.add_list.append(return_text + "\n")
        self.clear_screen()
        return typed_text, self.add_list

    def multi_select(self, name, content, additions):
        selections, return_text = self.multiple_selection(
            name, content, additions, "".join(self.add_list)
        )
        self.add_list.append(return_text + "\n")
        self.clear_screen()
        return selections, self.add_list

    def choice_horizontal(self, name, content, additions):
        selected_index, return_text = self.horizontal_selection(
            name, content, additions, "".join(self.add_list)
        )
        self.add_list.append(return_text + "\n")
        self.clear_screen()
        return selected_index, self.add_list

    def run(self):
        self.clear_screen()


if __name__ == "__main__":

    class FixtureCLI(InteractivePrompt):
        def create(self):
            self.clear_screen()
            # Starting the interactive session
            self.begin("Interactive Test Session")

            # Simple choice selection
            self.choice(
                "Select an option",
                ["Option 1", "Option 2", "Option 3"],
                [" cool option", " not so cool", "maybe"],
            )

            # Simulating a loading process
            self.loading("Loading...", 24, "Loading Complete!")

            # Text input
            self.type_f("Your name", "Enter your name", "Please type a name")

            # Multi-selection
            self.multi_select(
                "Choose multiple",
                ["Choice A", "Choice B", "Choice C"],
                ["", "", ""],
            )

            # Horizontal choice selection
            self.choice_horizontal(
                "Select horizontally",
                ["Left", "Center", "Right"],
                ["", "", ""],
            )

            print("All interaction history:\n", "".join(self.add_list))

            # End of the script
            print("End of the interactive test session.")
