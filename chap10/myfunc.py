def myfunc(*args):
    print(*args, end=" ")

    if args:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep="->", end=" ")

    if kwargs:
        print()
