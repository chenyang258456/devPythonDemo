import logging


def log(filename: str = 'a.log'):
    def inner(func):  # func用来接收被装饰的函数
        def wrapper(*args, **kwargs):  # *args **kwargs 用来接受被装饰的函数的参数
            print(filename)
            logging.warning(f"{func.__name__} is running")  # 装饰的代码
            result = func(*args, **kwargs)  # 调用被装饰的函数
            return result  # 把被装饰的函数的运行结果返回

        return wrapper  # 返回包装器

    return inner


class C(object):
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func, *args, **kwargs):
        def warpper(*args, **kwargs):
            print(self.filename)
            logging.warning(f"{func.__name__} is running")
            result = func(*args, **kwargs)
            return result

        return warpper


@C(filename="aaa.log")
# @log(filename="aaa.log")
def f(a, b):
    return a + b


if __name__ == '__main__':
    print(f(1, 1))
