def search4vowels(word: str) -> set:
    """
    指定された英単語に含まれる母音を返す。
    """
    vowels = set("aeiou")

    return vowels.intersection(set(word))


if __name__ == "__main__":
    word = input("入力：")
    print(search4vowels(word))
