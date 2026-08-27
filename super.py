class Grandfather:
    def __init__(self):
        print("1. Dada ji ka constructor call hua")

class Father(Grandfather):
    def __init__(self):
        super().__init__() # Yeh Dada ji ko call karega
        print("2. Papa ka constructor call hua")

class Son(Father):
    def __init__(self):
        super().__init__() # Yeh Papa ko call karega
        print("3. Bete ka constructor call hua")

# Sirf ek line likhne se teeno call honge
obj = Son()


class Father:
    def __init__(self):
        super().__init__()
        print("Father constructor call hua")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother constructor call hua")

class Child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child constructor call hua")

c = Child()