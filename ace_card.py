from card import Card


""" Represents any of the four aces: spades, diamonds, hearts or flowers
"""
class AceCard(Card):
	def _points(self):
		return 1, 11

