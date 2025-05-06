import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

def choose_game():
    root = ctk.CTk()
    root.title('Jeu de la vie')
    

    root.resizable(False,False)
    width = 350
    height = 200

    # Récupère la largeur et la hauteur de l'écran
    ws = root.winfo_screenwidth() # largeur
    hs = root.winfo_screenheight() # hauteur

    x0 = (ws/2) - (width/2)
    y0 = (hs/2) - (height/2)

    # placement de la fenetre
    root.geometry('%dx%d+%d+%d' % (width,height,x0,y0))

    # ----------------- Frame -----------------
    frm = ctk.CTkFrame(root, width=width, height=height)
    frm.pack(fill='both', expand='True', padx=0, pady=0)

    # ----------------- Labels -----------------
    main_label = ctk.CTkLabel(frm, text = 'A quel jeu voulez-vous jouer ?', font= ('bodiny', 20), justify='center', anchor= 'n')
    main_label.pack( padx = 30, pady=10)

    def langton():
        root.destroy()
        subprocess.run(['python', 'Interface_Langton.py'])
        
    def conway():
        root.destroy()
        subprocess.run(['python', 'Interface_Conway.py'])
        
    
    btn_conway = ctk.CTkButton(frm, text="Conway", state='normal', command=conway)
    btn_conway.pack( padx=20, pady=15)

    btn_langton = ctk.CTkButton(frm, text = "Langton", state='normal', command=langton)
    btn_langton.pack(padx=20, pady=15)
    
    root.mainloop()

if "__main__" ==__name__:
    choose_game()









