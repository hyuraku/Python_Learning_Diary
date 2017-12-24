#独自例外の作成
raise IndexError('fire!')

#独自例外のクラス作成
class UppercaseError(Exception):
    pass

def check():
    #リストの中に一つだけ大文字の単語を入れて、エラーを発生させる。
    words=['APPLE','orange','grape']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

check()
