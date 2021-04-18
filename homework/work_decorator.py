"""请设计一个装饰器 ,可以给函数扩展登录认证的功能（提示输入账号密码，然后进行校验），

多个函数同时使用这个装饰器， 调用函数的时候，只要登录成功一次， 后续的函数无需再进行登录

（默认的认证账号：qwe123，密码：123456） """


def login(func):
    login_result = []
    print(login_result)

    def wrapper(*args, **kwargs):
        nonlocal login_result
        sum_num = 0
        if not login_result:
            for i in range(3):

                account = input("请输入账号:")
                pwd = input("请输入密码:")
                if account == "qwe123" and pwd == "123456":
                    print("登录成功")
                    result = func(*args, **kwargs)
                    login_result.append(result)
                    return login_result[0]
                else:
                    sum_num += 1
                    print(f"第{sum_num}次账号密码输入错误，还有{3 - sum_num}次机会")
        else:
            return login_result[0]

    return wrapper


class SingletonLogin(object):
    obj = None

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        return self.func(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if not cls.obj:
            sum_num = 0

            for i in range(3):
                account = input("请输入账号:")
                pwd = input("请输入密码:")
                if account == "qwe123" and pwd == "123456":
                    print("登录成功")
                else:
                    sum_num += 1
                    print(f"第{sum_num}次账号密码输入错误，还有{3 - sum_num}次机会")
                    if sum_num==3:
                        print("登陆失败")
            cls.obj = super().__new__(cls)
        return cls.obj


@login
def f_1(a, b):
    return a + b


@login
def f_2(a, b):
    return a + b


if __name__ == '__main__':
    print(f_1(1, 2))
    print(f_2(1, 3))
