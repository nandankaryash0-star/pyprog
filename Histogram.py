words = ["apple","banana","apple","orange", "banana", "apple"]
frequency = {}

for w in words:
    if w in frequency:
        frequency[w] = frequency[w] + 1
    else:
        frequency[w] = 1

print("Word Counts",frequency)