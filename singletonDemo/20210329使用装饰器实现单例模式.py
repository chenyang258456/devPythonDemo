# 使用装饰器实现单例模式

def singleton(cls):
    obj = []

    def wrapper(*args, **kwargs):
        if not obj:
            obj.append(cls(*args, **kwargs))
        return obj[0]

    return wrapper


@singleton
class MyClass(object):
    pass


if __name__ == '__main__':
    print(id(MyClass()))
    print(id(MyClass()))
