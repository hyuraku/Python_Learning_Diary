#カッコ内にはpbjectやselfを入れるほうがよい。
class Person(object):
    def __init__(self,name='Mike'):
        self.name=name

    def say_some(self):
        print('I am {}'.format(self.name))

class teacher(Person):
    def __init__(self,subject='Japanese'):
        self.subject=subject

    def teach(self):
        print('I teach {}'.format(self.subject))

he=teacher('math')
he.teach()
