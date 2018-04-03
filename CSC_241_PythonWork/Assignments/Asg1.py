


# Osmel Savon
# Assignment 1
# 9/9/16


def nameYr():
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    year = input("In which year were you born? ")
    print (first[0:1] + "." + last[0:1] + ". " + year[2:4])



def calcPerc():

    score = input ("Enter your test score:")
    maxpts = input ("Enter max points possible:")
    product = 100 * float(score)/float(maxpts)
    print("{0:.2f}".format(product) + "%")
    


def addLElements():
    l1 = [0,1,2,3,4,5]
    l2 = [100,101,102,103,104]
    position =  int(input ("Enter position:"))
    total = l1[position] + l2[position]
    print ("The total at ",  position, " is", total)
