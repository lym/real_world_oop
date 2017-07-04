""" Generic card class
A card belongs to a suit.
A card has rank i.e; its value when the hand total is being computed
"""
class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank
		self.hard, self.soft = self._points()
