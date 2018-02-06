class Person(object):
    def __init__(self,name='Mike'):
        #自身に値を保持している
        self.name=name

    def say_some(self):
        print('I am {}'.format(self.name))
        self.run()

    def run(self):
        print('run')

    def __del__(self):
        print('good bye')



class Teacher(Person):
    def __init__(self,name='Tim',subject='Japanese',age=30,place='A_City'):
        #self.name = name
        super().__init__(name)
        self.subject=subject
        # _ をつけることで外部からの変更を防ぐ
        #ただ書き換え可能にする方法はある
        self._age = age
        self.__place = place

    #上のageに対してのプロパティ
    @property
    def age(self):
        return self._age

    # _ をつけた変数を書き換えにするコマンド
    @age.setter
    def age(self, how_years_old):
        if how_years_old >= 30:
            self._age = how_years_old
        else:
            raise ValueError

    def where_live(self):
        print('I live in {}'.format(self.__place))
    def teach(self):
        print('I teach {}'.format(self.subject))
    def say_age(self):
        print('I am {} years old'.format(self.age))

teacher = Teacher()
#>good bye

teacher.say_some()
#>I am Tim
#>run

#下のコマンドはエラーになる。
teacher.age =25
teacher.say_age()

teacher.where_live()
