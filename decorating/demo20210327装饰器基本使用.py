# 最简单的装饰器
def text():
    return "Hello World!"


def add_itali(func):
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


if __name__ == '__main__':
    print(add_itali(text)())
