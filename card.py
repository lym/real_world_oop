""" Generic card class
"""
class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank
		self.hard, self.soft = self._points()
