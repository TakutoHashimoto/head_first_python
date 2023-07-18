def search4vowels(word):
    """
    英単語に含まれる母音を表示する。
    """
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    print(*found, sep="\n")


if __name__ == "__main__":
    word = input("入力：")
    search4vowels(word)
