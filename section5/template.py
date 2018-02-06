import string

s=  """\

Hi $name

$contents

Have a good day
"""
#sを読み込み専用に使う時にTempleteを使用する
t=string.Template(s)

contents=t.substitute(name='Mike',contents='How are you')
print(contents)

#こんな読み込みもあり、対象ファイルを書き換えを防ぐことができる
with open('design/email_templete.txt') as f:
    t=string.Template(f.read())
contents2=t.substitute(name='Taro',contents='You look good.')
print(contents2)
