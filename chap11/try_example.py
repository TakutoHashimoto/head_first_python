try:
    with open("myfile.txt") as f:
        file_read = f.read()

    print(file_read)
except FileNotFoundError:
    print("データファイルがありません。")
except PermissionError:
    print("ファイルへのアクセスが許可されていません。")
except Exception as err:
    print(f"他のエラーが発生しました。{err}")
