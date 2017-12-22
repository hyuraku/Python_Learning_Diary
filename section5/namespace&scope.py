animal='cat'

def sample():
    #グローバル変数をローカル変数として扱うための宣言
    global animal
    animal='dog'
    fish='salmon'
    #ローカル変数とその値を出力する
    print(locals())
    print(animal)

sample()
#グローバル変数とその値を出力する
print(globals())
