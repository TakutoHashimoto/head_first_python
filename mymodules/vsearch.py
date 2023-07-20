def search4vowels(word: str) -> set:
    """
    指定された英単語に含まれる母音を返す。
    """
    vowels = set("aeiou")
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = "aeiou") -> set:
    """
    指定された英単語に含まれる母音を返す。
    """
    return set(letters).intersection(set(phrase))


if __name__ == "__main__":
    print(search4letters("galaxy", "xyz"))
