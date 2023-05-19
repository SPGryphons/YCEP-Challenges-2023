class ExitProgram(Exception):
    "Exits the program cleanly."
    pass

class ContinueProgram(Exception):
    "Allows program to continue from where it stopped off."
    pass