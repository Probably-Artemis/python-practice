"""
Objective: output a shuffled copy of deck, then output deck to prove it is unchanged. Then deal a hand of five random cards from deck, with no card appearing twice, and output it.
Restriction: you may not edit preexisting code.
"""

# all 52 cards, like "AS" for the ace of spades. this uses a nested comprehension, covered in comprehensions/05.
deck = [rank + suit for suit in "SHDC" for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]