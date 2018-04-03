#
# lab 9 template
#
# Your name
#

def wordCount(ifile):
    'Tis program takes a file and uses a dictionary to track the number of times a word appears in that file. It returns the dictionary.'
    wordcount = dict()
    bad = ['.',',','?']
    file = open(ifile, 'r')
    hold = file.read()
    hold = hold.lower()
    for i in hold:
        if i in bad:
            hold = hold.replace(i,'')
    hold = hold.strip()
    words = hold.split()
    for i in words:
        wordcount.update({i:words.count(i)})

    print (wordcount)
    
def uniquewordSet(ifile):
    'This program takea a file, grabs the unique words in the file and prints the number of unique words as well as returns a sorted list.'
    bad = ['.',',','?','—']
    file = open(ifile, 'r')
    hold = file.read()
    hold = hold.lower()       
    for i in hold:
        if i in bad:
            hold = hold.replace(i,'')
    hold = hold.strip()
    words = hold.split()
    words = set(words)
    print (len(words))
    return words
 
