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

    def addition(self, autre_matrice):
        result = [self.vecteurs[i].addition(autre_matrice.vecteurs[i]) for i in range(len(self.vecteurs))]
        return Matrice(result)

    #def produit_matrice(self, autre_matrice):


    #def transpose(self):


    def __repr__(self):
        return f"Matrice([\n" + ",\n".join([str(v) for v in self.vecteurs]) + "\n])"

vec1 = vecteur([1, 2])
vec2 = vecteur([3, 4])
vec3 = vecteur([5, 6])
vec4 = vecteur([7, 8])

mat1 = Matrice([vec1, vec2])
mat2 = Matrice([vec2, vec3])
print(mat1)
print(mat2)
print(mat1.addition(mat2))