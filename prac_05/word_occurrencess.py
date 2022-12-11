"""
Word Occurrences
Estimate: 15 minutes
Actual:   12 minutes
"""
word_count = {}
text = input("Text: ")
words = text.split()
longest_len = 0
for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
    if len(word) > longest_len:
        longest_len = len(word)
for word in sorted(word_count.keys()):
    print(f"{word:{longest_len}} : {word_count[word]}")
