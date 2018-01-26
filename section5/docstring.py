#docstring とは説明文のこと。

#自作のメソッドの中に以下のような説明文のコメント書けば、helpコマンドでコメント出力される。
def exam_fun(param1,param2):
    """
    これはDocstringの説明文

    Args:
        param1(int):first parameter
        param2(str):second parameter

    Return:
        bool:return bvalue.true for success,false otherwise

    """
    print(param1)
    print(param2)
    return True

help(exam_fun)
'''
>
Help on function exam_fun in module __main__:

exam_fun(param1, param2)
    これはDocstringの説明文

    Args:
        param1(int):first parameter
        param2(str):second parameter

    Return:
        bool:return bvalue.true for success,false otherwise
'''
