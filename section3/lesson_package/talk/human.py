#上のコマンドは絶対パス
#下のコマンドは相対パス
#from lesson_package.tool import plus
from ..tool import plus
def sing():
    return 'Sing'

def cry():
    return plus.say_double('Cry')
