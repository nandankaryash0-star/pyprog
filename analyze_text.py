def analyze_text(text):

    words = text.lower().split()

    stats = {}

    for w in words:
        if w in stats:
            stats[w] += 1
        else:
            stats[w] = 1

    return stats

sample_text = "AI is great. AI is future. I love AI."
result = analyze_text(sample_text)
print(result)
