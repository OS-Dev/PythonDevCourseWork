## Osmel Savon### WARNING: missing docstrings and missing comments will lose points## Question 1def inversions(s):    count = 0    for i in range(0, (len(s)-1)):        if s[i] > s[i+1]:            count += 1    print (count)    # Question 2def decVal(n):    num = []    lst = []    results = ''    try:        if n < 1:            raise ValueError()        else:            done = False            hold = float(n - .31)            while not done:                if hold < 0:                    done = True                else:                    lst.append(round(hold, 2))                    hold = float(hold - .31)                      num.append(len(lst))            num.append(lst[-2])            num.append(lst[-1])            results = num    except TypeError:        results = 'n must be numeric'    except ValueError:        results =  'n must be greater than or equal to 1'    return results        # Question 3def letter2Number(grade):    d=[['A',4.0],['B',3.0],['C',2.0],['D',1.0],['F',0]] # leave this here    done = False    grade = grade.upper()    while not done:        for sublst in d:            for i in range(len(sublst)):                if str(sublst[i]) == grade:                    print (sublst[i+1])                elif str(sublst[i]) == grade + '+':                    print (float(sublst[i+1])- .3)                else:                  done = True  if __name__ == "__main__":    def check(output, expected):        if output != expected:            return "FAILED!"        else:            return "PASSED!"    print("RUNNING CHECK ...")    print('inversions("ABBFHDL"): ' + check(inversions('ABBFHDL'),2))    print('inversions("ABCD"): ' + check(inversions('ABCD'),0))    print('inversions("CDBA"): ' + check(inversions('CDBA'),5))    print('inversions("DCBA"): ' + check(inversions('DCBA'),6))    print('inversions(""): ' + check(inversions(''),0))    print()    print('letter2Number("A-"): ' + check(letter2Number('A-'),3.7))    print('letter2Number("c+"): ' + check(letter2Number('c+'),2.3))    print('letter2Number("f"): ' + check(letter2Number('f'),0))    print('letter2Number("x"): ' + check(letter2Number('x'),'unknown grade'))    print()    print('decVal(3.1): ' + check(decVal(3.1),[9, 0.62, 0.31]))    print('decVal(1): ' + check(decVal(1),[3, 0.38, 0.07]))    print('decVal("a"): ' + check(decVal('a'),'n must be numeric'))    print('decVal(0): ' + check(decVal(0),'n must be greater than or equal to 1'))