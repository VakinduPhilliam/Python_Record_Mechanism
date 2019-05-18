# Python Application Logging
# Using file rotation
# Sometimes you want to let a log file grow to a certain size, 
# then open a new file and log to that. 
# You may want to keep a certain number of these files, and 
# when that many files have been created, rotate the files so 
# that the number of files and the size of the files both 
# remain bounded. 
# For this usage pattern, the logging package provides a 
# 'RotatingFileHandler':
 
import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger

handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20, backupCount=5)

my_logger.addHandler(handler)

# Log some messages

for i in range(20):
    my_logger.debug('i = %d' % i)

# See what files are created

logfiles = glob.glob('%s*' % LOG_FILENAME)

for filename in logfiles:
    print(filename)
