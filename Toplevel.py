from tkinter import *
from tkinter import PhotoImage

# ----------------- Globales -----------------
options_ouvert = False
commands_ouvert = False
jeu_ouvert = False
colorsposs_ouvert = False

# ----------------- MenuBar -----------------
def options(event=None):
    """ énumère l'ensemble des options disponibles dans l'interface via un TopLevel"""
    global options_ouvert

    def fermer_toplevel():
        """ permet d'ouvrir seulement une fois le topLevel et de le fermer"""
        global options_ouvert
        options_ouvert = False
        info.destroy()

    if not options_ouvert :
        options_ouvert = True

        info = Toplevel()
        info.title("Options : Langton")

        # dimensions
        window_x = 650
        window_y = 350

        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)
        info.resizable(False,False)

        multiline_text =  """
        - Nombre de fourmis :\n
            Vous pouvez insérer dans l'entry un nombre de fourmi entre 1 et 4.
            Pour valider le nombre, il vous suffit de cliquer sur le bouton 'ok'.\n
        - Couleurs des fourmis :\n
            Une fois le nombre de fourmis entrés, vous pouvez choisir les couleurs des fourmis avec les RadioButtons;
            Si vous souhaitez entrer une couleur autre que celles proposées une entry est disponible.\n
        - Vitesse des fourmis :\n
            Vous pouvez modifier la vitesse des fourmis de l'interface à n'importe quel moment.\n
        - Boutons :\n
            'Valider' : valide l'ensemble des caractéristiques entrées au préalable ;
            'Lancer' : lance le développement de la fourmi dans l'interface ou relance après un arrêt ;
            'Reinitialiser' : remet à zéro les options et le développement des fourmis ;
            'stop' : permet d'arrêter la boucle de façon temporaire. \n
        - Canvas :\n
            Vous avez la possibilité de modifier le canvas et ainsi les déplacements des fourmis en appuyant
            sur le clic gauche de votre souris sur le canva.
            Vous pouvez savoir que vous avez le focus sur le canva lorsque votre curseur sera en forme de cible. """
        scrollbar = Scrollbar(info, orient='vertical')
        scrollbar.pack(side="right", fill=Y)
        canvas=Canvas(info, yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        # Labels

        Label(frame, text = "Présentation des différentes options de l'interface :", anchor='nw', justify = 'left' ).pack(padx = 5, pady = 5)
        Label(frame, text = multiline_text, anchor = 'w', justify = 'left').pack()

        frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
        
        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        info.protocol("WM_DELETE_WINDOW",fermer_toplevel)
        info.mainloop()

def commands(event=None):
    """ énumère l'enssemble des commandes disponibles dans l'interface via un TopLevel """
    global commands_ouvert

    def fermer_toplevel():
        """ permet d'ouvrir seulement une fois le topLevel et de le fermer"""
        global commands_ouvert
        commands_ouvert = False
        info.destroy()

    if not commands_ouvert :
        commands_ouvert = True

        info = Toplevel()
        info.title("Comandes : Langton")

        # dimensions
        window_x = 650
        window_y = 300

        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        info.resizable(False, False)

        multiline_text =  """ 
        - 'barre espace' : lancer et stoper le/les déplacements des fourmis ;\n
        - 'Ctrl-Z' : associé au bouton réinitialiser ;\n
        - 'Ctrl-Q' : associé à la commande quitter ;\n
        - 'Ctrl-A' : lance le menu Jeu ;\n
        - 'Ctrl-W' : lance le menu Options ;\n
        - 'Ctrl-C' : lance le menu Commandes ;\n
        - 'Ctrl-S' : lance le menu Couleurs."""

        # Labels
        Label(info, text = "Présentation des différentes commandes de l'interface :", anchor='center' ).pack(padx = 5, pady = 5)
        Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))

        info.protocol("WM_DELETE_WINDOW",fermer_toplevel)
        info.mainloop()

def jeu(event=None):
    """ explique le concept de l'automate cellulaire via un TopLevel"""
    global jeu_ouvert

    def fermer_toplevel():
        """ permet d'ouvrir seulement une fois le topLevel et de le fermer"""
        global jeu_ouvert
        jeu_ouvert = False
        info.destroy()
    
    if not jeu_ouvert:
        jeu_ouvert = True

        info = Toplevel()
        info.title("Jeu : Langton")

        # dimensions
        window_x = 650
        window_y = 400

        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)

        info.resizable(False, False)

        multiline_text =  """ La fourmi de Langton ou Automate cellulaire de Langton est un modèle d'automate cellulaire\n représentant un comportement émergent, où des motifs (ici, des cellules) évoluent à partir de règles simples.\n
            - Une position initiale : initialisé de façon aléatoire dans la grille.\n
            - Une direction initiale : initialisé vers le nord mais modifié après chaque déplacement.\n
            - Des règles de déplacement, basées sur la couleur de la cellule sur laquelle elle se trouve :\n
                -> Si la cellule sous la fourmi est blanche, elle change la couleur de la cellule en la couleur de la fourmi,\n
                la fourmi s'oriente vers la droite et avance.\n
                -> Si la cellule sous la fourmi est de couleur, elle change la couleur de la cellule en blanc,\n
                la fourmi s'oriente à gauche et avance.\n
            A partir d'un certain temps, la fourmi génère des motifs complexes comme des Autoroutes,
            un escalier ou encore un pont. """
        
        # Labels
        Label(info, text = "Présentation de la fourmi de Langton", anchor='center' ).pack(padx = 5, pady = 5)
        Label(info, text = multiline_text, anchor = 'nw', justify = 'left').pack(padx = 5, pady = 5)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))
        info.protocol("WM_DELETE_WINDOW",fermer_toplevel)
        info.mainloop()

def colors_possibility(event=None):
    """ affiche les couleurs disponibles dans tkinter par un TopLevel"""
    global colorsposs_ouvert

    def fermer_toplevel():
        """ permet d'ouvrir seulement une fois le topLevel et de le fermer"""
        global colorsposs_ouvert
        colorsposs_ouvert = False
        info.destroy()
    
    if not colorsposs_ouvert:
        colorsposs_ouvert = True

        info = Toplevel()
        info.title("Couleurs")

        # dimensions
        window_x = 600
        window_y = 630

        x0 = (info.winfo_screenwidth()/2) - (window_x/2)
        y0 = (info.winfo_screenheight()/2) - (window_y/2)
        info.resizable(False, False)

        info.geometry('%dx%d+%d+%d' % (window_x, window_y, x0, y0))

        # Label
        Label(info, text= 'Possibilités de couleurs').grid(row=0, padx=5, pady=5)
        
        # Canva
        img = PhotoImage(file= 'colors.png') # image du canva

        cnv = Canvas(info, width=600,height= 600,bg= 'white' )
        cnv.create_image(0,0, image = img, anchor = NW)
        cnv.grid(row=1,column=0)

        info.protocol("WM_DELETE_WINDOW",fermer_toplevel)
        info.mainloop()
    