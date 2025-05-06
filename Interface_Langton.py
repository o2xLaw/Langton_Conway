import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from grid_tk_template import *
from Ants import *
from Toplevel import *

# ----------------- interfaces -----------------

def fenetre():
    """ initialisation de la taille de la grille par l'utilisateur """

    window = tk.Tk()
    window.title('Langton grid')

    width = 500
    height = 200

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    window.resizable(False, False)

    # ----------------- Frame -----------------
    frm = tk.Frame(window, bg='snow', width=width, height=height)
    frm.pack(fill=BOTH, expand=TRUE, padx=0, pady=0)

    # ----------------- Labels -----------------
    main_label = tk.Label(frm, text = 'Choississez les dimmensions de la grille', font= ('arial', 10, 'underline'), justify='center', anchor= 'n', bg='snow')
    main_label.grid(row=0, column=0)

    lbl1 = tk.Label(frm, text = 'Longueur de la grille : ', justify='left', anchor= 'e', bg='snow')
    lbl2 = tk.Label(frm, text = 'Hauteur de la grille : ', justify='left', anchor= 'ne', bg='snow')
    lbl3 = tk.Label(frm, text = 'Couleur du background : ', justify='left', anchor= 'w', bg='snow')

    lbl1.grid(row = 1, column= 0, pady=2, padx=2)
    lbl2.grid(row = 2, column= 0, pady=2, padx=2)
    lbl3.grid(row = 3, column= 0, pady=2, padx=2)

    # ----------------- Scales / Entry -----------------
    width_scale = tk.Scale(frm, from_=50, to=150, orient="horizontal", variable = IntVar(), resolution = 5, bg='snow', troughcolor='grey')
    width_scale.grid(row=1, column=1)

    height_scale = tk.Scale(frm, from_=50, to=150, orient="horizontal", variable = IntVar(),resolution = 5, bg='snow', troughcolor='grey')
    height_scale.grid(row=2, column=1, pady = 2)

    entry_bg = tk.Entry(frm, width=20, cursor="ibeam", bd=5)
    entry_bg.grid(row=3, column=1,pady = 2)

    # ----------------- Fonctions -----------------
    def pick_color():
        """ entre une couleur dans l'entry choisi par l'utilisateur"""

        initial_color = entry_bg.get()
        # Si l'entry est vide
        if not initial_color :
            initial_color = "white"

        color = askcolor(initialcolor= initial_color)
        #print(color)
        if color[1] is not None:
            entry_bg.delete(0,END)
            entry_bg.insert(0, color[1]) 
            
    def valider():
        """ valide les initialisations entrées par l'utilisateur"""
        global width_grid, height_grid

        valid_config.config(state = 'disabled')
        width_grid = width_scale.get()
        height_grid = height_scale.get()

        if entry_bg.get() == "": COLORS['bg'] = "white"
        else:COLORS['bg'] = entry_bg.get()

        width_scale.config(state = 'disabled')
        height_scale.config(state = 'disabled')
        
        window.destroy()
    
    def annuler():
        global state_window
        state_window = False
        window.destroy()
    
    # ----------------- Buttons -----------------
        
    color_btn = tk.Button(frm, text="Pick color", command=pick_color, cursor="hand2")
    color_btn.grid(row=3, column=2, padx=2, pady=2)

    valid_config = tk.Button(frm, text = 'Valider', command=valider, state='normal', cursor="hand2")
    valid_config.grid(row=4, column = 3, sticky='se')

    window.protocol("WM_DELETE_WINDOW", annuler)

    window.mainloop()

def limit_size_cell():
    """ modifie la taille des cellules de la grille selon les dimensions de la grille choisies"""
    global size_cell, width_grid, height_grid

    if 50<= width_grid <75 and 50<= height_grid <75 :
        size_cell = 10
    elif 75 <= width_grid <130 and 75<= height_grid <130:
        size_cell = 5
    
    elif height_grid< 100 and width_grid>100 :
        size_cell = 8
    else:
        size_cell = 3
        
