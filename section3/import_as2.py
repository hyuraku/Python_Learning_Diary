#ファイルの場所がわからない場合
#エラーを発生させることも可能
try:
    from lesson_package import plus
except ImportError:
    from lesson_package.tool import plus

print(plus.say_double('Good'))
