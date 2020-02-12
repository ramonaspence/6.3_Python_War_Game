import random

deck = list(range(1, 14)) * 4
# print(deck)

random.shuffle(deck)
print(deck)

player_one = deck[0:53:2]
print(player_one)

player_two = deck[0:53:2]
print(player_two)


#
# player_one_deck = (random.choice(deck))
# print(player_one_deck)

# player_one_deck = random.randint(range(0, 53))