def render():
    # ----------------- Positionnement de la fenetre + canva -----------------
    
    root.title('Langton')
    root.configure(bg="white")

    width = int(canvas['width']) + 400
    height = int(canvas['height']) +10 if height_grid <100 and width_grid >100 else int(canvas['height'])

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x0, y0))
    root.resizable(True, True)

    canvas.grid(row=0, column=0, sticky=NSEW)
    canvas.focus_set()
    
    # ----------------- Frame principale -----------------

    main_frm = tk.Frame(root, width=400, height=height, bg='white')
    main_frm.grid(row=0, column=1, sticky=NSEW)

    def quitter(event = None):
        """ Demande si l'utilisateur veut quitter le jeu """
        if bouton_etat.get() == "Démarrer":
            stop()
            if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate fourmi de Langton ?"):
                root.destroy()
            else : start()
        else:
            if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'automate fourmi de Langton ?"):
                root.destroy()

    # ----------------- MenuBar -----------------
    # MenurBar définis dans le fichier TopLevel.py
    menubar = tk.Menu(root)
    menubar.add_command(label="Jeu", command=jeu)
    menubar.add_command(label="Options", command=options)
    menubar.add_command(label="Commandes", command=commands)
    menubar.add_command(label="Couleurs", command=colors_possibility)
    menubar.add_command(label="Quitter", command=quitter)

    root.config(menu = menubar)
    root.protocol("WM_DELETE_WINDOW", quitter)

    # ------------------- LabelFrames -------------------
    # compteur
    lbl_compteur = tk.LabelFrame(main_frm, height= 50, text = 'Compteur')
    lbl_compteur.grid(row=1, column=0, sticky=NSEW, columnspan=2)
    lbl_compteur.columnconfigure(0, weight=1)

    # nombre de fourmis à entrer
    lbl_nb_fourmis = tk.LabelFrame(main_frm, height= 50, text = 'Nombre de fourmis')
    lbl_nb_fourmis.grid(row=2, column=0, sticky=NSEW, columnspan=2)
    lbl_nb_fourmis.columnconfigure(0, weight=1)

    # choix des couleurs
    lbl_cell_color = tk.LabelFrame(main_frm, height=50, text = 'Couleurs des fourmis')
    lbl_cell_color.grid(row=3, column=0, sticky=NSEW, columnspan=2)
    lbl_cell_color.columnconfigure(0, weight=1)

    # choix de vitesse
    lbl_speed = tk.LabelFrame(main_frm, height= 50, text = 'Vitesse')
    lbl_speed.grid(row=4, column=0, sticky=NSEW, columnspan=2)
    lbl_speed.columnconfigure(0, weight=1)

    # initialisation des labels des choix de couleurs
    color_labels = ['1', '2', '3', '4']
    lbl_color_fourmi = []
    
    # création des labels de couleurs
    for i, lbl in enumerate(color_labels):

        lbl_fourmis_color = tk.LabelFrame(lbl_cell_color, height=50, text = 'Fourmis '+str(lbl))
        lbl_fourmis_color.grid(row=i, column=0, sticky=NSEW ,columnspan=2)

        lbl_color_fourmi.append(lbl_fourmis_color)

    # ------------------- Label / Entry / Scale -------------------
    
    compteur = tk.Label(lbl_compteur, font=FONT['text_val'], text= str(cpt), justify='center')
    compteur.grid(row=0, column=0, columnspan=1)

    # label indiquant le nombre à entrer
    lbl_set_nb= tk.Label(lbl_nb_fourmis, text= 'Entrez un nombre de fourmis : ', font=FONT['text_val'])
    lbl_set_nb.grid(row=0, column=0)

    scale_speed = tk.Scale(lbl_speed, from_=10, to=200, orient="horizontal", variable = IntVar(), resolution = 5)
    scale_speed.grid(row=0, column=0)

    # initialisation de l'entry
    entry_val = tk.IntVar()
    entry_val.set('1')

    entry_nb_fourmis = tk.Entry(lbl_nb_fourmis, textvariable=entry_val, cursor="ibeam", bd=3)
    entry_nb_fourmis.grid(row=0, column=1)

    # ------------------- RadioButtons -------------------
        
    # initialisation des valeurs
    radiobuttons = []
    entries = []
    colors = ['red', 'blue', 'green', 'couleur : ']

    color_f1 = tk.StringVar()
    color_f2 = tk.StringVar()
    color_f3 = tk.StringVar()
    color_f4 = tk.StringVar()
    
    color_f1.set('red')
    color_f2.set('red')
    color_f3.set('red')
    color_f4.set('red')

    # création des différents RadioButtons selon la couleur indiqué par 'colors'
    for i, color in enumerate(colors):

        # ----------- Fourmi 1 -----------
        rb_1 = tk.Radiobutton(lbl_color_fourmi[0], variable=color_f1, text=color, value=color, command=lambda color=color_f1: color_fourmi(color, 0), state=DISABLED)
        rb_1.grid(row=0, column=i, padx=2, pady=2)
        
        # ----------- Fourmi 2 -----------
        rb_2 = tk.Radiobutton(lbl_color_fourmi[1], variable=color_f2, text=color, value=color, command=lambda color=color_f2: color_fourmi(color, 1), state=DISABLED)
        rb_2.grid(row=0, column=i, padx=2, pady=2)

        # ----------- Fourmi 3 -----------
        rb_3 = tk.Radiobutton(lbl_color_fourmi[2], variable=color_f3, text=color, value=color, command=lambda color=color_f3: color_fourmi(color, 2), state=DISABLED)
        rb_3.grid(row=0, column=i, padx=2, pady=2)

        # ----------- Fourmi 4 -----------
        rb_4 = tk.Radiobutton(lbl_color_fourmi[3], variable=color_f4, text=color, value=color, command=lambda color=color_f4: color_fourmi(color, 3), state=DISABLED)
        rb_4.grid(row=0, column=i, padx=2, pady=2)

        if color == 'couleur : ':

            # ----------- Fourmi 1 -----------
            rb_1 = tk.Radiobutton(lbl_color_fourmi[0], variable=color_f1, text=color, value=color, command=lambda color=color_f1: color_entry(color, 0), state=DISABLED)
            rb_1.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_1 = tk.Entry(lbl_color_fourmi[0], width = 18,state=DISABLED, cursor="ibeam")
            entry_color_cell_1.grid(row=0,column=i+1)

            # ----------- Fourmi 2 -----------
            rb_2 = tk.Radiobutton(lbl_color_fourmi[1], variable=color_f2, text=color, value=color, command=lambda color=color_f2: color_entry(color, 1), state=DISABLED)
            rb_2.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_2 = tk.Entry(lbl_color_fourmi[1], width = 18, state=DISABLED, cursor="ibeam")
            entry_color_cell_2.grid(row=0,column=i+1)

            # ----------- Fourmi 3 -----------
            rb_3 = tk.Radiobutton(lbl_color_fourmi[2], variable=color_f3, text=color, value=color, command=lambda color=color_f3: color_entry(color, 2), state=DISABLED)
            rb_3.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_3 = tk.Entry(lbl_color_fourmi[2], width = 18,state=DISABLED, cursor="ibeam")
            entry_color_cell_3.grid(row=0,column=i+1)

            # ----------- Fourmi 4 -----------
            rb_4 = tk.Radiobutton(lbl_color_fourmi[3], variable=color_f4, text=color, value=color, command=lambda color=color_f4: color_entry(color, 3), state=DISABLED)
            rb_4.grid(row=0, column=i, padx=2, pady=2)

            entry_color_cell_4 = tk.Entry(lbl_color_fourmi[3], width = 18, state=DISABLED, cursor="ibeam")
            entry_color_cell_4.grid(row=0,column=i+1)

            entries.append((entry_color_cell_1,entry_color_cell_2, entry_color_cell_3, entry_color_cell_4))

        radiobuttons.append((rb_1, rb_2, rb_3, rb_4))
    
    # ------------------- Fonctions interactives -------------------
    # Variable pour suivre l'état du bouton
    bouton_etat = tk.StringVar()
    bouton_etat.set("Arrêter")

    def valider():
        """ valide l'ensemble des entrées indiqués par l'utilisateur """
        global check
        check = True
        state_radiobtn()
        startbtn['state'] = 'active'
    
    def start():
        """ lance le programme de déplacement des fourmis"""
        global after_id
        startbtn.config(state=NORMAL)
        btn_valid.config(state=DISABLED)

        bouton_etat.set("Démarrer")

        # after_id est nécéssaire pour pouvoir stopper le programme
        after_id = dep_fourmi()

    def stop():
        """ met en pause le déplacement de la fourmi"""
        global after_id
        root.after_cancel(after_id)
        bouton_etat.set("Arrêter")
    
    def gestion_barre_espace(event):
        """ gère l'arret ou le démarrage du développement """
        if event.keysym == 'space':
            if bouton_etat.get() == "Démarrer":
                stop()
            else:
                start()

    def retry():
        """ réinitialise le canvas et le compteur """
        global canvas, cpt
        # on supprime le canvas
        canvas.delete(ALL)

        # création d'un canva identique
        canvas = grid_canvas(root, grid, size_cell, margin=10, gutter=2, show_vals=False, outline=False)
        canvas.grid(row=0, column=0, sticky=NSEW)
        canvas.focus_set()

        # création d'un nouveau binf pour le nouveau canva
        canvas.bind('<Button-1>', ajout_cell)
        # remise à 0 du compteur
        cpt = 0
        compteur.config(text=str(cpt))

    def reinitialiser(event=None):
        """ réinitialise les options de la fourmi """
        global check, nb_fourmis, after_id
        check = True
        if after_id !=None: stop()
        after_id = None
        
        startbtn.config(state=DISABLED)
        
        for i in range(nb_fourmis):
            color_var = color_f1 if i == 0 else (color_f2 if i == 1 else (color_f3 if i == 2 else color_f4))
            entry_bg = entry_color_cell_1 if i ==0 else (entry_color_cell_2 if i == 1 else (entry_color_cell_3 if i == 2 else entry_color_cell_4))
            color_var.set('red')
            entry_bg.configure(bg="white")
        
        state_radiobtn()
        entry_nb_fourmis.configure(state=NORMAL)
        retry()
        btnok.configure(state= NORMAL)
        
    def limit_entry():
        """ vérifie la valeur de l'Entry, limité à un intervalle de 1 à 4 """

        global nb_fourmis, check
        nb_fourmis = int(entry_nb_fourmis.get())
        check = False

        if nb_fourmis <= 4 and nb_fourmis >0:
            entry_nb_fourmis['bg']='white'
            entry_nb_fourmis.config(state=DISABLED)
            btnok['state'] = DISABLED
            btn_valid['state'] = ACTIVE 
            fourmis_pos(nb_fourmis)
            state_radiobtn()

        else:
            entry_nb_fourmis['bg']='salmon'
            messagebox.showerror('Erreur', "Le nombre de fourmis n'est pas adapté.\nVous pouvez entrer un nombre maximal de 4 fourmis.")
            entry_val.set("")

    def state_radiobtn():
        """ modifie l'état des radioButtons selon le nombre entré dans l'Entry """
        global nb_fourmis, check
        state = DISABLED if check == True else NORMAL
        
        for rb in radiobuttons:
            for i in range(nb_fourmis):
                for entry in entries:
                    
                    if len(radiobuttons) > nb_fourmis:
                            rb[i].config(state=state)
                            entry[i].delete(0, END)
                            entry[i].config(state=state)
                    else:
                        rb[i].config(state=state)
                        entry[i].delete(0, END)
                        entry[i].config(state=state)
                    
    def compteur_label():
        """ compte le nombre de déplacements des fourmis """
        global cpt
        compteur.config(text=str(cpt))
