"""
@Project   : decaNLP
@Module    : logger_setup.py
@Created   : 8/3/18 11:42 AM
@Desc      : 配置logger
"""
import logging


def define_logger(rank='default'):
    logger = logging.getLogger(f'process_{rank}')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(lineno)d - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def get_logger(rank='default'):
    logger = logging.getLogger(f'process_{rank}')
    return logger
