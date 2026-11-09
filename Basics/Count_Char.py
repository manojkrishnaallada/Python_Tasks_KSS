#Count how many times each character appears in "programming"

word = "programming"
freq = {}
for ch in word:
    freq[ch] = word.count(ch)
print(freq)

