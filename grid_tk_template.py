from tkinter import *
from customtkinter import *
from grid_manager_template import *

# Dictionnaires des paramètres de forme d'une grille
COLORS = {'bg': 'white', 'fg': 'red', 'outline': 'black', 'text_val': 'black'}
FONT = {'text_val': 'Arial'}

def grid_canvas(master, grid, size_cell, margin=10, gutter=5, show_vals=True, outline=True):
    """Retourne un 'Canvas' placé dans la fenêtre 'master'. Celui-ci est construit à partir de la grille 'grid'
    en s'appuyant sur les modules 'grid_manager' et 'tkinter' ainsi que sur les dictionnaires des paramètres de forme.
    La largeur et la hauteur du Canvas sont calculés en considérant la taille 'size_cell' d'une cellule, la valeur de
    marge 'margin' autour de la grille et d'une taille de gouttière 'gutter' entre les lignes et les colonnes.
    Chaque cellule affichera en son centre le texte correspondant à son contenu si 'show_vals' est à la valeur 'True'.
    Les bordures des cellules ne s'afficheront que si 'outline' est à la valeur 'True'.
    Chaque cellule sera taguée par la chaine 'c_lin_col' et leur texte par la chaine 't_lin_col'.
    De plus, les deux seront taguées en plus par la chaine 'lin_col'."""
    
    x_cnv = nb_lines(grid) 
    y_cnv = nb_columns(grid)
    #print(x_cnv,y_cnv)
    
    main_cnv = Canvas(master, width=x_cnv*size_cell+2*margin + gutter*(x_cnv-1), height=y_cnv*size_cell+2*margin +gutter*(y_cnv-1) , bg =COLORS['bg'], cursor="target")
    
    for x in range(x_cnv):
        for y in range(y_cnv):
            x_pos = margin + x *size_cell +gutter*x
            y_pos = margin + y *size_cell + gutter*y

            textx_pos = margin + x * size_cell +gutter*x+ size_cell / 2
            texty_pos = margin + y * size_cell +gutter*y + size_cell / 2
            main_cnv.create_rectangle(x_pos, y_pos, x_pos+size_cell, y_pos+size_cell , fill=COLORS['bg'],outline=COLORS['outline'] if outline else COLORS['bg'], tags=('c_'+str(x)+'_'+str(y)) )
            main_cnv.create_text(textx_pos, texty_pos, text= str(grid[x][y]) if show_vals else '', fill=COLORS['text_val'], tags=('t_'+str(x)+'_'+str(y)) )
                
    return main_cnv

def grid_ctkcanvas(master, grid, size_cell, margin=10, gutter=5, show_vals=True, outline=True):
    """Retourne un 'Canvas' placé dans la fenêtre 'master'. Celui-ci est construit à partir de la grille 'grid'
    en s'appuyant sur les modules 'grid_manager' et 'customtkinter' ainsi que sur les dictionnaires des paramètres de forme.
    La largeur et la hauteur du Canvas sont calculés en considérant la taille 'size_cell' d'une cellule, la valeur de
    marge 'margin' autour de la grille et d'une taille de gouttière 'gutter' entre les lignes et les colonnes.
    Chaque cellule affichera en son centre le texte correspondant à son contenu si 'show_vals' est à la valeur 'True'.
    Les bordures des cellules ne s'afficheront que si 'outline' est à la valeur 'True'.
    Chaque cellule sera taguée par la chaine 'c_lin_col' et leur texte par la chaine 't_lin_col'.
    De plus, les deux seront taguées en plus par la chaine 'lin_col'."""
    
    x_cnv = nb_lines(grid) 
    y_cnv = nb_columns(grid)
    #print(x_cnv,y_cnv)
    
    main_cnv = CTkCanvas(master, width=x_cnv*size_cell+2*margin + gutter*(x_cnv-1), height=y_cnv*size_cell+2*margin +gutter*(y_cnv-1) , bg =COLORS['bg'])

    for x in range(x_cnv):
        for y in range(y_cnv):
            x_pos = margin + x *size_cell +gutter*x
            y_pos = margin + y *size_cell + gutter*y

            textx_pos = margin + x * size_cell +gutter*x+ size_cell / 2
            texty_pos = margin + y * size_cell +gutter*y + size_cell / 2
            
            main_cnv.create_rectangle(x_pos, y_pos, x_pos+size_cell, y_pos+size_cell , fill=COLORS['bg'],outline=COLORS['outline'] if outline else COLORS['bg'], tags=('c_'+str(x)+'_'+str(y)) )
            main_cnv.create_text(textx_pos, texty_pos, text= str(grid[x][y]) if show_vals else '', fill=COLORS['text_val'], tags=('t_'+str(x)+'_'+str(y)) )
                
    return main_cnv

def get_lines_columns(can):
    """Retourne le nombre de lignes et de colonnes de la grille représentée par le Canvas 'can'."""
    tag = can.find_all()[-1]
    tag_end = can.itemcget(tag, 'tags')
    width = tag_end.split('_')[1]
    height =tag_end.split('_')[2]
    return width, height 

