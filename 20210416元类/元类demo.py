class MyClass(object):
    pass


def study():
    pass


def __init__(self, name):
    self.name = name


def hello(self):
    print(f'My name is{self.name}')


# 所有累都是type创建的对象
# 'Student'类名 ‘（object,）继承的对象’,后面字典内为类中的属性
Student = type('Student', (object,), {
    '__init__': __init__,
    'say': hello
})

if __name__ == '__main__':
    stu = Student("小明")
    stu.say()
    print("hello")