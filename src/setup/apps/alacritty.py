from src.constants import content_dir
from src.util import pamac_install, copy_file

from os import makedirs

name = "Alacritty terminal"


def setup() -> None:
    """terminal app written in rust"""

    pamac_install("alacritty")

    # copy configuration file
    copy_file(
        f"{content_dir}/home/pomp/.config/alacritty/alacritty.yml",
        "~/.config/alacritty/alacritty.yml",
    )
