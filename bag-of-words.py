sentences = "The AI is the one of the greatest creation in the history of computer science, ai have capcity of doing the complex task ai has buid to make human life easier  "
target_word = "ai"
count = 0

lower_sntence = sentences.lower()
word_list = lower_sntence.split()
for word in word_list:
    if word == "ai":
        count += 1

print (f"The word {target_word} appears {count} Times.")