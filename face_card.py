from card import Card


""" This is an instance of one of, a jocker, a king or a queen
"""
class FaceCard(Card):
	def _points(self):
		return 10, 10
