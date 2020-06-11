from class_and_func import Card, Deck, Game, getMinRank

if __name__ == "__main__":
    def testGameDeck():
        test_game = Game()
        assert len(test_game.deck.cards) == 36 # Standard length of a Durak deck

    def test_getMinRank():
        card_array = []
        card_array.append(Card("Ace", "Spades"))
        card_array.append(Card(8, "Hearts"))
        card_array.append(Card(10, "Diamonds"))
        minim = getMinRank(card_array)
        assert minim.rank == 8 and minim.suit == "Hearts" # Since 8 < Others

    try:
        testGameDeck()
        test_getMinRank()
        print("Both tests passed")
    except:
        print("One or more tests failed")
