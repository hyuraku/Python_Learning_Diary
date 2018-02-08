import logging

#このコマンドを実行しても有効にならなった。
logging.basicConfig(filename='test.log',level=logging.INFO)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

# デフォルトではwarning以上しか出力されない。
#basicConfigのlevelの設定により、ファイル(test.log)にinfoまで出力された。
"""
>
CRITICAL:root:critical
ERROR:root:error
WARNING:root:warning
INFO:root:info
"""
