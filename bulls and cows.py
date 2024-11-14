author = """
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls&Cows

author: Martin Blahuš
email: martinkuf@gmail.com
"""


#knihovna pro praci s nahodnymi prvky
import random
#knihovna pro praci s casem
import time

#generuje nahodne cislo v rozmezi 1-9, tzn. bez 0
first_digit = random.choice('123456789')
#generuje zbyle tri cisla v rozmezi 0-9 bez duplicity 
remain_digits = ''.join(random.sample('0123456789'.replace(first_digit, ''), 3))

generate_number = first_digit + remain_digits

line = 47 * '-'

pozdrav = (f'''
Hi there!
{line}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{line}
''')

#kontrolni printy, pro zapnuti kontroly odmaz hashtag        
#print(f'i just generated number {generate_number}')

#uvod do hry a vyzadani cisel od uzivatele, ochrana pred spatnym zadanim
print(pozdrav)
start = time.time()
def enter_number():
    number = input('Enter a Number:')
    if number.isdigit() and len(number) == 4 and number[0] != '0' and len(set(number)) == 4:
        return number
    else:
        print('wrong number, insert four digit number, first number shouldnt be 0 and no duplicity')
        return enter_number()
    
user_number = enter_number()

#kontrolni printy, pro zapnuti kontroly odmaz hashtag        
#print(f'your choice is number {user_number}')

#pravidla hry
#bull - pokud uživatel uhodne cislo i umístění
#cow - pokud uživatel uhodne pouze číslo, ale ne jeho umístění
# nezapomenout na mnozne cisla podle delky prvku v listech

guess_bull = [] #list na pridavani tzv. bull cisel
guess_cow = [] #list na pridavani tzv. cow cisel
attempts = 0 #pocitani pokusu

#nekonecna smycka vyberu cisel ktera konci az pri splneni podminky, tj. uhadnuti vsech cisel
while len(guess_bull) < 4:
    attempts += 1
    guess_bull.clear()
    guess_cow.clear()
    for guess in range(4):
        # Kontrolujeme jednotlive cislice na stejnych pozicich
        if user_number[guess] == generate_number[guess] and user_number[guess] in generate_number:
            guess_bull.append(user_number[guess])
        # kontrolujeme zda se cislo nachazi v inputu
        elif user_number[guess] in generate_number:
            guess_cow.append(user_number[guess])
    if len(guess_bull) <= 1 and len(guess_cow) <= 1:
        print(f'{len(guess_bull)} bull ,{len(guess_cow)} cow')
    elif len(guess_bull) >= 2 and len(guess_cow) >= 2:
        print(f'{len(guess_bull)} bulls ,{len(guess_cow)} cows')
    elif len(guess_bull) <= 1 and len(guess_cow) >= 2:
        print(f'{len(guess_bull)} bull ,{len(guess_cow)} cows')
    elif len(guess_bull) >= 2 and len(guess_cow) <= 1:
        print(f'{len(guess_bull)} bulls ,{len(guess_cow)} cow')
        
    # kdyz uhodnes všechna cisla na spravnych pozicich
    if len(guess_bull) == 4:
        print('Congratulations! You guessed the number correctly!')
        break
    else:
        user_number = enter_number()
        
#ukonceni casovace, vypis casu a pokusu        
end = time.time()
time_needed = end - start
time_rounded = round(time_needed, 2)
print(f'You needed {attempts} attempts, which lasted {time_rounded} ')