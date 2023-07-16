word = "bottles"

for beer_num in range(99, 0, -1):
    print(f"{beer_num} {word} of beer on the wall.")
    print(f"{beer_num} {word} of beer.")

    print("Take one down.")
    print("Pass it around.")

    if beer_num == 1:
        print(f"No more {word} of beer on the wall.")
    else:
        if (beer_num - 1) == 1:
            word = "bottle"
        print(f"{beer_num-1} {word} of beer on the wall.")

    print()
