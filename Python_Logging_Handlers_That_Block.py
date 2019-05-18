# Python Application Logging
# Dealing with handlers that block
# The advantage of having a separate QueueListener class 
# is that you can use the same instance to service multiple 
# QueueHandlers. This is more resource-friendly than, say, 
# having threaded versions of the existing handler classes, 
# which would eat up one thread per handler for no particular 
# benefit.
# An example of using these two classes follows (imports omitted):

import logging
import logging.config
import time
import os
import socket, sys, struct
 
que = queue.Queue(-1)  # no limit on size
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
listener = QueueListener(que, handler)
root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(threadName)s: %(message)s')
handler.setFormatter(formatter)
listener.start()

# The log output will display the thread which generated
# the event (the main thread) rather than the internal
# thread which monitors the internal queue. This is what
# you want to happen.

root.warning('Look out!')
listener.stop()

