class Next(object):
    """NOTE:

    迭代器：必须包含__iter()__与__next__()  __iter__方法要求返回值必须是一个“迭代器(返回值必须有__next__方法)”
          可以被for迭代，for迭代迭代器时，会执行__next__方法
          迭代器是特殊的可迭代对象
          核心：通过__next__记录迭代的位置
    可迭代对象：包含__iter()__
    生成器：目的--获得迭代器对象
    1.是特殊的迭代器
    2.如何创建生成器对象，通过关键字yield记住函数执行的状态
    当执行next(g)时，会执行g里面的yield
    yield与return的区别:yield暂时退出，还会回来  return彻底退出
    """

    def __init__(self, stop, start=0):
        self.stop = stop
        self.start = start

    def __next__(self):
        if self.start >= self.stop - 1:
            raise StopIteration
        self.start += 1 #用累加1生成新的数据
        return self.start


class Range(object):
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return Next(self.stop)


from typing import Iterator
class Student(Iterator):
    def __init__(self):
        self.student = [
            "hong",
            "huang",
            "lan"
        ]
        self.index = 0

    # def __iter__(self):
    #     return iter(self.student)
    def __next__(self):
        if self.index >=len(self.student):
            raise StopIteration
        self.index+=1
        return self.student[self.index-1]

def f():

    yield "hong"
    yield "huang"
    yield "lan"


if __name__ == '__main__':
    # for item in Range(10):
    #     print(item)
    # myRange = Range(10)
    # numbers = myRange.__iter__()
    # i = 0
    # while i<=10:
    #     print(numbers.__next__())
    #     i += 1
    # s = Student()
    # for i in s:
    #     print(i)

    g = f()
    for i in g:
        print(i)

