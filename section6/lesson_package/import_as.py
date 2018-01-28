#よく書かれるコマンドは以下の2つ
#import lesson_package.u_tell
#from lesson_package import u_tell as Ut
#from lesson_package.talk import human

#下の書き方は好まれてない
#from lesson_package.u_tell import say_twice

#from lesson_package.talk import animal

#talkフォルダにあるファイルをまとめてimportする
#しかし、どれがインポートされるかは外部からわからないのであまり使わないほうがよい
from lesson_package.talk import *

#print(Ut.say_twice('Hey'))
#> Hey!Hey!

#print(say_twice(('Bye')))
#> Bye!Bye!

print(human.sing())
#> Sing

print(human.cry())
#> Cry%Cry%

print(animal.sing())
print(animal.cry())
