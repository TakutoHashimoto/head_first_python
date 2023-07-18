vowels = set("aeiou")
word = input("英単語を入力してください。母音を探します：")

found = vowels.intersection(set(word))

print(*found, sep="\n")
