
'''unlike c++ class we need to give values
to variables mentioned in class also 
here in any method used inside class first
argument self is automatically passed and self
is the reference of the object for which
the method is being called'''
'''Now we will mention all the variables inside
constructor call whose value we want to pass from
constuctor call at time of object creation and others
normally with some dummy value inside class'''

class employee:
    height=None

    #following is how we define a constructor
    def __init__(self,name,salary,blood_grp):
        self.name=name
        self.salary=salary
        self.blood_grp= blood_grp

    def getsal(self):
        return self.salary
    
    def bloodgrp(self):
        return self.blood_grp

    def name_print(self):
        return self.name


a = employee("Vasuuuur",100000000001,"O+")

print(a.name_print())
print(a.getsal())
print(a.bloodgrp())
print(a.height)
a.height=7
print(a.height)
a.name="Vasu"
print(a.name)