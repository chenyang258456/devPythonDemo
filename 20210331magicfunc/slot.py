# 节省内存 限制对象中有哪些属性
# 覆盖__dict__中的属性，限制对象有哪些属性
# 应用场景：创建大量对象，可以用__slots__指定对象属性，减少内存
class MyClass(object):
    __slots__ = ['name', 'age']  # 限制对只有name与age属性

    def __init__(self, name, x):
        self.name = name
        self.x = x


if __name__ == '__main__':
    obj = MyClass('aaaa', 1)
    obj2 = MyClass('bbb', 2)
    print(obj.__slots__)
