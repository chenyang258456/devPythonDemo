"""
上下文管理协议：包含__enter()__和 __exit()__方法
上下文管理器:支持“上下文管理协议”的对象
"""


# 自己定义一个上下文管理器
class MyClass(object):
    def __enter__(self):
        print("enter is running")
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit is running")


def main():
    obj = MyClass()
    with obj as o:  # o = __enter()__的返回值
        print("with is running")


if __name__ == '__main__':
    main()
