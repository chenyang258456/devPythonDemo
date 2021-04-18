# 最简单的装饰器
def add_itali(func):
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


@add_itali
def text():
    return "Hello World!"


if __name__ == '__main__':
    print(text())
