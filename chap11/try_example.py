try:
    with open("myfile.txt") as f:
        file_read = f.read()

    print(file_read)
except FileNotFoundError:
    print("データファイルがありません。")
