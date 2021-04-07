# Conway's Game of life

# Rules
# L'état suivant d'une cellule est : (S = 3) OU (E = 1 ET S = 2).
#   S : nombre actuel de cellules vivantes dans son voisinage (entier naturel compris entre 0 et 8 inclus) ;
#   E : état actuel de la cellule (entier naturel égal à 0 pour une cellule morte et égal à 1 pour une cellule vivante).

from app import App

if __name__ == '__main__':
    print('Game of life is loading')
    app = App()
    app.start()
