#CSC 241
#Osmel Savon


def myFile(text, ofile):
#filework
    infile = open(text, 'r')
    hold = infile.read()
    infile.close()
#clean up
    punct = [',','.','\n','—','-']
    for i in punct:
        hold = hold.replace(i, " ")
    hold = hold.lower()
#put in list    
    lst = hold.split()
#hold unique words
    newlst = []
#look at every element in the list
    for i in lst:
        if i not in newlst:
            newlst.append(i)
            newlst.append(lst.count(i))
#write to output word count per line
    ofile = open(ofile, 'a')
    for i in range(0,len(newlst), 2):
        temp = '{} {}\n'.format(newlst[i],newlst[i+1])
        ofile.write(temp)
    ofile.close()

def showDebug():
    lst = ['a','b','c']
    for i in lst:
        print(i)
        
