# Base Class
class Father:
    def property(self):
        print("Father's Property")

    def business(self):
        print("Father's Business")


# Hierarchical Inheritance (Son inherits from Father)
class Son(Father):
    def study(self):
        print("Son loves to study")


# Hierarchical Inheritance (Daughter inherits from Father)
class Daughter(Father):
    def dance(self):
        print("Daughter loves to dance")


# Multiple Inheritance (GrandChild inherits from both Son and Daughter)
class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild loves gaming")


# Creating object of GrandChild
child_obj = GrandChild()

# Calling ALL methods using the GrandChild object
print("GrandChild accessing all methods")
child_obj.property()  # From Father
child_obj.business()  # From Father
child_obj.study()  # From Son
child_obj.dance()  # From Daughter
child_obj.gaming()  # From GrandChild
