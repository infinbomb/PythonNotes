import re

# [] . ^ $ * + ? {} () \ | *metacharacters

# [] finds the # of any of the characters in the brackets
# [a-e] is same as [abcde]
# [1-4] is same as [1234]
# ^ indicates anything but this value: [^0-9]=no numbers

# . indicates anything with . # of characters
# .. looks for 2 characters "a"=0, "ab"=2, "abc"=1, "abcd"=2

# ^ looks if it starts with indicated character
# ^a = does it start with "a", or ^ab = starts with ab?

# $ does it end with characters 
# character goes before -> a$   

#   


# EXAMPLES
txt = 'I Love Swim Pracs in 25 Yard Pools'
x = re.search("^I.*Pools$", txt)
# looks for a string that starts with I and ends with pools
if x:
    print("Match!")
else:
    print("No Match!")

print("______________________")
words_with_pattern = []
words = txt.split()
pattern = '^P...s$'
# pattern is 5 letter word that starts with P and ends with s

for word in words:
    print(word)
    if re.match(pattern, word):
        words_with_pattern.append(word)
        print("Word Added!")
    else:
        print("No Match")
        
print(words_with_pattern)
