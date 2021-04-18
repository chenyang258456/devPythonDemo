#递归

def sum(x):
    if x ==1:
        return 1


    return x+sum(x-1)

#闭包
def func_demo():
    x = 1
    def change_func():
        nonlocal x
        x += 1
        return x
    return change_func





if __name__ == '__main__':
    print(sum(5))
    f=func_demo()
    print(f())
    print(f())
    print(f())