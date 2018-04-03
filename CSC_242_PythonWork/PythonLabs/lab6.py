
# Osmel Savon
# Lab 6

if __name__=='__main__':
    import doctest
    print( doctest.testfile('Lab6TEST.py') )
    
    

    
def depthCount(lst):                            
    var=0
    if len(lst)!= 0:
        if type(lst[0])==list:
            var += 1
            var = var+depthCount(lst[0])
        if depthCount(lst[1:])> var:
            var = depthCount(lst[1:])
    return var

def recFloatCount(lst):
    if lst == []:
        return 0
    elif type(lst[0]) == list:
        return recFloatCount(lst[1:]) + recFloatCount(lst[0])
    elif type(lst[0]) == float:
        return 1 + recFloatCount(lst[1:])
    else:
        return recFloatCount(lst[1:])
