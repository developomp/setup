from src.util import paru_install, copy_file
from src.constants import content_dir, home_dir
from src import log

from os.path import isdir
from os import system

name = "Zsh"


def setup():
    """Objectively better shell"""

    paru_install("zsh")

    if isdir(f"{home_dir}/.oh-my-zsh"):
        log.log("zsh already configured. Skipping.")
        return

    # install oh my zsh
    system(
        'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    )

    # install powerlevel10k theme
    system(
        "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
    )

    # install syntax highlighter
    system(
        "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
    )

    # apply zshrc configuration
    copy_file(f"{content_dir}{home_dir}/.zshrc", "~/.zshrc")
