
#
# Assignment 3
#
# Osmel Savon
#
def calcDist(citydist):
    total = []
    totalm = 0
    count = 0
    for i in range(1,len(citydist),2):
        tot = int(citydist[i])
        totalm = int(tot + totalm)    
    total.append(totalm)
    for i in range(0, len(citydist),2):
        city = citydist[i]
        count = count + 1
        if i > 1 and city == citydist[0]:
            count = count - 1
    total.append(count)
    return total

    
def uniqueLasts(names):
    s = names.split(",")
    s = [i.replace(',' and ' ', "") for i in s]
    uniq = []
    seen = set()
    if names != '':
        for i in s:
            i = i.lower()
            if i not in seen:
                seen.add(i)
                uniq.append(i[:1].upper() + i[1:])
        uniq.sort()
    else:
        uniq = []
    return uniq


def triangleTypes(s):
    angles2 = []
    angles = s.split(";")
    angles = [i.replace(';','') for i in angles]
    if s != '':
        for i in angles:
            i = int(i)
            angles2.append(i)      
            if  max(angles2) > 90:
                ttype = "obtuse"  
            elif max(angles2) == 90:
                ttype = 'right'
            elif max(angles2) == 60:
                ttype = 'equiangular'
            elif max(angles2) < 90:
                ttype = 'acute'
        result = ("The triangle with angles {0}, {1}, and {2} is {3}.".format(angles2[0], angles2[1], angles2[2], ttype))
    else:
        result = ('No angles were given.')
    return result


    
if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
    print("RUNNING CHECK ...")
    print('calcDist(citydist): ' + check(calcDist(["Chicago",90,"Milwaukee",436,"Cleveland",168,"Detroit",614,"New York City"]),[1308,5]))
    print('calcDist(citydist): ' + check(calcDist([]),[0,0]))
    print('calcDist(citydist): ' + check(calcDist(["Chicago",90,"Milwaukee",436,"Cleveland",168,"Detroit",614,"New York City",789,"Chicago"]),[2097,5]))
    print()
    print('uniqueLasts(names): ' + check(uniqueLasts("Domel, domel, SMITH, smitH, PATel, GoMez, gomez, JONAS, JONNAS"),['Domel','Gomez','Jonas','Jonnas','Patel','Smith']))
    print('uniqueLasts(names): ' + check(uniqueLasts(""),[]))
    print('uniqueLasts(names): ' + check(uniqueLasts("SMITH, SMITH, SMITH, smith, smith, smith, smith, SMith"),['Smith']))
    print()
    print('triangleTypes(s): ' + check(triangleTypes("10;70;100"),'The triangle with angles 10, 70, and 100 is obtuse.'))
    print('triangleTypes(s): ' + check(triangleTypes(""),'No angles were given.'))
    print('triangleTypes(s): ' + check(triangleTypes("60;60;60"),'The triangle with angles 60, 60, and 60 is equiangular.'))
    print('triangleTypes(s): ' + check(triangleTypes("90;45;45"),'The triangle with angles 90, 45, and 45 is right.'))
    print('triangleTypes(s): ' + check(triangleTypes("55;55;70"),'The triangle with angles 55, 55, and 70 is acute.'))
