import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from grid_manager_template import *
from grid_tk_template import * 

ctk.set_appearance_mode("light")
ctk.deactivate_automatic_dpi_awareness()
# ----------------- interfaces -----------------


def fenetre():
    """ initialisation de la taille de la grille par l'utilisateur """
    
    window.title('Conway grid')

    width = 700
    height = 200

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    window.resizable(False, False)

    def slider_event(value):
        if value ==  gw.get():
            value_gw = int(value)
            lbl_wscl = ctk.CTkLabel(frm, text = str(value_gw))
            lbl_wscl.grid(row=1, column=2)

        if value == gh.get():
            value_gh = int(value)
            lbl_hscl = ctk.CTkLabel(frm, text = str(value_gh))
            lbl_hscl.grid(row=2, column=2)
        
    # ----------------- Frame -----------------
    frm = ctk.CTkFrame(window, width=width, height=height)
    frm.pack(fill=ctk.BOTH, expand="True", padx=0, pady=0)

    # ----------------- Labels -----------------
    main_label = ctk.CTkLabel(frm, text = 'Choississez les dimmensions de la grille', font= ('arial', 15 ,'underline'), justify='center', anchor= 'n')
    main_label.grid(row=0, column=0)

    lbl1 = ctk.CTkLabel(frm, text = 'Longueur de la grille : ', justify='left', anchor= 'e')
    lbl2 = ctk.CTkLabel(frm, text = 'Hauteur de la grille : ', justify='left', anchor= 'ne')
    lbl3 = ctk.CTkLabel(frm, text = 'Couleur du background : ', justify='left', anchor= 'w')
    lbl4 = ctk.CTkLabel(frm, text = 'Couleur des celulles : ', justify='left', anchor= 'w')

    lbl1.grid(row = 1, column= 0, pady=2, padx=2)
    lbl2.grid(row = 2, column= 0, pady=2, padx=2)
    lbl3.grid(row = 3, column= 0, pady=2, padx=2)
    lbl4.grid(row = 4, column= 0, pady=2, padx=2)

    # ----------------- Scales / Entry -----------------

    gw = IntVar()
    gh = IntVar()

    width_scale = ctk.CTkSlider(frm, from_=50, to=100, orientation="horizontal", variable = gw, number_of_steps = 10, fg_color=('turquoise', 'grey'), command= lambda value= gw:slider_event(value))
    width_scale.grid(row=1, column=1)

    height_scale = ctk.CTkSlider(frm, from_=50, to=100, orientation="horizontal", variable = gh, number_of_steps = 10,fg_color=('turquoise', 'grey'),command= lambda value = gh:slider_event(value))
    height_scale.grid(row=2, column=1, pady = 2)

    entry_bg = ctk.CTkEntry(frm, text_color="lightgreen")
    entry_bg.grid(row=3, column=1,pady = 2)

    entry_cell = ctk.CTkEntry(frm, text_color= "lightgreen")
    entry_cell.grid(row=4, column=1,pady = 2)

    # ----------------- Fonctions -----------------
    def pick_color(btn_type):
        """ entre une couleur dans l'entry choisi par l'utilisateur"""
        
        if btn_type == 'canva':
            initial_color = entry_bg.get()
            # Si l'entry est vide
            if not initial_color :
                initial_color = "white"

            color = askcolor(initialcolor= initial_color)
            #print(color)
            if color[1] is not None:
                entry_bg.delete(0,END)
                entry_bg.insert(0, color[1])
        else:
            initial_color = entry_cell.get()
            # Si l'entry est vide
            if not initial_color :
                initial_color = "black"

            color = askcolor(initialcolor= initial_color)
            #print(color)
            if color[1] is not None:
                entry_cell.delete(0,END)
                entry_cell.insert(0, color[1])

    def valider():
        """ valide les initialisations entrées par l'utilisateur"""
        global  grid_width, grid_height, color_cell

        valid_config.configure(state = 'disabled')
        grid_width = int(width_scale.get())
        grid_height = int(height_scale.get())

        if entry_bg.get() == "" : COLORS['bg'] = "white"
        else: COLORS['bg'] = entry_bg.get()
        
        if entry_cell.get() == "" : color_cell = "black"
        else: color_cell = entry_cell.get()
            
        width_scale.configure(state = 'disabled')
        height_scale.configure(state = 'disabled')
        window.destroy()
        
    
    def annuler():
        """ permet d'arreter à l'initialisation des dimensions et ainsi ne pas lancer le programme qui suit"""
        global state_window
        state_window = False
        window.destroy()
    
        # ----------------- Buttons -----------------
        
    color_btn = ctk.CTkButton(frm, text="Pick color", command=lambda : pick_color('canva'), fg_color="springgreen",text_color="black", hover_color="mediumspringgreen")
    color_btn.grid(row=3, column=2, padx=2, pady=2)

    color_btn_cell = ctk.CTkButton(frm, text="Pick color", command= lambda: pick_color('cell'), fg_color="springgreen", text_color="black", hover_color="mediumspringgreen")
    color_btn_cell.grid(row=4, column=2, padx=2, pady=2)

    valid_config = ctk.CTkButton(frm, text = 'Valider', command=valider, state='normal')
    valid_config.grid(row=5, column = 2, sticky='se')

    window.protocol("WM_DELETE_WINDOW", annuler)

    window.mainloop()

