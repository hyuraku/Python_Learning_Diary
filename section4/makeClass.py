# カッコ内にはpbjectを書いたほうがよい。
# 別に書かなくてもpython3では動く


class Person(object):
    # コンストラクタ:オブジェクト生成時に実行されるメソッド
    #__inin__
    def __init__(self, name='Mike'):
        # 自身に値を保持している
        self.name = name

    def say_some(self):
        # selfをつけて、保持している値にアクセスしている。
        print('I am {}'.format(self.name))
        # class内のメソッドもselfでアクセスできる。
        self.run()

    def run(self):
        print('run')

    # デストラクタ:オブジェクトが使われなくなったときに実行されるメソッド
    #__del__
    def __del__(self):
        print('good bye')


# クラス生成
person = Person()
person.say_some()
#>I am Mike
#>run

person2 = Person('John')
person2.say_some()
#>I am John
#>run
#>good bye #これはオブジェクトpersonが使われない時に実行された
#>good bye #これはオブジェクトperson2が使われない時に実行された
