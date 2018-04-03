# CSC242
# Assignment 1
#
# Osmel Savon - Ozzy
#

def makeString(s):
    'This function takes a string as a parameter and returns the string  produced by concatenating all the non- digits that appear in the string.'
    string = ''
    num = ['0','1','2','3','4','5','6','7','8','9']
    for ch in s:
        if ch in num:
            string = string 
        else:
            string = string + ch
    if string == '':
        results = 0
    else:
        results = string
    return results

def returnTwoSmallest():
    'This function returns a list of the two smallest values(in increasing order) entered  by the user.'
    lst = []
    results = []
    done = False
    while not done:
        num = int(input('Enter number: '))
        if num <= 0:
            done = True
        else:
            lst.append(num)
    lst.sort()
    try:
        results.append(lst[0])
        results.append(lst[1])
    except:
        results = lst
    return results

def payroll(infile):
    ' function  reads the input  file  line  by line,   computing  the total pay (i.e. the product of the hours times the pay_rate) and appending each amount to a list. Ending by returning the list of the amounts.'
    lst = []
    ifile = open(infile)
    for i in ifile:
        split = i.split()
        for i in range(len(split)):
            split[i] = float(split[i])
        ans = float(split[0] * split[1])
        lst.append(ans)
    return lst


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"

print ('makeString("a1b2c3d4"): ' + check(makeString("a1b2c3d4"),'abcd'))
print ('makeString("1234"): ' + check(makeString("1234"),0))
print ('makeString(""): ' + check(makeString(""),0))
print ('makeString("abc"): ' + check(makeString("abc"),'abc'))

print('Enter 3 then 2 then 1 then -1')
print ('returnTwoSmallest(): ' + check(returnTwoSmallest(),[1, 2]))
print('Enter 4 then -1')
print ('returnTwoSmallest(): ' + check(returnTwoSmallest(),[4]))
print('Enter -1')
print ('returnTwoSmallest(): ' + check(returnTwoSmallest(),[]))

print ('payroll("pay1.txt"): ' + check(payroll("pay1.txt"),[157.5, 1006.0, 116.25, 245.0]))
print ('payroll("pay2.txt"): ' + check(payroll("pay2.txt"),[878.75, 578.0, 367.0, 310.0, 116.25, 180.0, 474.25, 446.25000000000006]))
print ('payroll("pay3.txt"): ' + check(payroll("pay3.txt"),[]))
