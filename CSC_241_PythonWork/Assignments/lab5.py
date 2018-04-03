
#CSC 241
#Osmel Savon
#Lab5


def idChar():
    done = False
    vowels = 'aeiou'
    con = 'bcdfghjklmnpqrstvwzyx'
    while not done:
        anw = input("Enter character: ")
        if anw == '':
            done = True
            print('Good-bye!')
        elif anw in vowels:
            print ('{} is a vowel.'.format(anw))
        elif anw in con:
            print ('{} is a consonant.'.format(anw))
        elif  anw.isnumeric():
            print ('{} is a number.'.format(anw))
        else:
            print ('{} is niether a vowel, consonant nor number.'.format(anw))
        
    
def sumUp(lst,n):
    done = False
    hold = 0
    try:
        for i in lst:
            if i >= 0:
                hold = hold + i
            else:
                raise ValueError()
        if hold%n==0:
            print ('Sum of {} is divisible by {}'.format(hold,n))
        else:
            print('Sum of {} is not divisble by {}'.format(hold,n))
    except ValueError:
        print ('Negative found. Processing stopped.')
