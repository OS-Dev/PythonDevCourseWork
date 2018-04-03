# CSC 241
# Lab 3

# Osmel Savon


# Problem 1
def printInitials():
    first = input('Please enter your first name: ')
    last = input('Please enter your last name: ')
    print ('The intials for that name are: {0}.{1}.'.format(first.upper()[0:1],last.upper()[0:1]))

# Problem 2
def avgLst():

    string = eval(input ('Please enter a list: '))
    if string == []:
        return 0.0   
    return sum(string) / len(string)

        



