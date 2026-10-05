import random

def deck_create() :
  deck = []
  ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
  suits = ("hearts", "diamonds", "clubs", "spades")
  for rank in ranks : 
    for suit in suits :
      card = (rank, suit)
      deck.append(card)

  return deck

def deck_shuffle() :
  deck = deck_create()
  random.shuffle(deck)
  return deck

def deal_card(deck) :
  return deck.pop()

deck = deck_shuffle()
player_hand = []
dealer_hand = []
player_hand.append(deal_card(deck))
dealer_hand.append(deal_card(deck))
player_hand.append(deal_card(deck))
dealer_hand.append(deal_card(deck))
print(player_hand, dealer_hand, len(deck))
