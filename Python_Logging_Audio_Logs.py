# Python Application Logging
# Speaking logging messages (Audio Logs)
# There might be situations when it is desirable to have logging messages 
# rendered in an audible rather than a visible format. 
# This is easy to do if you have text-to-speech (TTS) functionality available 
# in your system, even if it doesn’t have a Python binding. 
# Most TTS systems have a command line program you can run, and this can be 
# invoked from a handler using subprocess.

import logging
import subprocess
import sys

class TTSHandler(logging.Handler):

    def emit(self, record):
        msg = self.format(record)

        # Speak slowly in a female English voice

        cmd = ['espeak', '-s150', '-ven+f3', msg]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        # wait for the program to finish

        p.communicate()

def configure_logging():

    h = TTSHandler()
    root = logging.getLogger()
    root.addHandler(h)

    # the default formatter just returns the message

    root.setLevel(logging.DEBUG)

def main():
    logging.info('Hello')
    logging.debug('Goodbye')

if __name__ == '__main__':
    configure_logging()
    sys.exit(main())
