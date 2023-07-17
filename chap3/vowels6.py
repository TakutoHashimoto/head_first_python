vowels = ["a", "e", "i", "o", "u"]
word = input("英単語を入力してください。母音を探します：")

found = {}

for letter in word:
    if letter in vowels:
        # setdefaultは存在しないキーを指定のデフォルト値に初期化する（もしくは何もしない）
        # https://docs.python.org/ja/3/library/stdtypes.html?highlight=dict#dict.setdefault
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(f"{k} の出現回数は {v} 回")
