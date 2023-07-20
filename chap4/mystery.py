"""
値渡しと参照渡しのサンプルコード
"""

def double(arg):
    print(f"実行前: {arg}")
    arg *= 2
    print(f"実行後: {arg}")


def change(arg):
    print(f"実行前: {arg}")
    arg.append("さらなるデータ")
    print(f"実行後: {arg}")
