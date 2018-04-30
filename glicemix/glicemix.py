#!/usr/bin/env python
''' glicemix.py
    The starting point
'''
def mainMenu():
    ''' Show the main menu and ask for a choice
        @return choice
    '''
    print(' === Benvenuto in Glicemix ===\n')
    print('[1] Visualizza dati')
    print('[2] Importa dati')
    print('[3] Esporta dati')
    print('[4] Impostazioni')
    print('[5] Modifica dati')
    print('[6] Esci\n')
    
    choice = int(input('Cosa vuoi fare? '))
    while choice in range(1,6):
        print(choice)
        break
    else: 
        print('Scelta sbagliata!')
    return choice

print(mainMenu())
#TODO modificare in modo che segua il ciclo principale descritto nell'outline