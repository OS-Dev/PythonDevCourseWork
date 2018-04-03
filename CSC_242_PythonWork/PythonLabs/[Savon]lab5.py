# Lab 6
#
# Osmel Savon
#

def sublstCount(lst):
    if lst == []: #base case
        return 0
    elif type(lst[0]) == list:
        return 1 + sublstCount(lst[1:]) + sublstCount(lst[0])
    else:
        return 0 + sublstCount(lst[1:])

def itemCount(lst):
    if lst == []: #base case
        return 0
    elif type(lst[0]) == list:
        return 1 + itemCount(lst[1:]) + itemCount(lst[0])
    else:
        return 0 + itemCount(lst[1:]) 
