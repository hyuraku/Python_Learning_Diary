with open("samp.txt","r")as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(4))
