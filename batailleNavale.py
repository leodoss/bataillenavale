from tkinter import *
from random import *

class Grille:
    def __init__(self, x, y, taille):
        """ Int, int, int -> None
        Crée et dessine une grille de dimension taille x taille, 
        dont la case en haut à gauche est de coordonnées (x, y) dans la fenêtre
        """
        self.taille = taille
        self.grille = []
        self.atire = False
        self.ready = False
        self.bateausurgrille = 0
        self.bateaux = {1: Bateau(2,1,1), 2: Bateau(2,1,2), 3: Bateau(4,2,3), 4: Bateau(1,3,4), 5: Bateau(1,3,5)}
        self.couleur_associee = {1: "green", 2: "white", 3: "black", 4: "orange", 5: "pink"}
        for i in range(taille):
            self.grille.append([])
            for j in range(taille):
                case = Canvas(fenetre, width=25, height=25, bg="#1E90FF", highlightbackground="white")
                case.grid(column=j+x,row=i+y)
                self.grille[i].append({"case": case, "numero": 0})
    
    def active_tir(self):
        """ None -> None
        Active l'appel de la méthode tir lors d'un clic gauche sur une case
        """
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].bind("<Button-1>", lambda e, a = i, b = j: self.tir(a, b))
        self.atire = False
          
    def desactive_tir(self):
        """ None -> None 
        Désactive l'appel de la méthode tir lors d'un clic gauche sur une case
        """
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].unbind("<Button-1>")
        self.atire = True

    def active_placer(self, bateau, couleur):
        """ Bateau -> None
        Active l'appel de la méthode placer lors d'un clic gauche sur une case
        """
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].bind("<Button-1>", lambda e, a = i, b = j, c = bateau, d = couleur: self.placer(a, b, c, d))

    def desactive_placer(self):
        """ None -> None 
        Désactive l'appel de la méthode placer lors d'un clic gauche sur une case
        """
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].unbind("<Button-1>")

    def placer(self, i, j, bateau, couleur):
        """ Int, int, Bateau, str -> Bool
        Place si possible le bateau sur la grille à partir de la case de 
        coordonnées (i, j), qui correspond à la case en haut à gauche
        du bateau (les cases correspondant au bateau sont coloriées en gris) et
        renvoie True, sinon False
        """
        
        long_b = bateau.longueur
        larg_b = bateau.largeur

        # Vérifie que le bateau ne dépasse pas de la grille
        if i+long_b-1 < self.taille and j+larg_b-1 < self.taille:
            # Vérifie que le bateau ne chevauche pas des cases non vides
            for i_boucle in range(i+long_b-1, i-1, -1):
                for j_boucle in range(j, j+larg_b):
                    if not self.case_est_vide(i_boucle, j_boucle):
                        return False
                      
            for i_boucle in range(i+long_b-1, i-1, -1):
                for j_boucle in range(j, j+larg_b):
                    self.grille[i_boucle][j_boucle]["numero"] = bateau.numero
                    self.grille[i_boucle][j_boucle]["case"]["bg"] = couleur
            
            self.bateausurgrille += 1
            if self.est_remplie():
                self.ready = True
                self.desactive_placer()
            else:
                self.active_placer(self.bateaux[self.bateausurgrille+1], self.couleur_associee[self.bateausurgrille+1])
            return True
        else:
            return False
          
    def tir(self, i, j):
        """ Int, int -> None
        Change le numéro de la case de coordonées (i, j) en -1 (pour indiquer qu'elle a subi un tir)
        """
        if self.grille[i][j]["numero"] != -1:
            self.grille[i][j]["case"]["bg"] = "red" if self.grille[i][j]["numero"] == 0 else "grey"
            self.grille[i][j]["numero"] = -1
            self.atire = True
            return True
        return False
    
    def grille_est_vide(self):
        """ None -> Bool 
        Renvoie True si la grille est vide, sinon False
        """
        for i in range(len(self.grille)):
            for j in range(len(self.grille)):
                if self.grille[i][j]["numero"] > 0:
                    return False
        return True
    
    def est_remplie(self):
        """ None -> Bool
        Renvoie True si la grille contient 5 bateaux,
        sinon False
        """
        return self.bateausurgrille == 5

    def case_est_vide(self, i, j):
        """" Int, int -> Bool
        Renvoie True si la case est vide (on a décidé que le numéro associé à une case vide est 0), sinon False
        """
        return self.grille[i][j]["numero"] == 0
        
class Bateau:
    def __init__(self, longueur, largeur, numero):
        """ Int, int, int -> None
        Crée un bateau de taille largeur x longueur et lui associe
        un numéro unique
        """
        self.longueur = longueur
        self.largeur = largeur
        self.numero = numero
        
class Jeu:
    def __init__(self, Grille1, Grille2):
        """ Grille, Grille -> None
        """
        self.bateaux = {1: Bateau(2, 1, 1), 2: Bateau(2, 1, 2), 3: Bateau(4, 2, 3), 4: Bateau(1, 3, 4), 5: Bateau(1, 3, 5)}
        self.grille1 = Grille1
        self.grille2 = Grille2
        self.grille1.active_placer(self.bateaux[1], "blue")
        self.placement_automatique()

    def jeu(self):
        """ None -> None
        Prend en charge le déroulement du jeu
        """
        if not self.grille2.atire:
            if self.grille1.ready:
                self.grille2.active_tir()
            fenetre.after(500, self.jeu)
        else:
            self.grille2.desactive_tir()
            if self.grille2.grille_est_vide():
                print("Joueur 1 a gagné")
                return
            self.tir_automatique(self.grille1)
            if self.grille1.grille_est_vide():
                print("Ordinateur a gagné !")
                return
            self.grille2.active_tir()
            fenetre.after(200, self.jeu)
  
    def placement_automatique(self):
        """ None -> None
        Place automatiquement les bateaux de l'ordinateur
        """
        for i in range(1, 6):
            est_place = self.grille2.placer(randint(0, self.grille2.taille-1),randint(0, self.grille2.taille-1),self.bateaux[i], "#1E90FF")
            while not est_place:
                est_place = self.grille2.placer(randint(0, self.grille2.taille-1),randint(0, self.grille2.taille-1),self.bateaux[i], "#1E90FF")

    def tir_automatique(self, g):
        """ Grille -> None
        Tir automatiquement dans la grille du joueur
        """
        while True:
            if g.tir(randint(0, g.taille-1), randint(0, g.taille-1)):
                break
      
fenetre = Tk()
fenetre.geometry("1080x700")
fenetre.configure(background='white')

g1 = Grille(0, 0, 10)
separateur = Canvas(fenetre, width=25, height=25, bg="white", highlightbackground="white") # pour que les deux grilles ne soient pas collées
separateur.grid(column=0, row=11)
g2 = Grille(0, 12, 10)

game = Jeu(g1, g2)
game.jeu()

fenetre.mainloop()
