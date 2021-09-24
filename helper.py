import logging
logger = logging.getLogger(__name__)
logger.propagate = False # makes it display or not in the main file
logger.info("hello from helper")