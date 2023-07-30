def myfunc(*args):
    print(*args, end=" ")

    if args:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep="->", end=" ")

    if kwargs:
        print()


def myfunc3(*args, **kwargs):
    if args:
        print(*args, end=" ")
        print

    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep="->", end=" ")
        print()
