#docstring とは説明文のこと。

#example

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
