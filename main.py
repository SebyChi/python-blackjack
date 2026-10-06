import random

def deck_create():
  deck = []
  ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
  suits = ("hearts", "diamonds", "clubs", "spades")
  for rank in ranks : 
    for suit in suits :
      card = (rank, suit)
      deck.append(card)

  return deck

def deck_shuffle():
  deck = deck_create()
  random.shuffle(deck)
  return deck

def deal_card(deck):
  return deck.pop()

def hand_calculator(hand):
  hand_value = 0
  ace_ct = 0
  for card in hand : 
    if card[0] in ("J", "Q", "K") : 
      hand_value += 10
    elif card[0] == "A" :
      hand_value += 11
      ace_ct += 1
    else : 
      hand_value += int(card[0])
  hand_value = ace_subtraction(hand_value, ace_ct)
  return hand_value

def ace_subtraction(hand_value, ace_ct):

  while hand_value > 21 and ace_ct > 0 :
    hand_value -= 10
    ace_ct -= 1
  return hand_value

def dealer_turn(dealer_hand, deck):
  while hand_calculator(dealer_hand) < 17 : 
    dealer_hand.append(deal_card(deck))
  return dealer_hand

def hit_stand_answer(player_hand):
  answer = input(f"Your score is {hand_calculator(player_hand)}. Do you want to hit or stand? \n").lower().strip()
  while answer not in ("hit", "stand"):
    print("Input invalid please type hit or stand.")
    answer = input("Do you want to hit or stand? \n").lower().strip()
  return answer

def hit_stand_loop(player_hand, deck):
  while hand_calculator(player_hand) < 21:
    answer = hit_stand_answer(player_hand)
    if answer == "stand":
      break
    player_hand.append(deal_card(deck))
  return player_hand

def determine_winner(player_hand, dealer_hand):
  player_score = hand_calculator(player_hand)
  dealer_score = hand_calculator(dealer_hand)
  if player_score > dealer_score: 
    print("Player won")
  elif dealer_score > player_score: 
    print("Dealer won")                                   
  else:
    print("Draw")

def game_setup():
  deck = deck_shuffle()
  player_hand = []
  dealer_hand = []
  player_hand.append(deal_card(deck))
  dealer_hand.append(deal_card(deck))
  player_hand.append(deal_card(deck))
  dealer_hand.append(deal_card(deck))
  return player_hand, dealer_hand, deck

def game_flow():  
  keep_playing = True
  while keep_playing :
    player_hand, dealer_hand, deck = game_setup()
    hit_stand_loop(player_hand, deck)
    if hand_calculator(player_hand) > 21:
      print("Player lost")
    else:
      dealer_turn(dealer_hand, deck)
      if hand_calculator(dealer_hand) > 21:
        print("Player won")
      else:
        determine_winner(player_hand, dealer_hand)
    break
      
game_flow()


