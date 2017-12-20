#火曜日だけ小文字で間違っている
week=['Mon','tue','Wed','Thu','Fri','Sat','Sun']

def word_change(words,func):
    for word in words:
        print(func(word))

'''
def sample_func(word):
    return word.capitalize()
'''
#この時関数に括弧、()は必要ない
word_change(week,sample_func)


'''
上ではsample_funcを２行に渡って書いたが
ラムダを使うと一行で書ける
'''

#最初のwordは引数の扱い
#次のword.capitalize()は処理内容
sample_func = lambda word:word.capitalize()

#こうやって書くこともできる
word_change = (week ,lambda word:word.capitalize())

#ラムダを使うことで実装するまでのコードを書く量を減らせる
