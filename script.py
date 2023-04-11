from tkinter import *

class Grille:
    def __init__(self, taille):
        self.taille = taille
        self.grille = []
        self.bateausurgrille = 0
        for i in range(taille):
            self.grille.append([])
            for j in range(taille):
                case = Canvas(fenetre,width=25,height=25,bg='#1E90FF')
                case.grid(column=i,row=j)
                case.bind("<Button-1>", lambda e,a = i, b =j: self.tir(a, b))
                self.grille[i].append({"case": case, "numero": 0})
            
    def tir(self, x, y):
        if x < 0 or y < 0 or x >= self.taille or y >= self.taille:
            return
        self.grille[x][y]["case"]["bg"] = "red"
    
    def est_vide(self):
        return self.bateausurgrille == 0
    
    def est_remplie(self):
        return self.bateausurgrille == 5
        
    def placement(self, x, y, bateau):
        pass
        
    
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
        
    def start(self):
        pass
        
fenetre = Tk()
fenetre.geometry("1080x700")
g = Grille(10)

fenetre.mainloop()