import logging

logging.basicConfig(level=logging.INFO)

class NopassFilter(logging.Filter):
    def filter(self,record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NopassFilter())
logger.info('from main')
logger.info('from main password="test" ')
#> INFO:__main__:from main
