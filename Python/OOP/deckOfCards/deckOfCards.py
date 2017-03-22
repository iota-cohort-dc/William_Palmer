import random
class Deck(object):
    def __init__(self):
        self.deck=[]


    def createDeck(self):
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        for val in values:
            for suit in suits:
                card = Card(val,suit)
                print card
                self.deck.append(card)

        print self.deck
        print ("end of deck")
        # return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        print self.deck
        # return self.deck
        print ("Deck has been shuffled")

        pass

    def dealCards(self):
        print ("You got: ")
        # for i in range(2):
        print(self.deck.pop(),self.deck.pop())
        cards=(self.deck.pop(),self.deck.pop())
        # return cards
        # pass

    def resetDeck(self):
        self.deck=[]
        print "is there a new deck???????"
        print self.deck
        print ("deck has been emptied and ready for new deck")
        self.createDeck()
        print ('new deck')
        print self.deck
        pass


class Card(object):
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "Card(Value %r, Suit %r)" % (self.value, self.suit)

deck1=Deck()

deck1.createDeck()

deck1.shuffle()

deck1.dealCards()

deck1.resetDeck()
