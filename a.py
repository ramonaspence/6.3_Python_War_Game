import random

def createdeck():
    deck = list(range(1, 14)) * 4
    random.shuffle(deck)

    return deck

def main():
    deck = createdeck()

    player_one = deck[0:52:2]
    player_two = deck[1:52:2]

    playeronelen = len(player_one)
    playertwolen = len(player_two)
    while (playeronelen > 0) or (playertwolen > 0):
        # try:
        random_card = random.randint(1, 5)
        card_one = player_one.pop(random_card)
        print(card_one)
        card_two = player_two.pop(random_card)
        print(card_two)
        dealt = [card_one, card_two]
        if card_one > card_two:
            # print(len(player_one),player_one)
            player_one.insert(-1, card_one)
            player_one.insert(-1, card_two)
            print('Player1 Takes the Cards',len(player_one),player_one)

        elif card_two > card_one:
            # print(len(player_two), player_two)
            player_two.insert(-1, card_one)
            player_two.insert(-1, card_two)
            print('Player2 Takes the Cards',len(player_two), player_two)

        elif card_two == card_one:
            hand_one = player_one[0:3]
            hand_two = player_two[0:3]
            if hand_one[2] > hand_two[2]:
                hand = hand_one + hand_two
                player_one.extend(hand)
            else:
                hand = hand_one + hand_two
                player_two.extend(hand)

        # except:
        #     print("ran out of cards!")
        #     break

    if len(player_one) >= 52 or len(player_two) >= 52:
        print('Player 2 Won!', len(player_two))
    else:
        print('Player 1 Won!', len(player_one))


main()
