alphabet ={
 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}

phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer at sapien a purus luctus tristique. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed vel turpis eget turpis sollicitudin volutpat. Suspendisse potenti. Nullam consequat, felis vel facilisis dictum, justo libero ultrices est, in laoreet sapien magna non purus. Donec at gravida erat. Morbi nec tincidunt erat. Maecenas vehicula augue eu est bibendum, id vene"

for letter in phrase:
    low_letter = letter.lower()
    if low_letter in alphabet:
        alphabet[low_letter] += 1
    else:
        alphabet[low_letter] = 1
print(alphabet)
