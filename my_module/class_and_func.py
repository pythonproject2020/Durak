# This code cell has the class and function declarations. It is the same
# code that is included in the modules section of the directory.

import random # Looked up on docs.python.org

class Card:
  """
  A Card object-> just has a rank and a suit
  """
  def __init__(self, rank = None, suit = None):
      self.rank = rank
      self.suit = suit
    
  def __repr__(self):
    """
    Allows the card to be printed out as "[Rank] of [Suit]"
    """
    return str(self.rank) + " of " + self.suit 

class Deck:
  """
  A Deck object-> represents a deck of cards. For durak, a 36-card deck is used
  in which cards 2 through 5 are excluded
  """
  def __init__(self):
      self.suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
      self.ranks = ["Ace", 6 , 7, 8, 9, 10, "Jack", "King", "Queen"]
      self.cards = []
      self._initialize_cards()

  def _initialize_cards(self):
    """
    Helper function for the constructor, just used to populate deck.cards
    """
    for suit in self.suits: # For each suit
        for rank in self.ranks: # Add one card per rank
            self.cards.append(Card(rank, suit))

  def shuffle(self):
    """
    Shuffles the deck
    """
    random.shuffle(self.cards)

class Game:
  """
  Represents all cards in play during a game.
  """
  def __init__(self):
      self.num_players = 2 # One human player, one AI
      self.deck = Deck() # Contains a deck
      self.hands = [[] for i in range(self.num_players)] # 1 hand per player
      self.deck.shuffle()
    
  def deal(self, num_cards = 6):
    """
    Deals 6 cards to each player to start off -> in Durak, each player is
    supposed to begin with 6 cards.
    """
    for player in range(self.num_players):
        for card in range(num_cards):
            self.hands[player].append(self.deck.cards[-1])
            self.deck.cards.pop() # Looked up list.pop() on Stack Overflow
  
def getMinRank(hand):
  """ 
  Gets the card with the minimum rank of a list of cards
  """
  ranks = {'Ace': 14, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack': 11, 'King':13,
                 'Queen':12}
  minRank = min(ranks[card.rank] for card in hand) # min() from docs.python.org
  minCard = None
  for card in hand:
    if ranks[card.rank] == minRank:
      minCard = card
  return minCard
