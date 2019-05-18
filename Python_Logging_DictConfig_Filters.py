# Python Application Logging
# Configuring filters with dictConfig()
# This script shows how you can pass configuration data to the callable 
# which constructs the instance, in the form of keyword parameters.

import logging
import logging.config
import sys

class MyFilter(logging.Filter):

    def __init__(self, param=None):
        self.param = param

    def filter(self, record):

        if self.param is None:
            allow = True

        else:
            allow = self.param not in record.msg

        if allow:
            record.msg = 'changed: ' + record.msg
        return allow

LOGGING = {
    'version': 1,
    'filters': {
        'myfilter': {
            '()': MyFilter,
            'param': 'noshow',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['myfilter']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
}

if __name__ == '__main__':

    logging.config.dictConfig(LOGGING)
    logging.debug('hello')
    logging.debug('hello - noshow')
