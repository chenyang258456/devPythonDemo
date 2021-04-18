# 需求：写一个装饰器，能多任意函数进行装饰,装饰器的功能就是记录日志
import logging
import time


def log(func):
    def wrapper(*args, **kwargs):
        logging.warning(f"{func.__name__} is running")
        return func(*args, **kwargs)

    return wrapper


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 运行了{end - start}')
        return result

    return wrapper


@log
@calc_time
def f(a, b):
    time.sleep(1)
    return a + b


if __name__ == '__main__':
    print(f(1, 2))
