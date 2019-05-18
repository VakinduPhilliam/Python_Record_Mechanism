# Python Application Logging
# Logging to multiple destinations
# Let�s say you want to log to console and file 
# with different message formats and in differing 
# circumstances. 
# Say you want to log messages with levels of DEBUG 
# and higher to file, and those messages at level 
# INFO and higher to the console. 
# Let�s also assume that the file should contain timestamps, 
# but the console messages should not. 
# Here�s how you can achieve this:
 
import logging

# set up logging to file

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/temp/myapp.log',
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr

console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format which is simpler for console use

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format

console.setFormatter(formatter)

# add the handler to the root logger

logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...

logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
