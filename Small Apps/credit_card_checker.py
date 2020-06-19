#!/usr/bin/env python3
"""
Program to check whether entered credit card number is valid and not and if so return its brand to user.
"""


def input_checker(number):
    numbers = "0123456789"
    for i in number:
        if i not in numbers:
            return True
    return False


def validity_checker(number):
    # needs refactoring
    result = []
    listo = [int(number[i]) * 2 for i in range(0, len(number), 2)]
    total = [str(i) for i in listo]
    for i in total:
        if len(i) > 1:
            for j in i:
                result.append(int(j))
        else:
            result.append(int(i))
    final = [int(number[i]) for i in range(1, len(number), 2)]

    if (sum(final) + sum(result)) != 20:
        return False
    else:
        return True


def brand_checker(number):
    card_brands = {"Master Card": ["51", "52", "53", "54", "55"],
                   "Visa": ["4"],
                   "American Express": ["34", "37"]}

    for card_brand, card_number in card_brands.items():
        if number[:2] in card_number or number[:1] in card_number:
            return card_brand
    return False


if __name__ == "__main__":
    user_choice = input("1-) Demo\n2-) Enter Credit Card Number\n>>")

    if user_choice == "1":
        cards = ["2223000048400011", "2223016768739313", "5555555555554444", "378282246310005",
                 "5105105105105100", "4111111111111111", "4012888888881881", "4222222222222",
                 "378734493671000", "371449635398431"]
        for i in cards:
            if len(i) < 13 or input_checker(i) or len(i) > 16:
                print("Check card length and make sure to input only as numbers")
            else:
                if validity_checker(i):
                    print(f"Card number: {i} is valid and its {brand_checker(i)}")
                else:
                    print(f"{i} card number is not valid")

    elif user_choice == "2":
        card_number = input("Enter your credit card number: ")  # 4003600000000014
        if len(card_number) < 13 or input_checker(card_number) or len(card_number) > 16:
            print("Entered Wrong Card Number")
        else:
            if validity_checker(card_number):
                print(f"Card number: {card_number} is valid and its {brand_checker(card_number)}")
            else:
                print("Card number is not valid")

    else:
        print("Wrong input")
