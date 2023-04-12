from tkinter import *

class Grille:
    def __init__(self, x, y, taille):
        self.taille = taille
        self.grille = []
        self.bateausurgrille = 0
        for i in range(taille):
            self.grille.append([])
            for j in range(taille):
                case = Canvas(fenetre, width=25, height=25, bg="#1E90FF", highlightbackground="white")
                case.grid(column=i+x,row=j+y)
                self.grille[i].append({"case": case, "numero": 0})
    
    def peut_tirer(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].bind("<Button-1>", lambda e,a = i, b =j: self.tir(a, b))
                
    def peut_pas_tirer(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].unbind("<Button-1>")
                                                 
    def tir(self, x, y):
        self.grille[x][y]["case"]["bg"] = "red"
    
    def est_vide(self):
        return self.bateausurgrille == 0
    
    def est_remplie(self):
        return self.bateausurgrille == 5
    
    def peut_placer(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].bind("<Button-2>", lambda e,a = i, b =j: self.placement(a, b))
                
    def peut_pas_placer(self):
        for i in range(self.taille):
            for j in range(self.taille):
                self.grille[i][j]['case'].unbind("<Button-2>")
        
    
class Bateau:
    def __init__(self, longueur, largeur, numero):
        self.longueur = longueur
        self.largeur = largeur
        self.numero = numero
        
class Jeu:
    def __init__(self, Grille1, Grille2):
        self.bateaux = {1: Bateau(2,1,1), 2: Bateau(2,1,2), 3: Bateau(4,2,3), 4: Bateau(1,3,4), 5: Bateau(1,3,5)}
        self.grille1 = Grille1
        self.grille2 = Grille2
        
    def placement(self, Grille):
        i = 0
        while not Grille.est_rempli():
            bateau_courant = self.bateau[i]
            
    
    def placement_aux(self):
        pass
            
            
        
    def start(self):
        pass
        
fenetre = Tk()
fenetre.geometry("1080x700")
fenetre.configure(background='white')

g1 = Grille(0, 0, 10)
g1.peut_tirer()
separateur = Canvas(fenetre, width=25, height=25, bg="white", highlightbackground="white")
separateur.grid(column=0, row=11)
g2 = Grille(0, 12, 10)

fenetre.mainloop()
