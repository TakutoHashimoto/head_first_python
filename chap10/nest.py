def outer():

    def inner():
        print("これは内部関数です。")

    print("これは外部関数なので内部関数を呼び出します。")

    inner()
