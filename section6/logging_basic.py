import logging

#logのフォーマットを変えることができる
formatter = '%(levelname)s:%(message)s'
#下のコマンドはlogの日時を表示させる。
formatter = '%(asctime)s:%(message)s'

# デフォルトではwarning以上しか出力されない。
#basicConfigのlevelの設定により、ファイル(test.log)にinfoまで出力された。
#filenameを指定することで別ファイルに保存可能
logging.basicConfig(filename='test.log',level=logging.INFO,format=formatter)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
#formatを使わなくても以下のように式展開が可能になる。
logging.info('info　%s %s','test1','test2')
logging.debug('debug')

"""
>
CRITICAL:root:critical
ERROR:root:error
WARNING:root:warning
INFO:root:info　test1 test2
"""
