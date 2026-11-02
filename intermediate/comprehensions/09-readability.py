"""
Objective: the comprehension below works, but it is hard to read. Below it, write regular loops that build the same list, then output both lists to prove they match.
Restriction: you may not edit preexisting code.
"""

sentence = "the quick brown fox jumps over 2 lazy dogs and 3 cats"

result = [w.upper() if len(w) > 3 else w for w in sentence.split() if w.isalpha() if w[0] not in "aeiou"]