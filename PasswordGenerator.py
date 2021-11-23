#Start
import string
import random
import sys
import os
#Library
    #string
hvl_ww = 'Hoeveel wachtwoorden wilt u maken? - '
hvl_kk = 'Hoeveel karakters wilt u in uw wachtwoord(en) - '
#Functies
def invalid_reactie():
    print('U heeft een fout antwoord ingevult')

def lengte_bepaling(bericht):
    print(bericht,end='')
    lengte = int(input())
    return lengte
#Complexiteit samenstellen
while True:
    print('#' * 80 + '\n')
    nummer = lengte_bepaling(hvl_ww)
    lengte_wachtwoord = lengte_bepaling(hvl_kk)

    complexiteit = ''
    choice = input('\nWil je de interne library met karakters gebruiken?\n(Alternatief is zelf karakters intypen) ja/nee - ')

    if choice == 'ja':
        print('\nLoading Libraries...')
        antwoord = input('\nWil je kleine letters gebruiken? ja/nee - ')
        if antwoord == 'ja':
            complexiteit += string.ascii_lowercase
        else:
            print('')
        antwoord = input('Wil je hoofdletters gebruiken? ja/nee - ')
        if antwoord == 'ja':
            complexiteit += string.ascii_uppercase
        antwoord = input('Wil je nummers gebruiken? ja/nee - ')
        if antwoord == 'ja':
            complexiteit += string.digits
        antwoord = input('Wil je speciale karakters gebruiken? ja/nee - ')
        if antwoord == 'ja':
            complexiteit += string.punctuation
    else:
        antwoord = input('\nVul hier je eigen karakters in: ')
        complexiteit = antwoord

    #Passwords worden hier gegenereerd
    for p in range(nummer):
        password = ''
        for c in range(lengte_wachtwoord):
            password += random.choice(complexiteit)
        print('\n' + password)
    print('\n' + '#' * 80 + '\n')
#End
