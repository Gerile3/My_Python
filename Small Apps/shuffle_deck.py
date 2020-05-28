#!/usr/bin/env python3
import random


class Card:
    def __init__(self):
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.suits = ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]

    def shuffle(self):
        cards = Card._build_deck(self)
        random.shuffle(cards)
        return cards

    def _build_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append(rank + " of " + suit)
        return deck

    def get_card(self, _random=True, num=1):
        deck = []
        if _random:
            if num == 1:
                rank = random.choice(self.ranks)
                suit = random.choice(self.suits)
                return rank + " of " + suit
            if num > 1:
                for i in range(num):
                    rank = random.choice(self.ranks)
                    suit = random.choice(self.suits)
                    deck.append(rank + " of " + suit)
                return deck
        else:
            if num == 1:
                return "Ace" + " of " + "Clubs (♣)"
            if num > 1:
                pass  # todo


if __name__ == "__main__":
    card = Card()
    shuffled_cards = card.shuffle()
    print("********\n", shuffled_cards)
    one_card = card.get_card()
    print("********\n", one_card)
    multi_card = card.get_card(num=10)
    print("********\n", multi_card)
