import numpy as np

class vecteur:
    def __init__(self, elements):
        self.elements = np.array(elements)

    def norme(self):
        return np.linalg.norm(self.elements)

    def addition(self, autre_vecteur):
        return vecteur(self.elements + autre_vecteur.elements)

    def multiplication(self, autre_vecteur):
        return vecteur(self.elements * autre_vecteur.elements)

    def produit_scalaire(self, autre_vecteur):
        return np.dot(self.elements, autre_vecteur.elements)

    def __repr__(self):
        return f"Vecteur({self.elements})"

    def dimension(self):
        return len(self.elements)

v1 = vecteur([1,2,3])
v2 = vecteur([2,3,4])
print(v1.__repr__())
v1=v1.addition(v2)
print(v1.__repr__())
v2=v2.multiplication(vecteur([2,2,2]))
print(v2.dimension())