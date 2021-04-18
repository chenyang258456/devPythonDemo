class MyMetaClass(type):
    def __new__(mcs, name, bases: tuple, attrs):
        """
        创建对象（这个对象是一个类）
        :param name: 字符串，类的名称
        :param bases: 元祖（基础类1，基础类2.。。。）
        :param attrs: 字典（__dict__属性）
        """
        name = 'Person'
        attrs['name'] = '某人'
        attrs['age'] = 18
        bases = (object,)
        return super().__new__(mcs, name, bases, attrs)


# metaclass 指定类是由谁创建的
class MyClass(object, metaclass=MyMetaClass):
    pass


if __name__ == '__main__':
    print(MyClass.__dict__)
    print(MyClass.name)
    print(MyClass.__bases__)
