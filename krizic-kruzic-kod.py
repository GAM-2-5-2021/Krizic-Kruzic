#Križić - kružić
#Teo Crnković, 2. 5

import pygame
from pygame.locals import *

# definiranje osnovnih varijabli u igri
XO   = "X"   # X uvijek igra prvi
mreza = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]

pobjednik = None #prazan prostor u pythonu

# definicija pomocnih funkcija
#------------------------------------------------------------------------------
def PocetnaPloca(kk): #stvaranje pocetne ploce za igru kk-krizic-kruzic
    # pozadina
    pozadina = pygame.Surface (kk.get_size())
    pozadina = pozadina.convert()
    pozadina.fill ((127, 255, 215))
    # crtanje crta u tablici
    # vertikalne linije - boja + debljina
    pygame.draw.line (pozadina, (0,0,0), (100, 0), (100, 300), 2)
    pygame.draw.line (pozadina, (0,0,0), (200, 0), (200, 300), 2)
    # horizontalne linije
    pygame.draw.line (pozadina, (0,0,0), (0, 100), (300, 100), 2)
    pygame.draw.line (pozadina, (0,0,0), (0, 200), (300, 200), 2)
    return pozadina

def NapisiStatusIgre (tablica): #na dnu ploce zelim da pise tko je na redu
    global XO, pobjednik
    # odredivanje statusa igre
    if (pobjednik is None):
        poruka = XO + " je na redu"
    else:
        poruka = pobjednik + " je pobijedio!"
    # sredivanje teksta poruke
    font = pygame.font.Font(None, 24)
    text = font.render(poruka, 1, (10, 10, 10))
    tablica.fill ((250, 250, 250), (0, 300, 300, 25))
    tablica.blit(text, (10, 300))

def PokaziPlocu (kk, tablica):
    # prikaz ploce na ekranu
    # tablica : tablica na kojoj se igra
    NapisiStatusIgre (tablica)
    kk.blit (tablica, (0, 0))
    pygame.display.flip()
    
def PozicijaPloce (misX, misY):
    # nakon kliktanja misem zelim odrediti gdje se kliknulo
    # misX : X koordinata
    # misY : Y koordinata
    # odredivanje retka
    if (misY < 100):
        row = 0
    elif (misY < 200):
        row = 1
    else:
        row = 2
    # odredivanje stupca
    if (misX < 100):
        col = 0
    elif (misX < 200):
        col = 1
    else:
        col = 2
    # vraca redak i stupac kliktaja misa
    return (row, col)

def OznaciKlikMisa (tablica, tablicaRow, tablicaCol, Znak):
    # nacrtaj X ili O
    # odredi centar kvadrata
    centerX = ((tablicaCol) * 100) + 50
    centerY = ((tablicaRow) * 100) + 50
    # nacrtaj odgovarajuci znak
    if (Znak == 'O'):
        pygame.draw.circle (tablica, (0,0,0), (centerX, centerY), 40, 3)
    else:
        pygame.draw.line (tablica, (0,0,0), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 3)
        pygame.draw.line (tablica, (0,0,0), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 3)
    mreza [tablicaRow][tablicaCol] = Znak
    
def NacrtajZnak(tablica):
    global mreza, XO
    (misX, misY) = pygame.mouse.get_pos()
    (row, col) = PozicijaPloce (misX, misY)
    # moramo biti sigurni da je pozicija prazna
    if ((mreza[row][col] == "X") or (mreza[row][col] == "O")):
        # pozicija je zauzeta
        return
    # nacrtaj X ili O
    OznaciKlikMisa (tablica, row, col, XO)
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"
    
def PobjednikIgre(tablica):
    # odredivanje pobjednika
    global mreza, pobjednik
    # provjera pobjednickog retka
    for row in range (0, 3):
        if ((mreza [row][0] == mreza[row][1] == mreza[row][2]) and \
           (mreza [row][0] is not None)):
            # ovaj redak pobjeduje
            pobjednik = mreza[row][0]
            pygame.draw.line (tablica, (250,0,0), (0, (row + 1)*100 - 50), \
                              (300, (row + 1)*100 - 50), 4)
            break
    # provjera pobjednickog stupca
    for col in range (0, 3):
        if (mreza[0][col] == mreza[1][col] == mreza[2][col]) and \
           (mreza[0][col] is not None):
            # ovaj stupac pobjeduje
            pobjednik = mreza[0][col]
            pygame.draw.line (tablica, (250,0,0), ((col + 1)* 100 - 50, 0), \
                              ((col + 1)* 100 - 50, 300), 4)
            break
    # provjera je li pobjeda na dijagonali
    if (mreza[0][0] == mreza[1][1] == mreza[2][2]) and \
       (mreza[0][0] is not None):
        # dijagonala - lijevo - desno
        pobjednik = mreza[0][0]
        pygame.draw.line (tablica, (250,0,0), (50, 50), (250, 250), 4)
    if (mreza[0][2] == mreza[1][1] == mreza[2][0]) and \
       (mreza[0][2] is not None):
        # dijagonala - desno - lijevo
        pobjednik = mreza[0][2]
        pygame.draw.line (tablica, (250,0,0), (250, 50), (50, 250), 4)

#-------------------------------------------------------------------------------		
#OSNOVNI PROGRAM:
pygame.init()
kk = pygame.display.set_mode((300,325))
pygame.display.set_caption ('Krizic - Kruzic') #ovako ce pisati na pygame windowu

# pocetna ploca
tablica = PocetnaPloca (kk)

running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        elif event.type == MOUSEBUTTONDOWN:
            # igrac je kliknuo: nacrtaj X ili O ovisno tko je na redu
            NacrtajZnak(tablica)
        # provjera imamo li pobjednika
        PobjednikIgre (tablica)
        # updataj tablicu
        PokaziPlocu (kk, tablica)


pygame.quit()


















    
    

