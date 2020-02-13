import random

deck = list(range(1, 14)) * 4
# print(deck)

random.shuffle(deck)
# print(deck)

player_one = deck[0:53:2]
print(player_one)

player_two = deck[1:53:2]
print(player_two)


while len(player_one) > 0 and len(player_two) > 0:
    card_one = player_one.pop()
    print(card_one)
    card_two = player_two.pop()
    print(card_two)
    if card_one > card_two:
        print('Player1 Takes the Cards')
        player_one.insert(0, card_one)
        player_one.insert(0, card_two)
        print(len(player_one))
    elif card_one < card_two:
        print('Player2 Takes the Cards')
        player_two.insert(0, card_one)
        player_two.insert(0, card_two)
        print(len(player_two))
    elif card_one == card_two:
        print('Tie! Draw Three!')
        card_one = player_one.pop()
        card_two = player_two.pop()
        print(card_one)
        print(card_two)
else:
    if len(player_one) == 0 or len(player_two) == 0:
        print('game over')
#
# else:
#     if len(player_one) == 0:
#         print('Player 1 Wins!')
#     elif len(player_two) == 0:
#         print('Player 2 Wins!')
