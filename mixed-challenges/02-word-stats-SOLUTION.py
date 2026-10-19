"""
Objective: for the text given, ignoring capitalization and the punctuation ,.;!? at the ends of words, output: the total number of words, the number of different words, the longest word (the first one, if there's a tie), the most common word and how many times it appears (the first one to appear in the text, if there's a tie), the average word length rounded to two decimal places, and a sorted list of the words that appear exactly once.
Restriction: you may not edit preexisting code.
"""

text = "It was the best of times, it was the worst of times; it was the age of wisdom, it was the age of foolishness. It was the epoch of belief!"

words = [w.strip(",.;!?").lower() for w in text.split()]

print("Total words:", len(words))
print("Different words:", len(set(words)))

longest = words[0]
for w in words:
    if len(w) > len(longest): # > rather than >= so the first of any tied words is kept.
        longest = w
print("Longest:", longest)

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

most_common = words[0]
for w in counts:
    if counts[w] > counts[most_common]:
        most_common = w
print("Most common:", most_common, counts[most_common])

average = sum([len(w) for w in words]) / len(words)
print(f"Average length: {average:.2f}")

once = sorted([w for w in counts if counts[w] == 1])
print("Only once:", once)