class Person:
    value = 100
    def __init__(self):
        print "parent constructor"

    def parentMethod(self):
        print "calling parent method"

    def setAttr(self, attr):
        Person.value = attr

    def getAttr(self):
        print "person code:", Person.value

class Male(Person):
    def __init__(self):
        print "calling subclass male constructor"

    def malemethod(self):
        print "calling subclass method"

class Female(Person):
    def __init__(self):
        print "calling subclass female constructor"

    def femalemethod(self):
        print "calling subclass method"

m = Male()
m.malemethod()
m.parentMethod()
m.setAttr(200)
m.getAttr()

f = Female()
f.femalemethod()
f.parentMethod()
f.setAttr(200)
f.getAttr()
