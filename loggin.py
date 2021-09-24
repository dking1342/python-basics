# logging: ways to track log types and to set up how a log should be configured

import logging
# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
# import helper

###############
# types of logging
# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warning message")
# logging.error("this is an error message")
# logging.critical("this is a critical message")

##############
# setup without config file
# logger = logging.getLogger(__name__)

# logger.warning("this is a warning")
# logger.error("this is an error")

# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("file.log")

# # level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formatter) 
# file_h.setFormatter(formatter) 

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

####################
# using the config file
import logging.config
logging.config.fileConfig("logging.conf") # can also use dictConfig made as a dict

logger = logging.getLogger("simpleExample")
logger.debug("this is a debugger message")


##################
# using a try except method to do this stuff
import traceback

try:
    a = [1,2,3]
    val = a[4]
except: # if you do not know the type of error
    logging.error(f"the error is {traceback.format_exc()}")
# except IndexError as e: # if you know the type of error
#     logging.error(e,exc_info=True)


##################
# rotating file handler
# recommend using json format for real world type of activities
from logging.handlers import RotatingFileHandler # size/space based
from logging.handlers import TimedRotatingFileHandler # time based
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("app.log",maxBytes=2000,backupCount=5)
t_handler = TimedRotatingFileHandler("timed.log",when="s",interval=5,backupCount=5)
logger.addHandler(handler)
logger.addHandler(t_handler)

for _ in range(6):
    logger.info("hello world")
    time.sleep(6)

