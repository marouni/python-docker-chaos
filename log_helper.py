import colorlog
import logging

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(asctime)s %(log_color)s%(levelname)s : %(message)s'))

logger = colorlog.getLogger('docker_chaos')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_logger():
    return logger


def enable_debug_level():
    logger.setLevel(logging.DEBUG)