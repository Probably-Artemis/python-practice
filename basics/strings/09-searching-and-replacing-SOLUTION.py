"""
Objective: output how many times the letter "a" appears in sentence, then output the index where the word "cat" first appears, then output sentence with every "cat" replaced by "dog".
Restriction: you may not edit preexisting code.
"""

sentence = "a cat sat on a mat and another cat sat on a hat"

print(sentence.count("a"))
print(sentence.find("cat")) # find() returns -1 if it cannot find the desired substring.
print(sentence.replace("cat", "dog")) # like every string method, this makes a new string. sentence itself still has cats in it.