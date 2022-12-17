


class HitungLuas:

    def stop():
        s = str(input("press [Y/n], n to stop : "))
        if s == "n":
            return True
        return False

    # PERSEGI  
    def setPersegi(self, P, L):
        self.p = P
        self.l = L
    
    def getLuasPersegi(self):
        luas =  float(self.p) * float(self.l)
        return luas

    # SEGITIGA
    def setSegitiga(self, A, T):
        self.a = A
        self.t = T
    
    def getLuasSegitiga(self):
        i = 0.5
        luas = float(self.a) * float(self.t)
        return i * luas
    
    # LINGKARAN
    def setLingkaran(self, J):
        self.jari_jari = J
    def getLuasLingkaran(self):
        phi = 3.14
        luas = phi * float(self.jari_jari) * float(self.jari_jari)
        return luas
    
    

