# Osmel Savon
# Jerwin

# Lab 8


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab7TEST.py' ))

from html.parser import HTMLParser
from urllib.request import urlopen

class HeaderParser(HTMLParser):
    '''subclass of imported HTMLParser class. Finds and collects contents of
    headings in an HTML file that is fed to it. Identifies when a heading tag
    has been encountered and sets a boolean variable to indicate it. When data
    handler is called and the boolean in the calss indicates the header is currently
    open, the data inside the header is added to a list. Finally, when a closing
    header tag is encountered, the boolean variable is unset. Override the
    following methods'''
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.boo = False
        self.headers = ['h1','h2','h3','h4','h5','h6']
        
    def handle_starttag(self, tag, attrs):
        if tag in self.headers:
            self.boo =True
    

    def handle_endtag(self, tag):
        '''If the tag that resulted in this method being called is a header,
           the header indicator should be unset'''
        if tag in self.headers:
            self.boo = False

    def handle_data(self, data):
        '''If the parser is currently inside a header, then the data should be
           added to the list. Strips any leading or trailing white space.'''
        if self.boo == True:
            if data.strip() != '':
                self.lst.append(data.strip())

    def getHeadings(self):
        '''The function returns the list of headings gathered by the parser'''
        return self.lst

def testHParser(url):
    '''opens the url, reads it, and converts it to a string saved in a variable.
       Creats an object of HeaderParser class and feeds it the string. Returns
       the the getHeadings method'''
    content = urlopen(url).read().decode()
    parser = HeaderParser()
    parser.feed(content)
    return parser.getHeadings()
