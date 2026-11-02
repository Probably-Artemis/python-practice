"""
Objective: output a shuffled copy of deck, then output deck to prove it is unchanged. Then deal a hand of five random cards from deck, with no card appearing twice, and output it.
Restriction: you may not edit preexisting code.
"""

# all 52 cards, like "AS" for the ace of spades. this uses a nested comprehension, covered in comprehensions/05.
deck = [rank + suit for suit in "SHDC" for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

import random

shuffled = deck.copy()
random.shuffle(shuffled) # shuffle() changes the list in place and returns None, which is why we shuffle a copy.

print(shuffled)
print(deck)

hand = random.sample(deck, 5) # sample() picks items without repeats, and leaves the original list alone.

print(hand)