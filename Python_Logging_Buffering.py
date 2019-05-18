# Python Application Logging
# Buffering logging messages and outputting them conditionally
# There might be situations where you want to log messages in 
# a temporary area and only output them if a certain condition 
# occurs. 

import logging
from logging.handlers import MemoryHandler
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def log_if_errors(logger, target_handler=None, flush_level=None, capacity=None):

    if target_handler is None:
        target_handler = logging.StreamHandler()

    if flush_level is None:
        flush_level = logging.ERROR

    if capacity is None:
        capacity = 100

    handler = MemoryHandler(capacity, flushLevel=flush_level, target=target_handler)

    def decorator(fn):

        def wrapper(*args, **kwargs):
            logger.addHandler(handler)

            try:
                return fn(*args, **kwargs)

            except Exception:
                logger.exception('call failed')
                raise

            finally:
                super(MemoryHandler, handler).flush()
                logger.removeHandler(handler)

        return wrapper

    return decorator

def write_line(s):
    sys.stderr.write('%s\n' % s)

def foo(fail=False):

    write_line('about to log at DEBUG ...')
    logger.debug('Actually logged at DEBUG')

    write_line('about to log at INFO ...')
    logger.info('Actually logged at INFO')

    write_line('about to log at WARNING ...')
    logger.warning('Actually logged at WARNING')

    if fail:

        write_line('about to log at ERROR ...')
        logger.error('Actually logged at ERROR')

        write_line('about to log at CRITICAL ...')
        logger.critical('Actually logged at CRITICAL')

    return fail

decorated_foo = log_if_errors(logger)(foo)

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)
    write_line('Calling undecorated foo with False')

    assert not foo(False)
    write_line('Calling undecorated foo with True')

    assert foo(True)
    write_line('Calling decorated foo with False')

    assert not decorated_foo(False)
    write_line('Calling decorated foo with True')

    assert decorated_foo(True)
