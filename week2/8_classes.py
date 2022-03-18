# Class is the blueprint of a object
# Defines what attributes the object has and what kind of functionality it provides
# new instances => new objects of the class


# Note camel case
class ClassName:
    att1 = 5
    att2 = "Sam"

    def __init__(self):
        print(5)

    def get_att1(self):
        return self.att1


cls_obj = ClassName()


class ClassName:
    att1 = 5    # class variable, matters when you use vars that passed by pointers

    def __init__(self, at):
        self.att2 = at    # instance variable
        self.a = []
        att1 = 10   # local variable for __init__
        print(att1, "local att1 in the init")
        print(self.att1, "class att1 in the init")

    def get_att1(self):
        return self.att1


cls_obj2 = ClassName(15)
print(cls_obj2.att1)
print(cls_obj2.att2)
print(cls_obj2.get_att1())  # its common to use functions to access obj vars
cls_obj2.a.append("cls_obj2")
print(cls_obj2.a)

cls_obj3 = ClassName(20)
print(cls_obj3.att2)
print(cls_obj3.get_att1())
print(cls_obj3.a)

# show moving it into init


# Inheritance
class ClassName2(ClassName):
    def get_att2(self):
        return self.att2


cls_obj4 = ClassName2(20)
print(cls_obj4.get_att1())
print(cls_obj4.get_att2())


class ClassName3(ClassName):
    def get_att2(self):
        return self.att2 + 1


cls_obj5 = ClassName3(20)
print(cls_obj5.get_att1())
print(cls_obj5.get_att2())


# Overwriting (Polymorphism # common to use the base as abstract)
class ClassName4(ClassName):
    def get_att1(self):
        return self.att1 + 1


cls_obj6 = ClassName4(20)
print(cls_obj6.get_att1())
print(isinstance(cls_obj6, ClassName4))
print(isinstance(cls_obj6, ClassName3))
print(isinstance(cls_obj6, ClassName))

# Remember objects are passed as a pointer


# magic functions
# Defines how basic functions should be done on your object
class ClassName5(ClassName):
    def __str__(self):
        return f"I have {self.att1} and {self.att2}"

    def __lt__(self, other):
        if self.att2 < other.att2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.att2 == other.att2:
            return True
        else:
            return False


cls_obj7 = ClassName5(20)
print(cls_obj7)

cls_obj8 = ClassName5(40)
print(cls_obj7 < cls_obj8)

