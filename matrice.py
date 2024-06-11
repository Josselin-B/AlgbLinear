# matrice.py
from vect import vecteur
import numpy as np

class Matrice:
    def __init__(self, vecteurs):
        # Vérifie que tous les éléments sont des instances de Vecteur
        if all(isinstance(v, vecteur) for v in vecteurs):
            self.vecteurs = vecteurs
        else:
            raise ValueError("Tous les éléments doivent être des instances de Vecteur")

    def shape(self):
        return (len(self.vecteurs), len(self.vecteurs[0].elements))

    #def addition(self, autre_matrice):


    #def produit_matrice(self, autre_matrice):


    #def transpose(self):


    def __repr__(self):
        return f"Matrice([\n" + ",\n".join([str(v) for v in self.vecteurs]) + "\n])"