#
# Assignment 5
#
# Osmel Savon
#

def printTriangle(n,m):
    'This function is recursive and prints a upside down triangle starting from n. Also using m for indentation of the triangle'
    star = '*'
    space = ' '
    if n <= 0:
        return 0
    else:
        print ((space * m)+(star * n))
        printTriangle(n-2,m+1)

def recSymPrint(sym1,sym2,n,m):
    'This function is recursive and prints an upside down and a rightside up triangle of 2 symbols. Using n as the base and m as the indentation.'
    star = '*'
    space = ' '
    if n <= 0:
        return
    elif sym1 == '' or sym2 == '':
        return
    else:
        print ((space * m)+(sym1 * n))
        recSymPrint(sym1,sym2,n-2,m+1)
        print ((space * m)+(sym2 * n))

        
def recStrCount(lst):
    'This function recursively counts the string items in a list'
    if lst == []:
        return 0
    elif type(lst[0]) == str:
        return 1 + recStrCount(lst[1:])
    else:
        return recStrCount(lst[1:])
    
def recStrMerge(s1,s2):
    'This function merges the each character from each string one by one until it has exhausted all characters in string'
    if s1 == '' and s2 == '':
        return ''
    else:
        return s1[0:1] + s2[0:1] + recStrMerge(s1[1:],s2[1:])

def recListSum(lst):
    'This finction adds all numbers in a list or nested list and returns the total'
    if lst == []:
        return 0
    elif lst[0] == list:
        return recListSum(lst[0]) + recListSum(lst[1:])
    elif type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + recListSum(lst[1:])
    else:
        return recListSum(lst[1:])
