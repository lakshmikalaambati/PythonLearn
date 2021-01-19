import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
all_cards=[]
deal_cards=[]
count=0
for  suit in suits:
  for rank in ranks:
    all_cards.append(str(rank)+' of '+str(suit))
    count+=1

print(f'There are {len(all_cards)} cards in the deck')
print('Dealing ...')

while len(deal_cards) < 5:
    card = random.choice(all_cards)
    all_cards.remove(card)
    deal_cards.append(card)

print('Player has the following cards in their hand:')
print(deal_cards)