import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *efects: str) -> None:
    """
    print 'text' using the insci sequence to change colour.
    :param text: 
    :param efects:
    :return: 
    """
    effect_string = "".join(efects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)

colorama.init()
colour_print("this is red", RED, BOLD, UNDERLINE, REVERSE)
print("this is print")
colorama.deinit()