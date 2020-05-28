#!/usr/bin/env python3
import random


def toss(money):
    """
    A player wins 1$ for every head and loses 1.5$ for every tail.
    The game is over when the player's balance reaches 0$
    """
    count = 0

    while money > 0:
        count += 1
        coin = random.choice(["Heads", "Tails"])

        if coin == "Heads":
            money += 1
        else:
            money -= 1.5

        if money > 0:
            choice = input(f"{coin}! You now have {money}$. Press N to get your money, Enter to keep trying")
        else:
            print(f"{coin}!, Wow you lost all your money! Better luck next time :(")

        if choice.lower() == "n":
            break

    return [money, count]


if __name__ == "__main__":
    money = float(input("How much money you are putting($): "))
    result = toss(money)
    print(f"You have started with {money}$ and ended up with {result[0]}$, you have tossed coin {result[1]} times.")
