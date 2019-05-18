# Python Application Logging
# Using a context manager for selective logging
# There are times when it would be useful to temporarily change the 
# logging configuration and revert it back after doing something.

import logging
import sys

class LoggingContext(object):

    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.level = level
        self.handler = handler
        self.close = close

    def __enter__(self):

        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)

        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, et, ev, tb):

        if self.level is not None:
            self.logger.setLevel(self.old_level)

        if self.handler:
            self.logger.removeHandler(self.handler)

        if self.handler and self.close:
            self.handler.close()

        # implicit return of None => don't swallow exceptions
