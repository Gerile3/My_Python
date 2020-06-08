#!/usr/bin/env python3
'''
Unit converter: Miles and Kilometers and bunch of others
'''


def print_menu():
    print("1. Kilometers to Miles\n2. Miles to Kilometers\n3. Feet to Inch and Cm\n4. Feet to miles,yard,inch",
          "\n5. Celcius to Kelvin and Fahrenheit\n6. Pascal to Mmhg and Atm and Kpa")


def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))


def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))


def inchtocm():
    # feet = 12 inch
    # 1 inch = 2.54 cm

    result = float(input("Enter Feet: "))

    print("{} feet equals to {} inch and {} cm".format(result, result * 12, result * 12 * 2.54))


def feettoinch():
    # feet = 0.333 yard
    # feet = 0.0001893939 miles
    # feet = 12 inch

    result = float(input("Enter in feet: "))
    print("{} feets equals to {} yard, {} miles, {} inches".format(result, result * 0.333, result * 0.0001893939, result * 12))


def ctofk():
    t = float(input("Enter temperature: "))
    f = (t / 5) * 9 + 32
    k = t + 273.15

    print("{} *C equals {} F and {} Kelvin".format(t, f, k))


def pascalto():
    # 1 kPa = 0.145 psi
    kpa = float(input("Enter kilopascal: "))
    psi = kpa * 0.14504
    mmHg = kpa * 7.50062
    atm = kpa * 0.00987

    print("{} kpa equals {:.2f} psi, {:.2f} mmHg, {:.2f} atm".format(kpa, psi, mmHg, atm))


if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do? (q to quit): ')
    if choice == '1':
        km_miles()
    elif choice == '2':
        miles_km()
    elif choice == '3':
        inchtocm()
    elif choice == '4':
        feettoinch()
    elif choice == '5':
        ctofk()
    elif choice == '6':
        pascalto()
    elif choice.lower() == "q":
        exit(1)
    else:
        print("Wrong input")
