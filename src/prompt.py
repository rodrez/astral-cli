import time
from getkey import keys, getkey
import constants


def print_with_colors(text, color):
    print(f"{color}{text}{constants.ANSI_RESET}", end="")


def clear_screen():
    print(constants.ANSI_CLEAR_SCREEN, end="")


def loader(name, duration_secs, done_text, ontop=""):
    """
    Displays a loading animation for a specified duration.

    Args:
        name (str): Text to display alongside the loader.
        duration_secs (int): Duration in seconds for the loader to run.
        done_text (str): Text to display once loading is done.
        ontop (str): Additional text to display above the loader.

    Returns:
        str: The text that will be printed in the next section.
    """
    for i in range(duration_secs):
        symbol = constants.LOADING_SYMBOLS[i % len(constants.LOADING_SYMBOLS)]
        print(
            f"{ontop}{constants.LOADING_COLOR}{symbol}{constants.ANSI_RESET} {name}{constants.ANSI_RESET}"
        )
        time.sleep(0.065)
        clear_screen()

    return f"{constants.TRIANGLE_RIGHT} {done_text}{constants.ANSI_RESET}\n{constants.LINE_G}{constants.ANSI_RESET}"


def type_in(name, pre_text, error_msg, validate_func, ontop=""):
    """
    A function for typing interaction.

    Args:
        name (str): The name or title of the prompt.
        pre_text (str): The pre-filled text to display.
        error_msg (str): The error message to display if input is incorrect.
        validate_func (function): A function that takes the user input as an argument
            and returns True or False.
        ontop (str): Additional text to display above the typing area.

    Returns:
        tuple: A tuple containing the user's input and the result string.
    """
    typed_text = []
    error = constants.BLUE
    icon_index = 3  # Default icon index

    while True:
        display_text = (
            constants.GREY + pre_text if not typed_text else "".join(typed_text)
        )
        print(
            f"{ontop}{error}{constants.SP_SET[icon_index]}{constants.ANSI_RESET} {name}\n{error}{constants.SP_SET[4]}{constants.ANSI_RESET}  {display_text}{constants.ANSI_RESET}\n{error}{constants.SP_SET[1]} {error_msg}"
        )

        key = getkey()

        if key in keys.ENTER:
            if validate_func("".join(typed_text)):
                break
            else:
                error = constants.YELLOW
                typed_text = []
                icon_index = 2
                error_msg = (
                    f"{constants.YELLOW}{error_msg}{constants.ANSI_RESET}"
                )
        elif key in [keys.UP, keys.DOWN, keys.LEFT, keys.RIGHT]:
            pass  # Ignore these keys
        elif key in keys.BACKSPACE:
            if typed_text:
                typed_text.pop()
        else:
            typed_text.append(key)

        clear_screen()

    result_text = f"{constants.TRIANGLE_RIGHT} {name}{constants.ANSI_RESET}\n{constants.LINE_G} {constants.GREY}{''.join(typed_text)}\n{constants.LINE_G}{constants.ANSI_RESET}"
    return "".join(typed_text), result_text


def g_select(title, options, descriptions, ontop=""):
    """
    Allows the user to select an option from a list using UP/DOWN and ENTER keys.

    Args:
        title (str): The title of the selection prompt.
        options (list): The list of option strings.
        descriptions (list): List of description strings for each option.
        ontop (str): Text to display above the selection.

    Returns:
        tuple: Selected index and the resulting display string.
    """
    current_selection = 0

    while True:
        print(f"{ontop}{constants.ACTIVE_ICON} {title}\n{constants.LINE_UNDER}")

        for index, option in enumerate(options):
            selection_indicator = (
                constants.CIRCLE_FILLED
                if index == current_selection
                else constants.CIRCLE_EMPTY
            )

            # Print the description only for the currently selected option
            if index == current_selection and descriptions:
                print(
                    f"{constants.LINE}  {selection_indicator}    {option}"
                    f"{constants.GREY}    {descriptions[index]}{constants.ANSI_RESET}"
                )

            else:
                print(f"{constants.LINE}  {selection_indicator}    {option}")

        print(constants.TO_RIGHT)
        key = getkey()

        if key in keys.UP and current_selection > 0:
            current_selection -= 1
        elif key in keys.DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key in keys.ENTER:
            break

        clear_screen()

    display_text = f"{constants.TRIANGLE_RIGHT} {title}{constants.ANSI_RESET}\n{constants.LINE_G} {constants.GREY} {options[current_selection]}{constants.ANSI_RESET}\n{constants.LINE_G}"
    return current_selection, display_text


def m_select(title, options, descriptions, ontop=""):
    """
    Allows the user to select multiple options from a list.

    Args:
        title (str): The title of the selection prompt.
        options (list): The list of option strings.
        descriptions (list): List of description strings for each option.
        ontop (str): Text to display above the selection.

    Returns:
        tuple: List of selected items and the resulting display string.
    """
    current_selection = 0
    selected_options = [False] * len(options)  # Tracks which options are selected

    while True:
        print(f"{ontop}{constants.ACTIVE_ICON} {title}\n{constants.LINE_UNDER}")

        for index, option in enumerate(options):
            box_icon = (
                constants.BOX_FULL
                if selected_options[index]
                else constants.BOX_EMPTY_G
            )
            description = (
                f" {constants.GREY}{descriptions[index]}{constants.ANSI_RESET}"
                if descriptions
                else ""
            )
            highlight = constants.GREEN if index == current_selection else ""
            print(
                f"{constants.LINE}  {highlight}{box_icon}{constants.ANSI_RESET}    {option}{description}"
            )

        print(constants.TO_RIGHT)
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

        clear_screen()

    selected_items = [
        options[i] for i, selected in enumerate(selected_options) if selected
    ]
    display_text = f"{constants.TRIANGLE_RIGHT} {title}\n{constants.LINE_G} {constants.GREY} {', '.join(selected_items)}{constants.ANSI_RESET}\n{constants.LINE_G}"
    return selected_items, display_text


