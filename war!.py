#card 
  #suit,rank,ValueError
import random
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,   'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 

class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = value[rank]

  def __str__(self):
    return self.rank +" of " + self.suit


class Deck():

  def __init__(self):
    self.all_cards = []

    for suit in suits:
      for rank in ranks:
        created_card = Card(suit,rank)
        self.all_cards.append(created_card)

  def shuffle(self):
      random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()
    

class Player:

  def __init__(self, name):
    self.name = name
    self.all_cards = []

  def remove_one(self):
    return self.all_cards.pop(0)
  
  def add_cards(self, new_cards):
    if type(new_cards) is list:
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)

  def __str__(self):
    return f"{self.name} has {len(self.all_cards)} cards"

#Game Setup
player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()  

for x in range(26):
  player_one.add_cards(new_deck.deal_one())
  player_two.add_cards(new_deck.deal_one())




#start round
game_on = True
round = 0
while game_on == True:
  if len(player_one.all_cards) ==0:
    print ("player one is out of cards! they lose!")
    print ("player two wins!")
    
    break
  if len(player_two.all_cards) ==0:
    print ("player two is out of cards! they lose!")
    print ("player one wins!")
    break
  
  round += 1
  print (f"it's round {round}")

  player_one_card = []
  player_two_card = []

  player_one_card.append(player_one.remove_one())
  player_two_card.append(player_two.remove_one())

  if player_one_card[-1].value > player_two_card[-1].value:
    player_one.add_cards(player_one_card)
    player_one.add_cards(player_two_card)
    print(f"{player_one_card[-1].suit}{player_one_card[-1].rank} and {player_two_card[-1].suit}{player_two_card[-1].rank}were added to player one's deck")
    print (len(player_one.all_cards))

  elif player_one_card[-1].value < player_two_card[-1].value:
    player_two.add_cards(player_one_card)
    player_two.add_cards(player_two_card)
    print(f"{player_one_card[-1].suit}{player_one_card[-1].rank} and {player_two_card[-1].suit}{player_two_card[-1].rank}were added to player two's deck")
    print (len(player_two.all_cards))


  else:
    print ("IT'S WAR!")
    war = True
    while war == True:
      if len(player_one.all_cards) < 5:
        print ("player one cannot war, they lose!")
        print ("player two wins")
        game_on = False
        break
      elif len(player_two.all_cards) < 5:
        print ("player two cannot war, they lose!")
        print ("player one wins")
        game_on= False
        break
        
      for x in range(5):
        player_one_card.append(player_one.remove_one())
        player_two_card.append(player_two.remove_one())
 
      if player_one_card[-1].value > player_two_card[-1].value:
        player_one.add_cards(player_one_card)
        player_one.add_cards(player_two_card)
        war = False

      elif player_one_card[-1].value < player_two_card[-1].value:
        player_two.add_cards(player_one_card)
        player_two.add_cards(player_two_card)
        war = False

      else:
        pass
