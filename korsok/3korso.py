from keres import *

class Korso(Feladat):
    def __init__(self, ke, c): #((8, 0, 0), 4) kezdo touple, cel konkret ertek
        super().__init__(ke, c)
        self.K1=8
        self.K2=5
        self.K3=3

    def celteszt(self, allapot): #(a1, a2, a3) az elso kettoben lehet 4 litert elerni.
        return allapot[0] == 4 or allapot[1] == 4


    def rakovetkezo(self, allapot): #findnext
        lepesek=[]
        a1, a2, a3 = allapot

        if a1>0 and a2 < self.K2:
            m = min(a1, self.K2-a2)
            tmp = (a1-m, a2+m, a3)
            lepesek.append(('1-es korsobol, a 2-es korsoba {} litert'.format(m), tmp))

        if a1 > 0 and a3 < self.K3:
            m = min(a1, self.K3 - a3)
            tmp = (a1 - m, a2, a3 +m)
            lepesek.append(('1-es korsobol, a 3-es korsoba {} litert'.format(m), tmp))

        if a2 > 0 and a3 < self.K3:
            m = min(a2, self.K3 - a3)
            tmp = (a1, a2 - m, a3 + m)
            lepesek.append(('2-es korsobol, a 3-es korsoba {} litert'.format(m), tmp))

        if a2 > 0 and a1 < self.K1:
            m = min(a1, self.K1 - a1)
            tmp = (a1 + m, a2 - m, a3)
            lepesek.append(('2-es korsobol, a 1-es korsoba {} litert'.format(m), tmp))

        if a3 > 0 and a1 < self.K2:
            m = min(a3, self.K1 - a1)
            tmp = (a1 + m, a2, a3 -m)
            lepesek.append(('3-as korsobol, a 1-es korsoba {} litert'.format(m), tmp))

        if a3 > 0 and a2 < self.K2:
            m = min(a3, self.K2 - a2)
            tmp = (a1, a3 -m, a2 + m)
            lepesek.append(('3-as korsobol, a 2-es korsoba {} litert'.format(m), tmp))

        return lepesek

    def __str__(self):
        return 'Korsok {}'.format(self.kezdő)


K = Korso((8, 0 , 0), 4)
print(K)
print(K.celteszt(K.kezdő))
print(K.celteszt((3,4,1)))
print(K.rakovetkezo(K.kezdő))

