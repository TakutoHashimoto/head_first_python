"""
Don't panicという文字列をon tapという文字列に変換する
リストに対する操作のみで実現する
"""


phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


for _ in range(4):
    plist.pop()

plist.remove("'")
plist.remove("D")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))


new_phrase = "".join(plist)
print(plist)
print(new_phrase)