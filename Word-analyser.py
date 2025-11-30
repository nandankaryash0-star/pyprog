#This program analyse the word

paragraph = input("Write the paragraph here: ")

word = paragraph.split()
longest = max(word,key=len)
smallest = min(word,key=len)

print(f"The words is {word}")
print(len(word))
print(longest,"--This is the longest word ")
print(smallest,"--This is the smallest word")