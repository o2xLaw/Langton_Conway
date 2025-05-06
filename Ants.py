from grid_tk_template import *
from grid_manager_template import *

def fourmis(grid, nb):
    """ définis la famille de fourmis dans l'interface """
    ants = [{'label' : label, 'position' : get_pos(grid, random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1)),
                 'orientation': 0, 'color' : 'red'} for label in range(nb)]
    return ants
def deplacer(grid,orientation, posx, posy):
    """ deplace la fourmi selon son orientation et ses voisins """
    delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return neighbour(grid, posx, posy, delta[orientation], tore=True)

def droite(orientation):
    """ oriente la fourmi vers sa droite """
    orientation = (orientation+1)%4
    return orientation

def gauche(orientation):
    """ oriente la fourmi vers sa gauche """
    orientation = (orientation-1)%4
    return orientation


