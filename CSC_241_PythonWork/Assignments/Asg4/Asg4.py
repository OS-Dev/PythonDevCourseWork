# Assignment 4
#
# Osmel Savon
#



### Dont know what else i needed to do here.
def countMembers(ifile):
    results = []
    lst = []
    count = 0
    seven = 0
    eighty = 0
    
    f1 = open(ifile, 'r')
    f2 = f1.read()
    lst = f2.split()
    
    for i in lst:
        if i[0:2] == '60':
            count = count + 1
        elif i[0:2] == '78':
            seven = seven + 1
        elif i[0:2] == '81':
            eighty = eighty + 1
    results.append('60')        
    results.append(count)
    results.append('78')
    results.append(seven)
    results.append('81')
    results.append(eighty)

    f1.close()
        
    return results



# need to take in account for line spacing
def sumWords(ifile,lcount):
    lcount = int(lcount)
    lst = []
    holdlst = []
    count = 0
    
    infile = open(ifile, 'r')

    infile = open(ifile, 'r')
    for i in range(0, lcount):
        hold = infile.readline()
        holdlst = hold.split()
        if holdlst != []:
            for i in holdlst:
                lst.append(i)
                count = count + 1
        else:
            count = -1
        
    infile.close()
    return count

    

def countWord(ifile,s):
    lst = []
    num  = 0
    f1 = open(ifile, 'r')
    hold = f1.readlines()
    counter = 0
    for i in range(0, len(hold)):
        lst.append("Line {}".format(i))        
        count = hold[i].count(str(s))
        lst.append(count)
    f1.close()
    return lst

            
if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
        
    print('countMembers("namenum.txt"): ' + check(countMembers("namenum.txt"),['60', 1, '00', 3, '99', 1, '78', 1, '77', 1]))
    print('countMembers("namenum2.txt"): ' + check(countMembers("namenum2.txt"),['60', 1, '00', 5, '99', 2, '78', 2, '77', 2]))
    print('sumWords("namenum.txt",3)' + check(sumWords("namenum.txt",3),6))
    print('sumWords("namenum.txt",10)' + check(sumWords("namenum.txt",10),-1))
    print('sumWords("gettysburg.txt",5)' + check(sumWords("gettysburg.txt",5),44))
    print('sumWords("gettysburg.txt",25)' + check(sumWords("gettysburg.txt",25),-1))
    print('sumWords("gettysburg.txt",24)' + check(sumWords("gettysburg.txt",24),267))
    print('countWord("namenum2.txt","smith")' + check(countWord("namenum2.txt","smith"),['Line 0', 1, 'Line 1', 0, 'Line 2', 0, 'Line 3', 0, 'Line 4', 0, 'Line 5', 0, 'Line 6', 0, 'Line 7', 0, 'Line 8', 0, 'Line 9', 0, 'Line 10', 0, 'Line 11', 0]))
    print('countWord("namenum.txt","smith")' + check(countWord("namenum.txt","smith"),['Line 0', 1, 'Line 1', 0, 'Line 2', 0, 'Line 3', 0, 'Line 4', 0, 'Line 5', 0, 'Line 6', 0]))
    print('countWord("gettysburg.txt","this")' + check(countWord("gettysburg.txt","this"),['Line 0', 1, 'Line 1', 0, 'Line 2', 0, 'Line 3', 0, 'Line 4', 0, 'Line 5', 0, 'Line 6', 0, 'Line 7', 0, 'Line 8', 0, 'Line 9', 1, 'Line 10', 0, 'Line 11', 0, 'Line 12', 1, 'Line 13', 0, 'Line 14', 0, 'Line 15', 0, 'Line 16', 0, 'Line 17', 0, 'Line 18', 0, 'Line 19', 0, 'Line 20', 0, 'Line 21', 1, 'Line 22', 0, 'Line 23', 0]))
