############################
#### Name: Yujia Xie    ####
#### Uniqname: yujiaxie ####
############################


import unittest
import hw5_cards_ec2



class TestCard(unittest.TestCase):

    def testremovePairs(self):
        c1 = hw5_cards_ec2.Card(suit=0, rank=2)
        c2 = hw5_cards_ec2.Card(suit=1, rank=2)
        init_list = [c1, c2]
        #2, 2
        hand1 = hw5_cards_ec2.Hand(init_list)
        hand1.remove_pairs()
        self.assertEqual(len(hand1.init_card), 0)

        c3 = hw5_cards_ec2.Card(suit=2, rank=2)
        init_list = [c1, c2, c3]
        #2, 2, 2
        hand2 = hw5_cards_ec2.Hand(init_list)
        hand2.remove_pairs()
        self.assertEqual(len(hand2.init_card), 1)

        c4 = hw5_cards_ec2.Card(suit=3, rank=2)
        c5 = hw5_cards_ec2.Card(suit=3, rank=5)
        c6 = hw5_cards_ec2.Card(suit=1, rank=5)
        c7 = hw5_cards_ec2.Card(suit=2, rank=5)
        init_list = [c1, c2, c3, c4, c5, c6, c7]
        # 2, 2, 2, 2, 5, 5, 5
        hand2 = hw5_cards_ec2.Hand(init_list)
        hand2.remove_pairs()
        self.assertEqual(len(hand2.init_card), 1)
    
    def testDeal(self):
        a_deck = hw5_cards_ec2.Deck()
        num_hand = 3
        num_card = -1
        three_hands = a_deck.deal(num_card=num_card, num_hand=num_hand)

        self.assertEqual(len(a_deck.cards), 0)
        self.assertEqual(len(three_hands[0].init_card), 18)
        self.assertEqual(len(three_hands[1].init_card), 17)

        a_deck = hw5_cards_ec2.Deck()
        num_hand = 3
        num_card = 7
        three_hands = a_deck.deal(num_card=num_card, num_hand=num_hand)
        self.assertEqual(len(a_deck.cards), 31)
        self.assertEqual(len(three_hands[0].init_card), 7)
        self.assertEqual(len(three_hands[1].init_card), 7)
        self.assertEqual(len(three_hands[2].init_card), 7)

if __name__=="__main__":
    unittest.main()
    
