from .class_and_func import Card, Deck, Game, getMinRank
def durak():
  """
  Main Game
  """

  # The following block initializes the beginning state of the game:
  # 1.) Deals cards
  # 2.) Selects Trump Card
  # 3.) No current card is in middle yet, so cards on the table is also empty
  my_durak = Game()
  my_durak.deal()
  trump_suit = my_durak.deck.cards.pop().suit 
  print("Trump Suit:", trump_suit, "\n")
  ranks = {'Ace': 14, 6:6, 7:7, 8:8, 9:9, 10:10, 'Jack': 11, 'King':13,
                 'Queen':12}
  turn = 0 # 0 represents player turn, 1 represents AI turn
  current_card = None 
  cards_on_table = []
  game_running = True
  check = False # When one player has gotten rid of all their cards

  # The following is the main algorithm of the game
  while game_running == True:
    if current_card == None:
      print("No cards in middle yet: place first card\n")

    if turn == 0: # If is player's turn

      # The following block creates a list of cards that would beat the 
      # current card in play.
      # 1.) If no card has been played yet, any card in the hand will work.
      # 2.) If the card in the middle is not a trump, it can be beaten by
      #     a card of the same suit with a higher rank or by any trump.
      # 3.) If the card in the middle is a trump, it can only be beaten by 
      #     another trump of a higher rank.
      valid_choices = []
      for card in my_durak.hands[0]: 
        current_trump = (current_card != None and 
                         current_card.suit == trump_suit)
        outrank = (current_card != None and 
                   ranks[card.rank] > ranks[current_card.rank] 
                   and card.suit == current_card.suit)
        if (current_card == None or (current_trump and outrank) or 
            ((not current_trump) and (card.suit == trump_suit or outrank))):
          valid_choices.append(card)

      print("\nThis is your current hand: ", my_durak.hands[0])

      if len(valid_choices) > 0: # If some cards would win
        print('The following cards would beat the current card:')

        for index in range(len(valid_choices)):
          print("Enter", index, "to select", valid_choices[index])
        print("OR enter -1 to PASS and Collect Middle")

        selection_index = int(input("\n"))

        # The following while loop makes sure the player entered a valid card
        while selection_index > len(valid_choices)-1 or selection_index < -1:
          selection_index = int(input("Please enter a valid choice\n"))

        # If player chooses not to play a winning card
        if selection_index == -1:
          if check == True: # If AI has no more cards
            game_running = False

          input('\nYou PASSED-> PRESS ENTER to Collect Middle\n')

          # Collects middle, except for Trump cards which are discarded
          my_durak.hands[0].extend([card for card in cards_on_table 
                                   if card.suit != trump_suit])
          cards_on_table = []
          current_card = None
        
        # If the player picked a card to play
        else:
          if check == True: # If the AI has 0 cards
            check = False # Since the AI will have to collect the middle cards

          selected = valid_choices[selection_index]
          cards_on_table.append(selected)
          my_durak.hands[0].remove(selected)
          current_card = cards_on_table[-1]

          if len(my_durak.hands[0]) == 0: # If this card was player's last
            check = True # AI has to beat it next turn or game is over

      else: # If no cards would win, player collects middle cards
        if check == True:
          game_running = False

        input("\nNone of your cards can win-> PRESS ENTER to Collect Middle\n")
        my_durak.hands[0].extend([card for card in cards_on_table 
                                 if card.suit != trump_suit])
        cards_on_table = []
        current_card = None
      turn = 1

    elif turn == 1: #if AI turn

      trump_choices = [] # Trump cards the AI has that would beat current card
      non_trumps = [] # Non-trump cards that would beat the current card

      # The following determines which cards are valid options in the same way
      # that was done for the player, except this time it separates the choices
      # based on whether they are trump cards or not.
      for card in my_durak.hands[1]:
        current_trump = (current_card != None and 
                         current_card.suit == trump_suit)
        outrank = (current_card != None and 
                   ranks[card.rank] > ranks[current_card.rank] 
                   and card.suit == current_card.suit)
        if (current_card == None or (current_trump and outrank) or 
            ((not current_trump) and (card.suit == trump_suit or outrank))):
          if card.suit == trump_suit:
            trump_choices.append(card)
          else:
            non_trumps.append(card)

      # If no cards would win
      if len(trump_choices) == 0 and len(non_trumps) == 0:
        if check == True: # If player has no cards, game over
          game_running = False

        print('\nAI has no winning cards: it collects the cards in middle\n')
        my_durak.hands[1].extend([card for card in cards_on_table 
                                  if card.suit != trump_suit])
        cards_on_table = []
        current_card = None


      # If possible, the AI would prefer to play a non-trump instead of a Trump,
      # and it would prefer to play the card with the lowest rank that can beat
      # the current card
      elif len(non_trumps) > 0:  
        if check == True:
          check = False

        best_choice = getMinRank(non_trumps)
        print("\nThe AI has played:\n", best_choice)
        cards_on_table.append(best_choice)
        my_durak.hands[1].remove(best_choice)
        current_card = cards_on_table[-1]
      
        if len(my_durak.hands[1]) == 0:
          check = True

      # If only a Trump can win, the AI chooses to play the trump with the
      # lowest rank that can beat the current card
      else:
        if check == True:
          check = False

        best_choice = getMinRank(trump_choices)
        print("The AI has played:\n", best_choice)
        cards_on_table.append(best_choice)
        my_durak.hands[1].remove(best_choice)
        current_card = cards_on_table[-1]
        
        if len(my_durak.hands[1]) == 0:
          check = True
      turn = 0

  # If player managed to get rid of all their cards
  if len(my_durak.hands[0]) == 0:
    print("The player wins. The AI is the durak")
  
  # If the AI managed to get rid of all their cards
  elif len(my_durak.hands[1]) == 0:
    print("The AI wins. The player is the durak")
