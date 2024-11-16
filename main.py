class y:
    def __init__(self,name,maxspeed,turnradius):
        self.name=name
        self.maxspeed=maxspeed
        self.turnradius=turnradius
class x(y):
    pass
BMW=x("BMW x8",234,"Weak")
print("The name is: ",BMW.name)
print("Max speed is: ",BMW.maxspeed) 
print("The turn radius is:",BMW.turnradius)       