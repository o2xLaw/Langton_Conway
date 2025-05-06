- Présentation du programme -

L'objectif de notre programme est de permettre à l'utilisateur d'avoir la possibilité d'intéragir avec l'interface de manière ludique.
A la fois avec les automates, mais aussi avec les différentes options de tkinter.
Ainsi, nous avons essayé de mettre en valeur la bibliothèque tkinter avec les différents automates, tout en respectant au mieux les templates imposés.

Plusieurs fichiers sont présents dans le programme, afin de faciliter la compréhension du code et séparer les fonctions appelées continuellements ou nécéssaires 
à l'interface et les autres utilisées occasionnellements.

Comme différents fichiers nous avons : 

A_lancer.py : utilisant la bibliothèque customtkinter qui rend l'interface tkinter plus moderne et propose à l'utilisateur les différents automates auquel il peut jouer.

Interface_Lanton.py et Interface_Conway.py : lancent respectivement les jeux de la vie de Langton et de Conway, utilisent la bibliothèque tkinter pour Langton
et customtkinter pour Conway. L'idée est d'avoir un visuel différent entre les deux jeux.

Toplevel.py et Ants.py : utilisés seulement pour Interface_Lanton,
    Toplevel.py répertorie l'ensemble des Toplevels appelées par les options dans le Menu.
    Ants.py répertorie les fonctions de déplacements de la ou des fourmis.

grid_manager_template.py et grid_tk_template.py : les templates imposés, quel que peu modifiés pour faciliter la création du code
    ou des fonctions ajoutées tel que get_pos() ou neighbour() dans grid_manager_template.
    De même pour modif_cnv() dans grid_tk_template.

    --------- Manuel d'utilisation --------- 

Installez customtkinter: pip install customtkinter dans votre terminal.
Si vous ne souhaitez pas installer customtkinter, le lancement du jeu de Langton se fera directement dans Interface_Lanton.
Etant donné que le jeu de Conway est exclusivement en customtkinter.

Lancement de Jeu : A_lancer.py 

Choix entre les jeux Conway et Langton via des Buttons, lance automatiquement le jeu choisi et donc son fichier avec subprocess.

- Proposition de modifier les dimensions de la grille et la couleur du Canva.
    Les dimensions via des Scales
    Le Canva par le bouton Pick Color : lorsque vous avez l'affichage de la méthoe askcolor faites attention à ce que sur la scale de droite
                    le curseur ne reste pas sur le blanc, sinon vous pouvez entrer les couleurs de base.
    
    Appuyez sur Valider pour lancer le programme.


----- Interface_Lanton.py ------

Si vous avez appuyé sur le boutton Langton.

Le programme lance une fenetre d'une dimension adapté selon les dimensions de la grille entrées au préalable, avec un Canva sur la gauche et une Frame à droite
rempli de plusieurs options disponibles, des Buttons, Entries, RadioButtons, Scale.

Pour jouer: 

1 - Entrez un nombre de fourmis dans l'entry proposée et validez avec le boutton "ok" placé à droite. 
    Cela vous propose ainsi les RadioButtons/entries selon le nombre de fourmis entrées, et vous pouvez donc choisir les couleurs des fourmis.

2 - Choisir les couleurs
    Une fois certain de vos couleurs vous pouvez les valider avec le boutton "Valider", si vous n'êtes pas certain le button "Réinitialiser" reste disponible
        pour modifier vos couleur ou encore faire repartir de zéro l'interface.

3 - Validez les options choisies
    Le boutton "Lancer" devient disponible

4 - Appuyez sur "Lancer" 
    L'interface se met en route.

Un compteur est présent afin de suivre le nombre de mouvements de la fourmi ou des fourmis.

Une Scale est présente et disponible tout le long du processus, afin de pouvoir modifier la vitesse des fourmis à n'importe quel moment.

Un bouton "Stop" est disponible pour pouvoir arrêter les fourmis.

Vous pouvez aussi modifier le canva/grille en appuyant sur clique gauche sur le canvas, ainsi cela ajoutera des cellules noires qui modifiera le déplacement des fourmis.

Ce manuel d'utilisation est disponible tout le long du jeu dans le Menu "Options"

D'autres commandes sont accessibles dans le MenuBar pour rendre plus accéssible l'interface, comme "Commandes" qui énumère l'ensemble des raccourcis 
disponible associés aux différents boutons.
Ou encore, "Couleurs" qui affiche les couleurs possibles pour vos fourmis.
Ces différents menus sont affichés en tant que TopLevel donc vous pouvez les avoir en même temps que l'interface principale.

Des messagesbox sont implémentées un peu partout dans le code en cas d'erreur de l'utilisateur ou pour quitter le programme.

----- Interface_Conway.py ------

Si vous avez appuyé sur le bouton Conway.

3 boutons sont disponibles, "Lancer", "Rejouer", et "Quitter".

L'interface graphique se lancera en appuyant sur le bouton "Lancer".

Vous souhaitez créer un nouveau jeu de conway, "Rejouer" lancera une nouvelle grille aléatoire, appuyez sur "Lancer" pour lancer la nouvelle grille.

"Quitter" vous permettra de quitter la fenêtre.

----- Répartition du travail ------

Les fichiers principaux des interfaces et A_lancer ont été faits par Aude Bernier.
Les fichiers Ants, TopLevel ont été fait par Yuzwal Michel.
Les templates imposés ont été modifiés en groupe.








