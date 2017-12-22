i=[1,2,3]
t=5

#下のコマンドを実行するとエラーが発生する
#i[t]

#そこで例外処理を行う
try:
    i[t]
except:
    print("Don't do that")

#IndexErrorが起きた場合の例外処理
#excにはエラーの内容が入っている
try:
    i[t]
except IndexError as exc:
    print("Don't do that:{}".format(exc))