# -----------------------------------------------------------------------------------------------------------------------------------------------
    # développement de la fourmi

    def fourmis_pos(nb):
        """ récupère les positions et les couleurs des fourmis.
        Les positions sont choisies de façon aléatoires dans le canvas, les couleurs sont entrées par l'utilisateur via les RadioButtons """
        global ants, grid
        ants = fourmis(grid, nb)

    def color_fourmi(color, label):
        """ récupere les couleurs des différentes fourmis des RadioButtons """
        ants[label]['color'] = color.get()
    
    def color_entry(color, label):
        """ récupère les couleurs des radioButton avec des entries emet un message d'erreur si la valeur entrée n'est pas une couleur """
        color = entries[0][label].get()

        try: # test si la couleur est correcte
            tk.Label(root, text="", bg=color)
            entries[0][label].config(state=DISABLED)
            ants[label]['color'] = color

        except tk.TclError: # sinon affiche une erreur

            entries[0][label].delete(0, END)
            entries[0][label].config(bg = 'salmon')
            color_var = color_f1 if label == 0 else (color_f2 if label == 1 else (color_f3 if label == 2 else color_f4))
            color_var.set('red')
            messagebox.showerror('Erreur', " Aucune couleur n'a été entré \n Veuillez cliquer sur le RadioButton après avoir entré votre couleur.")

    def ajout_cell(event=None):
        """ ajoute une cellule au canvas à chaque appel"""
        global canvas
        modif_cnv(canvas, grid, color_cell=None)
    
    def dep_fourmi():
        """ permet de déplacer la fourmi et de l'afficher dans le canva """
        global canvas, ants, cpt, after_id, grid
        
        for ant in ants:
            
            posx_fourmi, posy_fourmi = ant['position']
            #print('position : ',posx_fourmi, posy_fourmi)

            set_cell_text(canvas, posx_fourmi, posy_fourmi, ' ')
            
            if get_color_cell(canvas, posx_fourmi, posy_fourmi) == COLORS['bg']:
                set_color_cell(canvas, posx_fourmi, posy_fourmi, ant['color'])
                ant['orientation'] = droite(ant['orientation'])
            else:
                set_color_cell(canvas, posx_fourmi, posy_fourmi, COLORS['bg'])
                ant['orientation'] = gauche(ant['orientation'])

            # position actuelle de la fourmi
            posx_bis, posy_bis = deplacer(grid, ant['orientation'],posx_fourmi, posy_fourmi)

            # définition de la position pour le prochain déplacement
            ant['position'] = posx_bis, posy_bis
            set_cell_text(canvas, posx_bis, posy_bis, '¤')

        cpt +=1
        compteur_label()
        after_id = root.after(scale_speed.get(), dep_fourmi)

    # ------------------- Buttons -------------------

    # valide l'entry
    btnok = tk.Button(lbl_nb_fourmis, width=4, height=2, text='ok', bg='light grey', command = limit_entry, cursor="hand2")
    btnok.grid(row=0, column=2, padx=2, pady=2, sticky=NSEW)

    # lance les fourmis
    startbtn = tk.Button(main_frm, height=4, text='Lancer', bg='grey', command = start, state=DISABLED, cursor="hand2")
    startbtn.grid(row=0, columnspan=2, sticky=NSEW)

    # valide les options et rend accessible le lancer
    btn_valid = tk.Button(main_frm, text = "Valider", command = valider, state=DISABLED, cursor="hand2")
    btn_valid.grid(row=5,columnspan=2, sticky=NSEW)

    # remet à zéro les options entrées
    btn_opt0 = tk.Button(main_frm, text = "Reinitialiser", command = reinitialiser, state=ACTIVE, cursor="hand2")
    btn_opt0.grid(row=6, columnspan=2, sticky=NSEW)

    # arrete le cheminement de la fourmi
    btnstop = tk.Button(main_frm, text = "Stop", command = stop, state=ACTIVE, cursor="hand2")
    btnstop.grid(row=7, columnspan=2, sticky=NSEW)
    
    # ------------------- Commands -------------------

    root.bind('<space>', gestion_barre_espace)
    root.bind('<Control-w>', options)
    root.bind('<Control-z>', reinitialiser)
    root.bind('<Control-q>', quitter)
    root.bind('<Control-c>', commands)
    root.bind('<Control-a>', jeu)
    root.bind('<Control-s>', colors_possibility)
    canvas.bind('<Button-1>', ajout_cell)

    
if __name__ == "__main__":

    # ------------------- variables globales -------------------

    width_grid = 0 # largeur de la grille
    height_grid = 0 # hauteur de la grille
    size_cell = 0 # taille de les cellules
    nb_fourmis = 0 # nombre de fourmis
    cpt = 0 # compteur
    check = False # vérification de l'état des boutons
    after_id = None # modification de l'id du déplacement de la fourmis
    state_window = True # vérification de l'état de la première fenêtre
    

    # choix de l'utilisateur 
    fenetre()

    # vérification si les choix ont été validé
    if state_window == True:

        # modifie l'interface selon les dimensions de la grille
        limit_size_cell()

        # création de la grille et du canvas selon les fonctions initialisées dans les templates
        grid = create_random_grid_lc(width_grid, height_grid, [0,1])
        root = tk.Tk()
        
        canvas = grid_canvas(root, grid, size_cell, margin=10, gutter=2, show_vals=False, outline=False)
        render()
        
        root.mainloop()