
# Lab 2
# Osmel Savon

def computeTotal():

    p = float(input ("Enter Price (> 0): "))
    q = int(input ("Enter quantity: "))
    if p >= 0 and q >= 0:
        total = p * q
        float(round(total, 2))
        print ("$",total)

def printSeqs():
    for i in range(0,76, 25):
        print(i, end = " ")
    print()

    for i in range(21, 76, 3):
        print(i, end = " ")
    print()

    for i in range(-10, 1 , 2):
        print(i, end = " ")

