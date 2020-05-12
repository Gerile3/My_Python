def factors(num):
    '''Find the factors of an integer v.0.1'''
    return [i for i in range(1, num + 1) if num % i == 0]


if __name__ == '__main__':
    num = int(input('Your Number Please: '))
    if num > 0:
        print("Factors of {}: {}".format(num, factors(num)))
    else:
        print('Please enter a positive integer')
