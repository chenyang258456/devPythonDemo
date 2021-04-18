from functools import reduce
from typing import Iterator


def f(stu: dict):
    return stu['age']


def sort_test():
    students = [{"name": "hong", "age": 18, "sex": "m"},
                {"name": "huang", "age": 16},
                {"name": "lan", "age": 17},
                ]
    # soterd 方法 key:根据传递的参数进行排序
    print(sorted(students, key=lambda student: student['age'], reverse=True))
    print(sorted(students, key=f, reverse=True))


# map函数

# [x,y,z]->map->[f(x),f(y),f(z)]
def map_test(keys: list, values: list) -> Iterator:
    return map(lambda key, value: {key: value}, keys, values)


print(list(map(lambda x, y: {x: y}, (1, 2, 3, 4, 5), (6, 7, 8, 9, 10))))


# reduce
# 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
def reduce_test():
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))


# filter
list_demo = [2, 3, 4, 5, 6, 78, 9]
list_demo_2 = list(filter(lambda x: x % 2 == 0, list_demo))
print(list_demo_2)


# zip
def zip_test():
    list_1 = [1, 2, 3]
    list_2 = ['a', 'b', 'c']
    for i in zip(list_1, list_2):
        print(i)


if __name__ == '__main__':
    sort_test()
    reduce_test()
    list_demo = [2, 3, 4, 5, 6, 78, 9]
    list_demo_2 = list(filter(lambda x: x % 2 == 0, list_demo))
    print(list_demo_2)
    zip_test()
