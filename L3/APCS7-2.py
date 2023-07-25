# start
vowel = ["a", "e", "i", "o", "u"]
count = 0

words = input()

for word in words:
    if word.lower() in vowel:
        count += 1
print(count)
