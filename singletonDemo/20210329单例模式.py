class Demo(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


# 单例模式
class MyClass(object):
    obj = None

    def __new__(cls, *args, **kwargs):
        """如果对象已创建，就直接把创建的对象返回
        如果对象未创建，创建对象，并把对象返回"""
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj


if __name__ == '__main__':
    print(type(Demo()))
    print(id(MyClass()))
    print(id(MyClass()))
