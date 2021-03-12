############################
#### Name: Yujia Xie    ####
#### Uniqname: yujiaxie ####
############################


import random
import unittest

############################
#### Name: Yujia Xie    ####
#### Uniqname: yujiaxie ####
############################

import random
import unittest

VERSION = 0.01
 
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
 

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)
 
    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"
 

class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self): 

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order
 
    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i) 
 
    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)
 
    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list
    
    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
 
    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards
    
    def deal(self, num_hand, num_card):
        '''Deal number of cards to each hand and return a list of hands

        Parameters
        ----------------
        num_hand: int
            the number of hand
        
        num_card: int
            the numebr of cards per hand
        
        Returns
        -------
        list
            the list of hands.
        '''
        result = []
        len_card = len(self.cards)
        num_card_avg = num_card
        remain = -1
        if num_card == -1:
            num_card_avg = len_card // num_hand
            remain = len_card - num_card_avg * num_hand
        for i in range(num_hand):
            result.append(Hand(self.deal_hand(num_card_avg)))
        if remain != -1:
            for i in range(remain):
                result[i].draw(self)
        return result


def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

# create the Hand with an initial set of cards
class Hand:
    '''a hand for playing card


    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
        a list of cards

    '''
    def __init__(self, init_cards):
        self.init_card = init_cards
    

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters
        ---------------
        card: instance
            a card to add
        
        Returns
        -------
        None

        '''
        card_str = []
        for c in self.init_card:
            card_str.append(c.__str__())
        if card.__str__() not in card_str:
            self.init_card.append(card)


    def remove_card(self, card):
        '''remove a card from the hand

        Parameters
        --------------
        card: instance
            a card to remove
        
        Returns
        -------
        the card, or None if teh card was not in the Hand

        '''
        card_str = []
        for c in self.init_card:
            card_str.append(c.__str__())
        if card.__str__() not in card_str:
            return None
        else:
            idx = card_str.index(card.__str__())
            return self.init_card.pop(idx)
    
    def draw(self, deck):
        '''draw a card
        draw a card from the deck and add it to the hand
        side effect: the dec will be depleted by one card

        Parameters
        ----------------
        deck: instance
            a deck from which to draw
        
        Returns
        -------
        None

        '''
        self.add_card(deck.deal_card())

    def remove_pairs(self):
        ''' looks for pairs of cards in a hand and removes them.
        Note: if there are three of a kind, only two should be removed

        Parameters
        ----------------
        None

        Returns
        -------
        None

        '''
        rank_list = [c.rank for c in self.init_card]
        len_card = len(rank_list)
        pairs = set()
        for i in range(len_card):
            for j in range(i+1, len_card):
                if rank_list[i] == rank_list[j]:
                    if (i not in pairs) and (j not in pairs):
                        pairs.add(i)
                        pairs.add(j)
                        break
        list_no_pairs = []
        for i in range(len_card):
            if i not in pairs:
                list_no_pairs.append(self.init_card[i])
        self.init_card = list_no_pairs


