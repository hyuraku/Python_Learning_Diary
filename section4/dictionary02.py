#辞書型は参照型のデータなので
#単なる代入では複製できない
x={'a':1}
y=x

print(id(x),id(y))
#> 4381234088 4381234088

#複製するなら以下のコマンド
y=x.copy()
y['a']=100
print(id(x),id(y))
#> 4381234088 4381172360
