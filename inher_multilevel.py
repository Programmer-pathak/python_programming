class Grandfather:
    def land(self):
        print("Dada ji ki zameen.")

class Father(Grandfather):
    def business(self):
        print("Papa ka business.")

class Son(Father):
    def startup(self):
        print("Bete ka startup.")

s = Son()
s.land()     # Dada ji se mila
s.business() # Papa se mila
s.startup()  # Khud ka hai