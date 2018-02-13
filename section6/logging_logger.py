import logging

import log_test

logging.basicConfig(level=logging.INFO)

logging.info('info')
#> INFO:root:info

#loggerを使って、ロガーをカスタマイズする
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')
#> DEBUG:__main__:debug

log_test.do_some()
#> INFO:log_test:from log_test
#> INFO:log_test:from log_test debug
