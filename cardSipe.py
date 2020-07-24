import random

class Card():
    '''
    Represents a standard playing card
    rank: 1 - 13; Ace->1, Jack->11, Queen->12, King->13
    suit: 0->clubs, 1->diamonds, 2->hearts, 3->spades
    '''
    #rank and suit are class variables: consistent in all instances
    suit_names = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    rank_names = (None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, suit = 0, rank = 2):
        assert 0 <= suit < 4 and 0 < rank <= 13, 'rank or suit out of range'
        self.suit = suit
        self.rank = rank

    def __str__(self):
        #rank_names and suit_names are Card variables while self is the specific instance
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        #tuple comparison for elegant code
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __eq__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 == t2


class Deck():
    '''
    a deck comprises of 52 cards(jokers excluded)
    '''
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        listCards = [str(card) for card in self.cards]
        return '\n'.join(listCards)  

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for _ in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_of_hands, cards_per_hand):
        handList = []
        for _ in range(num_of_hands):
            self.shuffle()
            hand = Hand()
            self.move_cards(hand, cards_per_hand)
            handList.append(hand)
        return handList


class Hand(Deck):
    '''
    Represents a hand of playing cards.
    '''

    def __init__(self, label = ''):
        self.cards = []
        self.label = label


sipe = Deck()
spencer = Hand()
sipe.move_cards(spencer, 4)
print(spencer)