# Python Application Logging
# Customizing handlers with dictConfig()

import logging, logging.config, os, shutil

def owned_file_handler(filename, mode='a', encoding=None, owner=None):

    if owner:

        if not os.path.exists(filename):

            open(filename, 'a').close()
        shutil.chown(filename, *owner)

    return logging.FileHandler(filename, mode, encoding)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'file':{
 
            # The values below are popped from this dictionary and
            # used to create the handler, set the handler's level and
            # its formatter.

            '()': owned_file_handler,
            'level':'DEBUG',
            'formatter': 'default',

            # The values below are passed to the handler creator callable
            # as keyword arguments.

            'owner': ['pulse', 'pulse'],
            'filename': 'chowntest.log',
            'mode': 'w',
            'encoding': 'utf-8',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('mylogger')
logger.debug('A debug message')
