############################
#### Name: Yujia Xie    ####
#### Uniqname: yujiaxie ####
############################


import unittest
import hw5_cards_ec1



class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards_ec1.Card(0, 2)
        c2 = hw5_cards_ec1.Card(1, 1)
        init_list = [c1, c2]
        hand1 = hw5_cards_ec1.Hand(init_list)

        self.assertEqual(hand1.init_card, init_list)
        self.assertIsInstance(hand1.init_card[0], hw5_cards_ec1.Card)
    
    def testAddAndRemove(self):
        c1 = hw5_cards_ec1.Card(0, 2)
        c2 = hw5_cards_ec1.Card(1, 1)
        init_list = [c1, c2]
        hand1 = hw5_cards_ec1.Hand(init_list)

        #c2 should not be added to the hand
        #c2 is already in the hand
        len_before = len(hand1.init_card)
        hand1.add_card(c2)
        len_after = len(hand1.init_card)
        self.assertEqual(len_after, len_before)

        #c3 should be added successfullt
        c3 = hw5_cards_ec1.Card(suit=1, rank=7)
        len_before = len(hand1.init_card)
        hand1.add_card(c3)
        len_after = len(hand1.init_card)
        self.assertEqual(len_after, len_before+1)

        #remove one card
        #remove c3
        self.assertEqual(c3, hand1.remove_card(c3))

        #cannot remove c3, c3 is not in the hand
        self.assertEqual(None, hand1.remove_card(c3))

    
    def testDraw(self):
        deck1 = hw5_cards_ec1.Deck()
        deck1.shuffle()
        len_deck_before = len(deck1.cards)
        hand1 = hw5_cards_ec1.Hand([])
        len_hand_before = len(hand1.init_card)
        hand1.draw(deck1)
        len_dec_after = len(deck1.cards)
        len_hand_after = len(hand1.init_card)
        self.assertEqual(len_hand_before+1, len_hand_after)
        self.assertEqual(len_dec_after, len_deck_before-1)


if __name__=="__main__":
    unittest.main()
    