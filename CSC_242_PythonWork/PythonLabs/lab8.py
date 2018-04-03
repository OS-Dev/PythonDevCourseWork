
# Osmel Savon



import os

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py' ))
    
def fileCount(folder):
    "count the number of files in a directory"

    count = 0
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if os.path.isfile(path):
            count += 1
        elif os.path.isdir(path):
            count += fileCount(path)
    return count
def isPalindrome(s):

        if len(s) <= 1:
            return True

        elif s[0] != s[-1]:
            return False
        else:
            return isPalindrome(s[1:-1])


