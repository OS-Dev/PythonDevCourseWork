#
# Assignment 9
#
# Osmel Savon
#
#
#
def letter2number(s):
    'This program takes user input and returns the number grade associated to thier input. If user inputs invalid grade message alert.'
    grades = {'A':4, 'A-':3.7, 'B':3, 'B+':3.3,'B-': 2.7, 'C':2, 'C+':2.3,'C-': 1.7, 'D':1, 'D+':1.3,'D-': .7,'F':0, 'F+':.3}
    s = s.upper()
    if s in grades:
        print(grades[s])
    else:
        print ('unkown grade')
        
def translate():
    'This program is a translation service. Where you may enter an input and the translated word will be given back. Enter quit to exit.'  
    done = False
    translations = {'sen':'ago', 'tilltalande':'pleasing', 'ge':'provide', 'ont': 'hurt', 'allt': 'everything'}
    print ('Welcome to the WorldRUs translation service.')
    while not done:
        keys = translations.keys()
        word = input('Please enter a word: ')
        qword = word.lower()
        if qword == 'quit':
            done = True
            print('Thanks for using our translation service.')
        else:    
            for i in keys:
                valu = translations[i]
                if word == i:
                    valu = translations[i]
                    print (word, 'means', valu)
            if word not in keys:
                print (word, 'means', '_' * len(word))

def vote(lst):
    'This program allows users to vote in some sort of election and will return the votes person in the lst and it will tell how many votes to those not in the list were casted.'
    master = []
    count = 0
    done = False
    while not done:
        vote = input('Enter a vote: ').lower()
        vote = vote[0:1].upper() + vote[1:len(vote)+1]
        master.append(vote)
        if vote == '':
            done = True
        elif vote not in lst:
            count +=1
    for i in range(len(lst)):
        amnt = master.count(lst[i])
        if i % 2 == 0:
            word = 'were'
        else:
            word = 'was'
        print ('There {} {} votes for {}'.format(word, amnt, lst[i]))
    if count > 0:
        print ('There {} {} votes for {}'.format('were', count, 'Unknown'))

        
    
