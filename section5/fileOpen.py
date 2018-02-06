f=open("test.txt",'w')#'W'は書き込み、'a'は追加で書き込み
f.write("Hello Tokyo\n")
print('Who is he', file=f)
f.close()
