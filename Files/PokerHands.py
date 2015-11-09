# C. Haught and Math 215 class
# Poker hand examples for Oct 8, 2015

from deck import *

from deck import *
def is_flush(ahand):
    '''Return True exactly when ahand is a list of 5 cards
    and these cards represent a flush'''
    suits = []
    for c in ahand:
        suits.append(c.getSuit())
    if suits.count(suits[0])== 5:
        return True
    else:
        return False


def is_straight(ahand):
    '''Return True exactly when ahand is a list of 5 cards
    and these cards represent a straight'''
    ahand.sort()
    q = min(ahand).getRank()
    if ahand[0].getRank() + 1 == ahand[1].getRank() and ahand[1].getRank() + 1 == ahand[2].getRank():
        return True
    return False
    

def is_4_of_a_kind(ahand):
    '''Return True exactly when ahand is a list of 5 cards
    and these cards represent four of a kind'''
    ranks = []
    for card in ahand:
        ranks.append(card.getRank())
        
    for rank in ranks:
        if ranks.count(rank) == 4:
            return True
    return False
        

def is_3_of_a_kind(ahand):
    rankings = []
    for card in ahand:
        rank = card.rank
        rankings.append(rank)
    counts = []
    for x in range(len(rankings)):
        num = rankings[x]
        t = rankings.count(num)
        counts.append(t)
    if 3 in counts and 2 not in counts:
        print('3 of a kind')
        return True
    else:
        return False


def is_full_house(ahand):
    ranks = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
    for key in ranks:
        for card in ahand:
            if card == Card(key, "spade") or card == Card(key, "heart") or card == Card(key, "diamond") or card == Card(key, "club"):
                ranks[key] += 1
    isFullHouse = False
    for rank1 in ranks:
        if ranks[rank1] == 3:
            for rank2 in ranks:
                if ranks[rank2] == 2:
                    isFullHouse = True

    return isFullHouse
    '''Return True exactly when the ahand is a list of 5 cards
    and these cards represent a full house'''

def is_2_pair(ahand):
    ahand.sort()
    if ahand[0].getRank() == ahand[1].getRank():
        if ahand[2].getRank() == ahand[3].getRank():
            if ahand[1].getRank() != ahand[2].getRank():
                return True
            else:
                return False
        elif ahand[3].getRank() == ahand[4].getRank():
            if ahand[1].getRank() != ahand[3].getRank():
                return True
            else:
                return False
    elif ahand[1].getRank() == ahand[2].getRank():
        if ahand[3].getRank == ahand[4].getRank():
            if ahand[2].getRank() != ahand[3].getRank():
                return True
            else:
                return False
    else:
        return False

def is_1_pair(ahand):
    '''Return True exactly when the ahand is a list of 5 cards
    and these cards represent exactly one pair
    (no better result appears)'''
    pass


def is_straight_flush(ahand):
    '''Return True exactly when the ahand is a list of 5 cards
    and these cards represent a straight flush'''
    pass

def is_royal_flush(ahand):
    '''Return True exactly when the ahand is a list of 5 cards
    and these cards represent a royal flush'''
    pass

def testHand(ahand):
    for c in ahand:
        print(c)
    print("is_straight(hand)", is_straight(ahand))
    print("is_flush(hand)", is_flush(ahand))
    print("is_3_of_a_kind(hand)", is_3_of_a_kind(ahand))
    print("is_4_of_a_kind(hand)", is_4_of_a_kind(ahand))
    print("is_full_house(hand)", is_full_house(ahand))
    print("is_2_pair(hand)", is_2_pair(ahand))
    print("is_1_pair(hand)", is_1_pair(ahand))
    print("is_straight_flush(hand)", is_straight_flush(ahand))
    print("is_royal_flush(hand)", is_royal_flush(ahand))

def getHand():
    print("Press r for a random hand, u for a user-specified hand")
    response = input()
    my_hand = []
    if response.lower()=='r':
        myDeck = Deck()
        myDeck.shuffle()
        my_hand = [myDeck.draw() for k in range(5)]
    else:
        for k in range(5):
            r = int(input("Type the rank - an integer 1..13: "))
            s = input("Type the suit - heart, diamond, club, spade: ")
            suits = {'h':'heart', 'd':'diamond', 'c':'club', 's':'spade'}
            my_hand.append(Card(r, suits.get(s[0])))
    return my_hand
        
    
def main():  #Testing Code
    response = 'y'
    while response != 'n':
        h = getHand()
        testHand(h)
        response = input("Test another hand? Type y for yes, n for no: ").lower()    
                           
    

main()
            
    