def get_grid(can):
    """Retourne la grille représentée par le Canvas 'can'."""
    grid=[]
    grid_width = get_lines_columns(can)[0]
    grid_height = get_lines_columns(can)[1] 
    # pq quand j'inverse x et y cela donne la bonne grille ? 
    for y in range(grid_width):
        row = []
        for x in range(grid_height):
            text_tag = f't_{x}_{y}'
            text_tags = can.find_withtag(text_tag)
            item_coords = can.itemcget(text_tags,'text')
            row.append(int(item_coords))
        grid.append(row)

    return grid

def get_color_cell(can, i, j):
    """Retourne la couleur de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    cell_tag = f'c_{i}_{j}'
    cell_color= can.find_withtag(cell_tag)
    color = can.itemcget(cell_color,'fill')
    return color

def set_color_cell(can, i, j, color, outline=False):
    """Rempli la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'.
    Dessine ses bordures avec la couleur 'color' si 'outline' a la valeur 'False'."""
    cell_tag = f'c_{i}_{j}'
    cell_color= can.find_withtag(cell_tag)
    if outline == True:
        can.itemconfigure(cell_color, fill=color, outline=color)
    else:
        can.itemconfigure(cell_color, fill=color)
    
def get_color_text(can, i, j):
    """Retourne la couleur du texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can'."""
    text_tag = f't_{i}_{j}'
    text_color= can.find_withtag(text_tag)
    color = can.itemcget(text_color,'fill')
    return color

def set_color_text(can, i, j, color):
    """Rempli le texte de la cellule ('i', 'j') de la grille représentée par le Canvas 'can' par la couleur 'color'."""
    text_tag = f't_{i}_{j}'
    text_color= can.find_withtag(text_tag)
    can.itemconfigure(text_color, fill=color)

def get_cell_text(can, i, j):
    """Retourne la valeur du texte de la cellule ('i', 'j') du Canvas 'can'"""
    text_tag = f't_{i}_{j}'
    text_value= can.find_withtag(text_tag)
    value = can.itemcget(text_value,'text')
    return value

def set_cell_text(can, i, j, val):
    """Change la valeur du texte de la cellule ('i', 'j') du Canvas 'can' avec la valeur 'val'"""
    text_tag = f't_{i}_{j}'
    text_value= can.find_withtag(text_tag)
    can.itemconfigure(text_value, text=val)

def set_cell(can, grid, i, j, val, color_cell, show_vals=True, outline=True, color_text=COLORS['text_val']):
    """Modifie la grille 'grid' et le Canvas 'can' en affectant la valeur 'val' à la cellule ('i', 'j').
    Change la couleur de fond par 'color_cell'.
    Change la couleur du texte par 'color_text' et la valeur par 'val' si 'show_vals' a la valeur 'True'.
    Dessine les bordures de la cellule selon la valeur booléenne de 'outline'."""
    grid[i][j]= val
    set_color_cell(can, i, j, color_cell, outline)
    
    if show_vals ==True:
        set_cell_text(can, i, j, val)
        set_color_text(can, i, j, color_text)
    
def modif_cnv(canvas, grid, color_cell):
    """ permet de modifier une cellule du canvas """
    set_cell(canvas, grid, random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1), 1, "black" if color_cell==None else color_cell, outline=False, show_vals=False)

if __name__ == "__main__":
    """Définitions des variables de test et des tests de chaque fonction"""
    
    root = Tk()
    root.title('Jeu de la vie')
    #root.resizable(False,False)
    width = 700
    height = 600

    # Récupère la largeur et la hauteur de l'écran
    ws = root.winfo_screenwidth() # largeur
    hs = root.winfo_screenheight() # hauteur

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    # placement de la fenetre
    root.geometry('%dx%d+%d+%d' % (width,height,x0,y0))

    grid = create_random_grid_lc(5, 5, [0,1,2,3,4])
    canvas = grid_canvas(root, grid, size_cell=50, margin=20, gutter=0, show_vals=True, outline=True)
    canvas.grid(row = 0, column = 0, sticky = 'snew')

    #print(get_lines_columns(canvas))
    #print(get_color_cell(canvas,2,0))
    #print(neighbour(grid, 4, 4, (1,0), tore=True))
    #print(get_cell_text(canvas, 2, 1))
    #x, y = neighbour(grid, 4, 4, (1,0), tore=True)
    #set_color_cell(canvas, 2, 0, 'light blue', outline=False)
    #print(get_color_text(canvas, 2, 0))
    #set_color_text(canvas, 2, 0, 'purple')
    #print(get_cell_text(canvas, x, y))
    #set_cell_text(canvas, 0, 0, 5)
    #set_cell(canvas, grid, 3, 3, 10, 'light blue', show_vals=False, outline=False, color_text=COLORS['text_val'])
    root.mainloop()
    
    
    