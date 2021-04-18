# __dict__

class DictDemo(object):
    def __init__(self):
        self.name = "li"
        self.age = 18

    def __setattr__(self, key, value):
        print("__setattr__ is running")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("__delattr__ is running ")
        if item == "name":
            raise AttributeError("name 属性不允许删除")
        elif item == "age":
            super().__delattr__(item)


if __name__ == '__main__':
    print(DictDemo.__dict__)
    print(DictDemo().__dict__)

    obj = DictDemo()
    obj.name = "陈"
    print(obj.name)
    del obj.age
    print(obj.age)
