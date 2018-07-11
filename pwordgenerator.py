import random
import string

user=int(input('Enter 1 for Weak ,2 for strong Password:'))

def strong():

    special=['*',',','.','@','!','?','_','-']
    alphabetl=list(string.ascii_lowercase)
    alphabetH=list(string.ascii_uppercase)
    pword=random.sample(range(10), 4)
    pword=''.join(map(str,pword))
    pword2=pword+random.choice(special)
    pword3=pword2+random.choice(alphabetl)
    pword3=pword3+random.choice(alphabetl)
    pword3=pword3+random.choice(alphabetl)
    pword3=pword3+random.choice(alphabetl)
    pword4=pword3+random.choice(alphabetH)
        
    return pword4

def weak():

    pword=['123456789','0987654321','1357911','0246810']
    choice=random.choice(pword)
    return choice

if user == 2:
    print('Password=',strong())
elif user == 1:
    print('Password=',weak())
