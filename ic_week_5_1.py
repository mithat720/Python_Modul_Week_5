class Rectangle:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.oppervlakte = self.breedte * self.hoogte
        self.omtrek = 2 * (self.breedte + self.hoogte)
   
    #def oppervlakte(self):
    #    return self.breedte * self.hoogte
    #def omtrek(self):
    #    return 2*(self.breedte+self.hoogte)

r=Rectangle(5, 7)
r.breedte = 25

#print("Alanı", r.oppervlakte())
#print("Çevresi", r.omtrek())

print(r.oppervlakte)
print(r.omtrek)