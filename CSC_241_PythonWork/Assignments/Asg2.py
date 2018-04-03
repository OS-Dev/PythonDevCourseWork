#
#
# Assignment 2
# Osmel Savon (Ozzy)
#
# Put your name and the name of each person who worked on this solution.
# Include the role each person played.
# Emmaline Kelly
# This file MUST BE NAMED [your last name]Asg2.ps
#
#
def checkID(id, validIDs):
    validIDs = ['smith02','patel99','johnson75','philmore112','mcnaughton7']
    loc = -1
    for i in range(0,5):
        if validIDs[i] == id.lower():
            loc = i
    return loc


    
def colorNumbers(l):
    n = []
    b = "blue"
    r = "red"
    y = "yellow"
    
    for i in range(0,len(l)):
        if l[i].lower() == b:
            n.append(0)
        elif l[i].lower() == r:
            n.append(1)
        elif l[i].lower() == y:
            n.append(2)
        else:
            n.append(3)
    n.append(-1)
    return n


    
            
def simpleSizeCheck(s,max):
    s = float(len(s))
    an = False
    if s > max:
        an = True
    return an    
            


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
        
    validIDs=['smith02','patel99','johnson75','philmore112','mcnaughton7']
    print('checkID("philMORE112",validIDs"): ' + check(checkID("philMORE112",validIDs),3))
    print('checkID("ferrell20",validIDs"): ' + check(checkID("farrell20",validIDs),-1))
    print('checkID("mCnaughTON7",validIDs"): ' + check(checkID("mCnaughTON7",validIDs),4))
    print('checkID("smith02",validIDs"): ' + check(checkID("smith02",validIDs),0))
    print('checkID("",validIDs"): ' + check(checkID("",validIDs),-1))
    l=["blue","red","Yellow","green","purple","BLUE","green"]
    print('colorNumbers(["blue","red","Yellow","green","purple","BLUE","green"]): ' + check(colorNumbers(l),[0, 1, 2, 3, 3, 0, 3, -1]))
    l=["green","GREEN"]
    print('colorNumbers(["green","GREEN"]): ' + check(colorNumbers(l),[ 3, 3, -1]))
    l=[]
    print('colorNumbers([]): ' + check(colorNumbers(l),[-1]))
    print('simpleSizeCheck("DPU",2): ' + check(simpleSizeCheck("DPU",2),True))
    print('simpleSizeCheck("Hello World!",7): ' + check(simpleSizeCheck("Hello World!",20),False))
    print('simpleSizeCheck("",0): ' + check(simpleSizeCheck("",0),False))
