#take a sentence and convert it to lowercase

sentence = input("Write the sentences here:  ").lower()
text = len(sentence)
word = sentence.split()

print(sentence[0:3])
print(f"The total characters in this sentences is.... {len(sentence)}")
print(len(word))