#
# Lab 6 Template
# 


#
# 
def average(ifile):
    count = 0
    word = 0
    lst = []
    file = open(ifile, 'r')
    hold = file.readlines()
    for i in range(len(hold)):
        count = count + 1
        words = hold[i].split()
        lst = lst + words
    for i in range(len(lst)):
        word = word + 1
    results = int(word) / int(count)
    results = round(results)
    file.close()
    print ('There are {} lines in the file. There is an average of {} words per line.'.format(count,results))
        
    

        
        
    
#
#
#
def check(ifile):

    lst = []
    try:
        file = open(ifile, 'r')     
        for i in file:
            i = i.strip('\n')
            try:
                num = float(i)
                if num < 0:
                    print('Non-numeric or negative found: {}'.format(round(num * 10)))
                else: 
                    lst.append(round(num * 10))

            except ValueError:
                print('Non-numeric or negative found: {}'.format(i))
    except FileNotFoundError:
        print ('No such file.')
    return lst
        
    file.close()
        
                
            
