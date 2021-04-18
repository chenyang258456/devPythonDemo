# 实现了单例与非单例共存

class MyClass(object):
    __instance = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_singleton_obj(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    a = MyClass.get_singleton_obj()
    b = MyClass.get_singleton_obj()
    print(id(a))
    print(id(b))
