from card import Card


""" Represents a card with a number on it. e.g a 4 of hearts
"""
class NumberCard(Card):
	def _points(self):
		return int(self.rank), int(self.rank)
