# Python Application Logging
# Use of alternative formatting styles

import logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler()

bf = logging.Formatter('{asctime} {name} {levelname:8s} {message}',
                       style='{')
handler.setFormatter(bf)
root.addHandler(handler)
logger = logging.getLogger('foo.bar')
logger.debug('This is a DEBUG message')

# Displays '2010-10-28 15:11:55,341 foo.bar DEBUG   This is a DEBUG message'

logger.critical('This is a CRITICAL message')

# Displays '2010-10-28 15:12:11,526 foo.bar CRITICAL This is a CRITICAL message'

df = logging.Formatter('$asctime $name ${levelname} $message',
                     style='$')

handler.setFormatter(df)
logger.debug('This is a DEBUG message')

# Displays '2010-10-28 15:13:06,924 foo.bar DEBUG This is a DEBUG message'

logger.critical('This is a CRITICAL message')

# Displays '2010-10-28 15:13:11,494 foo.bar CRITICAL This is a CRITICAL message'