def limit_size_cell():
    """ modifie la taille des cellules de la grille selon les dimensions de la grille choisies"""
    global size_cell, grid_width, grid_height

    if 50<= grid_width <75 and 50<= grid_height <75 :
        size_cell = 10
    elif 75 <= grid_width <100 and 75<= grid_height <100:
        size_cell = 5
    
    elif grid_height< 100 and grid_width>100 :
        size_cell = 8
    else: size_cell = 8

def render():

    root.title('Conway')
    root.resizable(False,False)

    width = int(main_cnv['width'])
    height = int(main_cnv['height']) + 50

    # Récupère la largeur et la hauteur de l'écran
    ws = root.winfo_screenwidth() # largeur
    hs = root.winfo_screenheight() # hauteur

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    # placement de la fenetre
    root.geometry('%dx%d+%d+%d' % (width,height,x0,y0))
    main_cnv.grid(row = 0, column = 0, sticky=NSEW)
   
    #-------------------------------------------------------------------------------------------------------------------------------------

    def draw_grid():
        global main_cnv, color_cell, grid
        
        for x in range(int(nb_lines(grid))):
            for y in range(int(nb_columns(grid))):
                
                if grid[x][y]== 1:
                    set_cell(main_cnv, grid, x, y, 1, color_cell, show_vals=False, outline=False, color_text=COLORS['text_val'])
                else:
                    set_cell(main_cnv, grid, x, y, 0, COLORS['bg'], show_vals=False, outline=False, color_text=COLORS['text_val'])
    
    def drive():
        global grid, after_id
        deltas = DELTAS_CONWAY
        it_grid= grid_empty()
        draw_grid()
        
        for x in range(int(nb_lines(grid))):
            for y in range(int(nb_columns(grid))):

                liste_voisins = neighborhood(grid, x, y, deltas, tore=True)
                #print(liste_voisins)
                nb_vivants = sum(liste_voisins)

                if grid[x][y]==1 and (nb_vivants == 3 or nb_vivants == 2) or (grid[x][y]==0 and nb_vivants == 3):
                    # la cellule garde son statut vivant
                    it_grid[x][y]=1
                else:
                    it_grid[x][y]=0

        grid = it_grid
        after_id = main_cnv.after(10,drive)

    def retry():
        global grid, main_cnv, after_id
        main_cnv.after_cancel(after_id)
        after_id = None
        main_cnv.delete()
        grid = new_grid()
        
        main_cnv = grid_ctkcanvas(root, grid, size_cell, margin=10, gutter=2, show_vals=False, outline=False)
        main_cnv.grid(row = 0, column = 0)
    #---------------------------------------------------------------------------------------------------------------------------------
        # Variable pour suivre l'état du bouton
    bouton_etat = ctk.StringVar()
    bouton_etat.set("Arrêter")
    
    def start():
        """ lance le programme de déplacement des fourmis"""
        global after_id
        bouton_etat.set("Démarrer")

        # after_id est nécéssaire pour pouvoir stopper le programme
        after_id = drive()

    def stop():
        """ met en pause le déplacement de la fourmi"""
        global after_id
        main_cnv.after_cancel(after_id)
        bouton_etat.set("Arrêter")
    
    def gestion_barre_espace(event):
        """ gère l'arret ou le démarrage du développement """
        if event.keysym == 'space':
            if bouton_etat.get() == "Démarrer":
                stop()
            else:
                start()

    def quitter(event = None):
        """ Demande si l'utilisateur veut quitter le jeu """
        global after_id
        if after_id is not None:
            main_cnv.after_cancel(after_id)
            if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate de Conway ?"):
                    root.quit()
            else: after_id = drive()
        else:
            if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate de Conway ?"):
                root.quit()

    root.protocol("WM_DELETE_WINDOW", quitter)
    # Button
    lancer = ctk.CTkButton(root, text='Lancer', command=drive)
    lancer.grid(row=1, column=0,sticky='sw')
   
    new_game = ctk.CTkButton(root, text='Rejouer', command=retry)
    new_game.grid(row=1, column=0)

    quitter_btn = ctk.CTkButton(root, text='Quitter', command=quitter)
    quitter_btn.grid(row=1, column=0, sticky='se')

    root.bind('<Control-q>', quitter)
    root.bind('<space>', gestion_barre_espace)

    root.mainloop()

# Création d'une grille vide de départ
def grid_empty():
    global grid_width, grid_height
    grid = create_grid_lc(grid_width, grid_height, 0)
    return grid

# Création d'une grille de cellules random
def new_grid():
    global grid_width, grid_height
    grid = create_random_grid_lc(grid_width, grid_height, [0,1])
    return grid

if __name__ == "__main__":

    grid_width = 0 # largeur de la grille
    grid_height = 0 # hauteur de la grille
    size_cell = 0
    after_id = None
    state_window = True
    color_cell = ''
    window = ctk.CTk()
    fenetre()
    
    if state_window == True:
        limit_size_cell()
        
        grid = create_random_grid_lc(grid_width, grid_height, [0,1])
        root = ctk.CTk() # invalidcommand lié à Ctk en Tk() ça marche 
        main_cnv = grid_canvas(root, grid, size_cell, margin=10, gutter=2, show_vals=False, outline=False)       
        
        render()
        
        