def l_select(title, options, descriptions, ontop=""):
    """
    Allows the user to select an option from a list in a horizontal layout.

    Args:
        title (str): The title of the selection prompt.
        options (list): The list of option strings.
        descriptions (list): List of description strings for each option.
        ontop (str): Text to display above the selection.

    Returns:
        tuple: Selected index and the resulting display string.
    """
    current_selection = 0

    while True:
        print(f"{ontop}{constants.ACTIVE_ICON} {title}\n{constants.LINE_UNDER}")
        print(constants.LINE, end="")

        for index, option in enumerate(options):
            selection_indicator = (
                constants.CIRCLE_FILLED
                if index == current_selection
                else constants.CIRCLE_EMPTY
            )
            description = f" {descriptions[index]}" if descriptions else ""
            print(f"  {selection_indicator} {option}{description}", end="")

        print(f"\n{constants.TO_RIGHT}")
        key = getkey()

        if key in keys.LEFT and current_selection > 0:
            current_selection -= 1
        elif key in keys.RIGHT and current_selection < len(options) - 1:
            current_selection += 1
        elif key in keys.ENTER:
            break

        clear_screen()

    display_text = f"{constants.TRIANGLE_RIGHT} {title}\n{constants.LINE_G} {constants.GREY} {options[current_selection]}{constants.ANSI_RESET}\n{constants.LINE_G}"
    return current_selection, display_text


def start(title):
    """
    Displays the start of a prompt sequence.

    Args:
        title (str): The title of the sequence.

    Returns:
        str: Formatted start string.
    """
    start_text = f"{constants.GREY}↱{constants.ANSI_RESET} {constants.BLUE_BACKGROUND} {title} {constants.ANSI_RESET}\n{constants.GREY}{constants.SP_SET[0]}{constants.ANSI_RESET}"
    print(start_text)
    return start_text


def end(title, final_text):
    """
    Displays the end of a prompt sequence along with final text.

    Args:
        title (str): The title of the sequence.
        final_text (str): The final text to display.

    Returns:
        None
    """
    print(
        f"{final_text}{constants.GREY}↳{constants.ANSI_RESET} {constants.BLUE_BACKGROUND} {title} {constants.ANSI_RESET}"
    )
    # Additional text (can be customized or removed)
    extra_text = (
        " "
        + constants.GREY
        + constants.SP_SET[0]
        + "\n "
        + constants.GREY
        + constants.SP_SET[0]
        + constants.ANSI_RESET
        + "Cool right?\n "
        + constants.GREY
        + constants.SP_SET[0]
        + constants.ANSI_RESET
        + "Right\n "
        + constants.GREY
        + constants.SP_SET[0]
        + constants.ANSI_RESET
    )
    print(extra_text)


def begin(name, add_list):
    clear_screen()
    returned_text = start(name)
    add_list.append(returned_text + "\n")
    clear_screen()
    return add_list


def choice(name, content, additions, add_list):
    selected_index, return_text = g_select(name, content, additions, "".join(add_list))
    add_list.append(return_text + "\n")
    clear_screen()
    return selected_index, add_list


def loading(name, times, end_with, add_list):
    return_text = loader(name, times, end_with, "".join(add_list))
    add_list.append(return_text + "\n")
    clear_screen()
    return add_list


def type_f(name, pre_show, error, add_list):
    def is_valid_input(input_text):
        # Replace this with your validation logic
        return input_text == "Toad"

    typed_text, return_text = type_in(
        name, pre_show, error, is_valid_input, "".join(add_list)
    )
    add_list.append(return_text + "\n")
    clear_screen()
    return typed_text, add_list


def multi_select(name, content, additions, add_list):
    selections, return_text = m_select(name, content, additions, "".join(add_list))
    add_list.append(return_text + "\n")
    clear_screen()
    return selections, add_list


def choice_horizontal(name, content, additions, add_list):
    selected_index, return_text = l_select(name, content, additions, "".join(add_list))
    add_list.append(return_text + "\n")
    clear_screen()
    return selected_index, add_list


if __name__ == "__main__":
    clear_screen()
    add_list = []

    # Starting the interactive session
    add_list = begin("Interactive Test Session", add_list)

    # Simple choice selection
    selected, add_list = choice(
        "Select an option",
        ["Option 1", "Option 2", "Option 3"],
        [" cool option", " not so cool", "maybe"],
        add_list,
    )

    # Simulating a loading process
    add_list = loading("Loading...", 24, "Loading Complete!", add_list)

    # Text input
    typed_text, add_list = type_f(
        "Your name", "Enter your name", "Please type a name", add_list
    )

    # Multi-selection
    selections, add_list = multi_select(
        "Choose multiple", ["Choice A", "Choice B", "Choice C"], ["", "", ""], add_list
    )

    # Horizontal choice selection
    selected_horizontal, add_list = choice_horizontal(
        "Select horizontally", ["Left", "Center", "Right"], ["", "", ""], add_list
    )

    print("All interaction history:\n", "".join(add_list))

    # End of the script
    print("End of the interactive test session.")
