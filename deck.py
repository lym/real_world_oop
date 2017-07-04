import random

from ace_card import AceCard
from face_card import FaceCard
from number_card import NumberCard
from suit import Clubs, Diamonds, Hearts, Spades

class Deck(object):
    """ This class is an abstraction of a deck of cards.
    """
    def __init__(self):
        self.aces = [
            AceCard(1, Clubs),
            AceCard(1, Diamonds),
            AceCard(1, Hearts),
            AceCard(1, Spades)
        ]
        self.number_cards   = self._gen_numbered_cards()
        self.face_cards     = self._gen_face_cards()
        self.cards          = self.aces + self.number_cards + self.face_cards

    def _gen_numbered_cards(self):
        cards = []
        for suit in [Clubs, Diamonds, Hearts, Spades]:
            for num in range(2, 11):
                cards.append(NumberCard(num, suit))
        return cards

    def _gen_face_cards(self):
        cards = []
        for suit in [Clubs, Diamonds, Hearts, Spades]:
            for face in ['Jack', 'Queen', 'King']:
                cards.append(FaceCard(10, suit))
        return cards

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append({card.rank: card.suit.symbol})
        return str(cards)

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards


if __name__ == '__main__':
    deck = Deck()
    print('Number of cards in deck is: {}'.format(
        len(deck.cards)
    ))
    print('Initial deck:\n {}'.format(deck))
    deck.shuffle()
    print('After shufflin:\n {}'.format(deck))
    # deck.shuffle()
