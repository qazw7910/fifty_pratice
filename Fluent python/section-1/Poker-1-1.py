import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamond=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    # beer_card = Card('7', 'diamond')
    # print(beer_card)
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[-1])
    # print(deck._cards)
    # print(choice(deck._cards))
    # for card in reversed(deck):
    #     print(card)
    # print(Card('Q', 'diamond') in deck)
    for card in sorted(deck, key=spades_high):
        print(card)