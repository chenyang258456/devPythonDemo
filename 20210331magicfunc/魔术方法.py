# __str()__ 返回print(obj)时的值

class StrDemo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def str_main():
    print(StrDemo("hi"))


# __add()__实现相加
class AddDemo(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


def add_main():
    print(AddDemo(1) + AddDemo(2))


class SubDemo():
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


def sub_main():
    print(SubDemo(3) - SubDemo(1))


# del：销毁对象  析构？析构就是对象销毁
class DelDemo(object):
    def __init__(self):
        print("init is running")

    def __del__(self):
        print('del is runing')


def del_demo():
    o = DelDemo()

#__getitem__  字典元祖字符串列表等数据类型可根据[]取值是因为具有__getitem__属性
class GetDemo():
    def __init__(self):
        self.item = [1, 2, 3, 4, 5]

    def __getitem__(self, item):
        return self.item[item]

class AttrDemo():
    pass


if __name__ == '__main__':
    obj = AttrDemo()
    print(obj.add())

