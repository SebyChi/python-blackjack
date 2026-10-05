def deal_card(deck) :
  x = deck.pop()
  return deck, x

numbers = [10, 20, 30]
deck, x=deal_card(numbers)
print(deck, x)