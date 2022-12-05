import pyautogui
from pynput.keyboard import *
from os import system

avviamelo = Key.f7  # autoclicker start 
quitta = Key.f8     # autoclicker quit
pausamelo = Key.f9  # autoclicker pausa
                    # binds: https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
tasto = 'sx'        # dx = right , sx = left
statopausa = True   # non toccare
statoavviato = True # non toccare
keylog = False      # printa i tasti che premi

def quandopremiiltasto(tasto):
    global statopausa, statoavviato
    if keylog == True:
        print(f'Premuto il tasto: {tasto}')
    
    if tasto == avviamelo:
        print('AutoClicker: Avviato')
        stato = 'Avviato'
        system(f"title AutoClicker, Stato: {stato} - github.com/itsmat")
        statopausa = False
    elif tasto == pausamelo:
        statopausa = True
        stato = 'In pausa'
        system(f"title AutoClicker, Stato: {stato} - github.com/itsmat")
        print('AutoClicker: Stoppato')
    elif tasto == quitta:
        stato = 'Quit in corso'
        system(f"title AutoClicker, Stato: {stato} - github.com/itsmat")
        statoavviato = False
        print('AutoClicker: Quittato')
    

def home():
    if tasto != 'sx' and tasto != 'dx':
        print('Tasto inserito non valido, utilizza dx per utilizzare il tasto destro o utilizza sx per il tasto sinistro')
        exit()
    
    print('\nSettings:')
    print(f'[+] Avvio: {avviamelo}')
    print(f'[+] Pausa: {pausamelo}')
    print(f'[+] Quit: {quitta}')
    print(f'[+] Tasto: {tasto}')
    print('                       github.com/itsmat')
    print('-------------------------')
    print(f'''Premi {avviamelo} per avviare l'autoclicker''')

    
    
def inizio():
    stato = 'In pausa'
    system(f"title AutoClicker, Stato: {stato} - github.com/itsmat")
    global statopausa, statoavviato
    controllo = Listener(on_press=quandopremiiltasto)
    controllo.start()

    home()
    while statoavviato:
        if not statopausa:
            if tasto == 'dx':
                pyautogui.click(button='right')
            elif tasto == 'sx':
                pyautogui.click()
            elif tasto != 'sx' and tasto != 'dx':
                print('Tasto inserito non valido, utilizza dx per utilizzare il tasto destro o utilizza sx per il tasto sinistro')
    controllo.stop()
            
inizio()
