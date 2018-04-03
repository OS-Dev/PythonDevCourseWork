def findSigners(ifile):
    longlist = []
    lst = []
    #filework
    infile = open(ifile, 'r')
    hold = infile.read()
    infile.close()

    #clean up
    punct = [ 'Jr.' ,',', '\n']
    for i in punct:
        hold = hold.replace(i,'')
    lst.append(hold)

        
    return lst
                    
def changeIn(ifile):
    pass
            
                
def printFour(ifile):
    pass
