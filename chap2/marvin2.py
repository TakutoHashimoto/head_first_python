paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)

for char in letters[:6]:
    print(f"\t{char}")
print()

# f-string内でバックスラッシュが使えないので、文字列連結を使っている
for char in letters[-7:]:
    print("\t"*2, char)
print()

for char in letters[12:20]:
    print("\t"*3, char)
