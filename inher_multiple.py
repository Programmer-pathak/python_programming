class Father:
    def height(self):
        print("Height Papa jaisi hai.")

class Mother:
    def intelligence(self):
        print("Dimag Mummy jaisa hai.")

class Child(Father, Mother): # Do parents se inherit kiya
    pass

c = Child()
c.height()       # Father se aaya
c.intelligence() # Mother se aaya