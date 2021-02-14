import logging
import ovisbot.utils.logging

from colorama import init as colorama_init

from ovisbot.bot import OvisBot

logger = logging.getLogger(__name__)


def launch():
    colorama_init(autoreset=True)

    bot = OvisBot()
    bot.launch()


if __name__ == "__main__":
    launch()
