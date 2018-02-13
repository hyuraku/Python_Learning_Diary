import logging

logger= logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#指定のファイルに出力させたい場合はFileHandlerを使う
h= logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_some():
    logger.info('from log_test')
    logger.info('from log_test debug')
