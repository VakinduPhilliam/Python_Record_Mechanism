# Python Application Logging
# Customized exception formatting
# There might be times when you want to do customized exception 
# formatting - for argument�s sake, let�s say you want exactly 
# one line per logged event, even when exception information is 
# present. 

import logging

class OneLineExceptionFormatter(logging.Formatter):

    def formatException(self, exc_info):
        """
        Format an exception so that it prints on a single line.
        """
        result = super(OneLineExceptionFormatter, self).formatException(exc_info)
        return repr(result)  # or format into one line however you want to

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)

        if record.exc_text:
            s = s.replace('\n', '') + '|'
        return s

def configure_logging():

    fh = logging.FileHandler('output.txt', 'w')
    f = OneLineExceptionFormatter('%(asctime)s|%(levelname)s|%(message)s|',
                                  '%d/%m/%Y %H:%M:%S')
    fh.setFormatter(f)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(fh)

def main():

    configure_logging()

    logging.info('Sample message')

    try:
        x = 1 / 0

    except ZeroDivisionError as e:
        logging.exception('ZeroDivisionError: %s', e)

if __name__ == '__main__':
    main()
