# 类的装饰器 格式
# def 装饰器名(cls):
#     装饰代码
#     return cls
import time

name = "小明"


def add_name(cls):
    cls.name = name
    return cls


@add_name
class A(object):
    pass


# 装饰器类
# 格式如下：
# class 装饰器名(object):
#     def __init__(self,func):
#         self.func = func
#         pass
#     def __call__(self, *args, **kwargs):
#         pass #写装饰代码
#         return self.func(*args,**kwargs)


class B(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("hello everyone")
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'{self.func.__name__} 执行了{end - start}')
        return result


@B
def add(a, b):
    time.sleep(1)
    return a + b


# 类装饰器装饰类
class C(object):
    def __init__(self, cls):
        self.cls = cls
        self.name = "笑话"

    def __call__(self, *args, **kwargs):
        print("hello everyone")
        start = time.time()
        self.cls.name = self.name
        end = time.time()
        print(f'{self.cls.__name__} 执行了{end - start}')
        return self.cls


@C
class DemoC(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = A()
    print(a.name)
    print(add(1, 2))
    c = DemoC()
    print(c.name)
