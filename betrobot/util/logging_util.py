import logging


_logger = logging.getLogger('betrobot')
_logger.setLevel(logging.DEBUG)


def get_logger(name=None):
    if name is None:
        return _logger
    else:
        return _logger.getChild(name)
