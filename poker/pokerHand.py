from Card import Hand, Deck

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        '''
        pair: 2 cards with same rank
        '''
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twoPairs(self):
        counter = 0
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                counter += 1
        return counter > 1

    def has_threeOfaKind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        vals = [card.rank for card in self.cards]
        vals.sort()
        for i in range(1, len(vals)):
            if vals[i - 1] + 1 != vals[i]:
                return False
        return True

    def has_fullHouse(self):
        return self.has_threeOfaKind() and self.has_twoPairs()

    def has_fourOfaKind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straightFlush(self):
        return self.has_flush() and self.has_straight()

    def classify(self):
        if self.has_straightFlush():
            self.label = 'straight flush'
        elif self.has_fourOfaKind():
            self.label = 'four of a kind'
        elif self.has_fullHouse():
            self.label = 'full house'
        elif self.has_flush():
            self.label = 'flush'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_threeOfaKind():
            self.label = 'three of a kind'
        elif self.has_twoPairs():
            self.label = 'two pairs'
        elif self.has_pair():
            self.label = 'pair'


def get_classDict():
    deck = Deck()
    deck.shuffle()
    handList = []
    for _ in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        handList.append(hand)

    classDict = {}
    for hand in handList:
        hand.classify()
        classDict[hand.label] = classDict.get(hand.label, 0) + 1
    return classDict

def drawTable(f, num):
    newDict = {}
    for _ in range(num):
        searchList = f()
        for key in searchList:
            newDict[key] = newDict.get(key, 0) + 1
    denom = sum(list(newDict.values()))
    for keys in newDict.keys():
        print(keys, '-', end = " ")
        print(newDict[keys]/(denom * 7))



if __name__ == '__main__':
    '''
    # make a deck
    deck = Deck()
    deck.shuffle()
    
    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        print(hand.label)
        print(hand)
        print('')
    '''
    drawTable(get_classDict, 10000)