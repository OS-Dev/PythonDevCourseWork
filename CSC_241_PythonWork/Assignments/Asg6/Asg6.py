#
# Your name and the names of any collaborators
#
#

import os   # this is required to do the empty file check 

def showNames(ifile):
    lst = []
    name = []
    try:
        file = open(ifile, 'r')
        hold = file.readlines()
        for i in hold:
            lst = i.split()
            name.append(lst[0])
    except:
        name = [-1]
    return name
            

def calcAvg(ifile): # Couldnt figure out what was wrong
    lst = []
    grades = []
    non = ''
    try:
        file = open(ifile, 'r')
        hold = file.readlines()
        stu = int(len(hold))
        for i in hold:
            try:
                lst = i.split()
                grades.append(int(lst[2]))
            except:
                non = "Non-numeric found. "
                stu = stu - 1
        total = round((sum(grades)/stu))
        results = '{}Total number of students: {} Average score: {}'.format(non, stu,total)
    except:
        results = 'File not found.'
    print(results)
    return results

def studentAvg(ifile):
    lst = []
    avrg = []
    name = []
    try:
        if os.stat(ifile).st_size == 0: # note: it uses the stat method from os
            raise ValueError
        else:
            file = open(ifile, 'r')
            hold = file.readlines()
            for i in hold:
                lst = i.split()
                name = lst[0]
                grades = []
                non = ''
                for i in range(2, len(lst)):

                    try:   
                        grades.append(int(lst[i]))                      
                    except:
                        non = "Error! Non-numeric! "
                div = len(grades)
                total = (sum(grades)/ div)
                results = '{}Name: {} Number of assignments: {} Average score: {}'.format(non, name, div, total)
                avrg.append(results)
    except ValueError:
        avrg = 'File is empty.'
        
    except:
        avrg = 'File not found.'
    return avrg
if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
    print("RUNNING CHECK ...")
    print('showNames(ifile): ' + check(showNames("nosuchfile.txt"),[-1]))
    print('showNames(ifile): ' + check(showNames("grades1.txt"),['Domel', 'Fischer', 'Hope', 'Patel']))
    print('showNames(ifile): ' + check(showNames("grades2.txt"),['Domel', 'Fischer']))
    print()
    print('calcAvg(ifile): ' + check(calcAvg("nosuchfile.txt"),'File not found.'))
    print('calcAvg(ifile): ' + check(calcAvg("grades1.txt"),'Non-numeric found. Total number of students: 3  Average score: 96'))
    print('calcAvg(ifile): ' + check(calcAvg("grades2.txt"),'Non-numeric found. Total number of students: 1  Average score: 90'))
    print()
    print('studentAvg(ifile): ' + check(studentAvg("nosuchfile.txt"),'File not found.'))
    print('studentAvg(ifile): ' + check(studentAvg("grades1.txt"),['Error! Non-numeric! Name: Domel Number of assignments: 7 Average score: 81.42857142857143', 'Name: Fischer Number of assignments: 8 Average score: 74.125', 'Name: Hope Number of assignments: 8 Average score: 100.0', 'Name: Patel Number of assignments: 8 Average score: 90.375']))
    print('studentAvg(ifile): ' + check(studentAvg("grades2.txt"),['Error! Non-numeric! Name: Domel Number of assignments: 7 Average score: 0.0', 'Name: Fischer Number of assignments: 8 Average score: 90.0']))
    print('studentAvg(ifile): ' + check(studentAvg("grades3.txt"),'File is empty.'))


            
