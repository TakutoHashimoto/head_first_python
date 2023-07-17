vowels = ["a", "e", "i", "o", "u"]
word = input("英単語を入力してください: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(*found)
