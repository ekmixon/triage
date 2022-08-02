# Copyright (C) 2020 Hatching B.V.
# All rights reserved.

import json

def prompt_select_options(options, key, f=None):
    print("\nMake your selection by entering the numbers as listed below "
    "separated by spaces and finish with enter.\n")

    for i, option in enumerate(options):
        em = " "
        if option.get("selected"):
            em = ">"
        print(em, i, option[key])
    selection = []
    choices = input("> ")
    for choice in choices.split(" "):
        if choice.strip() == "":
            continue

        try:
            choice = int(choice)
        except ValueError:
            print("Bad input ", choice)
            continue

        if choice < 0 or len(options) <= choice:
            print("Out of range ", choice)
            continue

        if choice in selection:
            continue

        selection.append(choice)

    if f and not f(selection):
        return prompt_select_options(options, key,  f)

    if selection:
        print("You selected:")
    for choice in selection:
        print(" ", options[choice][key])
    return selection
