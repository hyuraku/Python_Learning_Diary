import os

#指定のファイル、フォルダがあるかどうか
print(os.path.exists('test.txt'))

#指定のファイルがファイル形式化どうか
print(os.path.isfile('test.txt'))

#指定のフォルダがフォルダなのかどうか
print(os.path.isdir('design'))

#os.rename('test.txt','rename.txt')

#os.symlink('test.txt','symlink.txt')

#os.mkdir('test_dir')
#os.rmdir('test_dir')
