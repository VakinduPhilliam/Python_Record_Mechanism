# Python Application Logging
# Multiple handlers and formatters
# Loggers are plain Python objects. 
# The addHandler() method has no minimum 
# or maximum quota for the number of 
# handlers you may add. Sometimes it will 
# be beneficial for an application to log 
# all messages of all severities to a text 
# file while simultaneously logging errors 
# or above to the console. 
# To set this up, simply configure the 
# appropriate handlers. 
# The logging calls in the application code 
# will remain unchanged.
 

import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger

logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
