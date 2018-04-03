#
# Assignment 6
#
# Osmel Savon Ozzy
#

from html.parser import HTMLParser
from urllib.request import urlopen

class ListParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.boo = False

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.boo =True

    def handle_endtag(self, tag):
        if tag == 'li':
            self.boo = False

    def handle_data(self,data):
        if self.boo == True:
            if data.strip() != '':
                self.lst.append(data.strip())

    def getItems(self):
        return self.lst

def testLParser(url):
    content = urlopen(url).read().decode()
    parser = ListParser()
    parser.feed(content)
    return parser.getItems()

def depthCount(lst,depth = 0):
    if lst ==[]:
        return 0
    elif type(lst) == list:
        if depthCount(lst[0], depth +1) > depthCount(lst[1:], depth):
            return depthCount(lst[0],depth+1)
        else:
            return depthCount(lst[1:],depth)
    else:
        return depth -1
    
import os

def filePrint(path,indent):
    pass

def search(ifile,fpath)
    pass



