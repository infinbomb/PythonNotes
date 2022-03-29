import random

words = ["mines", "clock", "slock", "slice"]

random_word = random.choice(words)

guess = input("input word: ")

for a in range(6):
    line = ""
    for l in range(len(list(guess))):
        if l == list(random_word)[l]:
            line += random_word[l]
        else:
            line += "_"

    print(line)