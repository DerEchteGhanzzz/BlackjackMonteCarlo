import math
import random


class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __str__(self):
        return f"{[str(card) for card in self.cards]} : {max(self.get_value())}"

    def hit(self, card: Card):
        self.cards.append(card)

    def is_blackjack(self):
        return len(self.cards) == 2 and max(self.get_value()) == 21

    def get_value(self):
        values = [0]
        for card in self.cards:
            if card.value != 11:
                for i in range(len(values)):
                    values[i] += card.value
            else:
                values2 = [v for v in values]
                for i in range(len(values2)):
                    values2[i] += 1

                for i in range(len(values)):
                    values[i] += 11
                values.extend(values2)
        values = set(v for v in values if v <= 21)
        return values if values else [0]


def get_bid_mult(player_hand: Hand, dealer_hand: Hand):
    p = player_hand.get_value()
    d = dealer_hand.get_value()
    player_bj = player_hand.is_blackjack()
    dealer_bj = dealer_hand.is_blackjack()
    if player_bj:
        if dealer_bj:
            return 1
        return 2.5
    if dealer_bj:
        return 0
    if max(p) == 0:
        return 0
    if max(p) == max(d):
        return 1
    if max(p) > max(d):
        return 2
    return 0


def get_deck(amount=6):
    deck = amount * 4 * ([i for i in range(2, 10)] + [10, 10, 10, 10, 11])
    deck = [Card(i) for i in deck]
    random.shuffle(deck)
    return deck


def play_round(hand_amount, bid, strategy, debug=False):
    deck = get_deck()
    player = [Hand([]) for _ in range(hand_amount)]
    bids = [bid for _ in range(hand_amount)]
    for hand in player:
        hand.hit(deck.pop())
    for hand in player:
        hand.hit(deck.pop())
    dealer = Hand([deck.pop()])
    player_target = strategy[0] if max(dealer.get_value()) < 7 else strategy[1]
    for hand in player:
        while 0 < max(hand.get_value()) < player_target:
            hand.hit(deck.pop())
    while 0 < max(dealer.get_value()) < 17:
        dealer.hit(deck.pop())
    for idx, hand in enumerate(player):
        bids[idx] *= get_bid_mult(hand, dealer)
    if debug:
        [print(hand) for hand in player]
        print("DEALER")
        print(dealer)
        print("\n")
    return bids


def simulate(rounds, hand_amount, bid, strategy):
    cash = 0
    for _ in range(rounds):
        cash -= hand_amount * bid
        cash += sum(play_round(hand_amount, bid, strategy, False))
    # print(f"{cash} kr")
    return cash


if __name__ == '__main__':
    winning_strategy = []
    for low in range(2, 22):
        for high in range(2, 22):
            winnings = []
            for _ in range(10):
                winnings.append(simulate(1000, 1, 1, (low, high)))
            # print(sum(winnings) / len(winnings))
            # print(sum(winnings))
            print(low, high)
            winning_strategy.append((sum(winnings), (low, high)))
    winning_strategy.sort(key=lambda x: x[0], reverse=True)
    [print(ws) for ws in winning_strategy]
    print("QED")
