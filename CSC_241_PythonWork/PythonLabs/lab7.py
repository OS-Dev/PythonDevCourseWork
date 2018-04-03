# CSC 241-404
# Lab 8 
# Osmel Savon

# Question 1
def intersect(lst1, lst2):
    'This program goes through two list to find the unique numbers and tells you how many unique number there are.'
    same = []
    for i in lst1:
        if i in lst2:
            same.append(i)
                
    print (same)

# Question 2
def pairSum(lst, n):
    'This program goes through one lst to find out what list items add up to n. Then prints out there corresponding indices.'
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == n:
                print (i,j)
            
            
        
