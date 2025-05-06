import random

DELTAS_CONWAY = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def create_grid_lc(lin, col, val):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisées à 'val'"""
    Tab = [[val for colonnes in range(col)] for lignes in range(lin)]
    return Tab

def create_random_grid_lc(lin, col, vals):
    """Retourne une grille de 'lin' lignes et 'col' colonnes
    initialisés aléatoirement avec des valeurs de la liste 'vals'"""
    Tab = [[random.choice(vals) for colonnes in range(col)] for lignes in range(lin)]
    return Tab

def nb_lines(grid):
    """Retourne le nombre de lignes de la grille 'grid'"""
    return len(grid)

def nb_columns(grid):
    """Retourne le nombre de colonnes de la grille 'grid'"""
    return len(grid[0])

def line2str(grid, num_line, sep='\t'):
    """Retourne la chaine de caractère correspondant à la concaténation des valeurs
    de la ligne numéro 'num_line' de la grille 'grid'. Les caractères sont séparés par le caractère 'sep'"""
    ligne = grid[num_line]
    ligne_str = sep.join(map(str,ligne))
    return ligne_str

def grid2str(grid, sep='\t'):
    """Retourne la chaine de caractère représentant la grille 'grid'.
    Les caractères de chaque ligne de 'grid' sont séparés par le caractère 'sep'.
    Les lignes sont séparées par le caractère de retour à la ligne \n"""

    lines = [line2str(grid,i, sep) for i in range(len(grid))]
    grille_str = '\n'.join(map(str,lines))
    return grille_str

def get_pos(grid, i, j):
    return i,j

def neighbour(grid, lin, col, delta, tore=True):
    """Retourne le voisin de la cellule 'grid[lin][col]' selon le tuple 'delta' = (delta_lin, delta_col).
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille 'grid'."""

    if tore:
        #voisin = grid[int(lin+delta[0])%(nb_lines(grid))][int(col+delta[1])%(nb_columns(grid)]
        #return voisin
        i = int(lin+delta[0])%nb_lines(grid)
        j = int(col+delta[1])%nb_columns(grid)
        voisin=grid[i][j]
        return i,j
    
    else:
        if 0<= int(lin+delta[0])<nb_lines(grid) and 0<= int(col+delta[0])< nb_columns(grid):
            voisin = grid[int(lin+delta[0])][int(col+delta[1])]
            return voisin
        
        else:
            return None

def neighborhood(grid, lin, col, deltas, tore=True):
    """Retourne pour la grille 'grid' la liste des N voisins de 'grid[lin][col]'
    correspondant aux N (delta_lin, delta_col) fournis par la liste 'deltas'.
    Si 'tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'tore' est à 'False' un voisin hors de la grille 'grid' n'est pas considéré."""

    if tore ==True:
        
        voisins=[grid[int(lin+deltas[i][0])%nb_lines(grid)][int(col+deltas[i][1])%nb_columns(grid)] for i in range(len(deltas))]
        return voisins
    else:
        
        voisins = [grid[int(lin+deltas[i][0])][int(col+deltas[i][1])]for i in range(len(deltas)) if 0<= int(lin+deltas[i][0])<nb_lines(grid) and 0<= int(col+deltas[i][1])<nb_columns(grid)]
        return voisins

if __name__ == "__main__":
    """Définitions des variables de test et des tests de chaque fonction"""
    # Tuple des déplacements (delta_lig, delta_col) pour repérer une cellule voisine dans une grille de Conway.
    # Les 8 directions possibles dans l'ordre sont : NO, N, NE, O, E, SO, S, SE.

    DELTAS_CONWAY = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    #grid = create_random_grid_lc(5, 5,[0,1])
    #print(create_random_grid_lc(5, 5,[0,1]))
    #print(create_grid_lc(3,3,4))
    #print(grid)
    #print(nb_lines(grid))
    #print(line2str(grid, 3, sep='\t'))
    #print(grid2str(grid, sep='\t'))
    #print('cas tore=True : ',neighbour(grid, 0,0, (-19, 0), tore = True))
    #print('cas tore=False : ',neighbour(grid, 0,0, (1, 0), tore = False))
    #print(neighborhood(grid, 0, 0, DELTAS_CONWAY, tore=True))
    #print(neighborhood(grid, 2, 2, DELTAS_CONWAY, tore=False))

