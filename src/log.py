# https://stackoverflow.com/a/33206814/12979111

RESET = "\e[0m"

# style
BOLD = "\e[1m"
INVERT = "\e[7m"

# colors
RED = "\e[91m"  # actually light red
GREEN = "\e[92m"  # actually light green
YELLOW = "\e[33m"


def log_no_label(msg: str):
    print(f"{GREEN}{BOLD}{msg}{RESET}")


def warn_no_label(msg: str):
    print(f"{YELLOW}{BOLD}{msg}{RESET}")


def error_no_label(msg: str):
    print(f"{RED}{BOLD}{msg}{RESET}")


def log(msg: str):
    print(f" {GREEN}{BOLD}    INFO |  {msg}{RESET}")


def warn(msg: str):
    print(f" {YELLOW}{BOLD} WARNING |  {msg}{RESET}")


def error(msg: str):
    print(f" {RED}{BOLD}   ERROR |  {msg}{RESET}")


def title(msg: str):
    print(f"\n{BOLD}{GREEN}====================[ {msg} ]===================={RESET}")
