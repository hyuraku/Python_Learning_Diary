def say_something(word1,word2,word3):
    print(word1)
    print(word2)
    print(word3)

say_something('Hi','Mike','Hello')

#まとめてタプルに入れることができる。
def say_something2(*args):
    print(args)

say_something2('Hi','Mike','Hello')

#最初のは出力させたいが、いくつ出力されるのか分からない場合
def say_something3(word,*args):
    print(word)
    print(args)

say_something3('Hi','Mike','Hello')
