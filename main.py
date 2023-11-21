from core.prompt import clear_screen, begin, choice, loading, multi_select, type_f, \
    choice_horizontal

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
