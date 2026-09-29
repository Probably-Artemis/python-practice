"""
Objective: output each word in text along with the number of times it appears. Then output the most common word and its count. Capitalization and the periods at the end of sentences should be ignored.
Restriction: you may not edit preexisting code, and you may not import anything.
"""

text = "The sun rose. The birds sang. The sun set and the birds slept."

counts = {}

for word in text.lower().replace(".", "").split():
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(word, count)

most_common = ""
highest = 0

for word, count in counts.items():
    if count > highest:
        most_common = word
        highest = count

print("Most common:", most_common, highest)

# max(counts, key=counts.get) finds the same word in one line. key tells max() what to compare instead of the keys themselves.