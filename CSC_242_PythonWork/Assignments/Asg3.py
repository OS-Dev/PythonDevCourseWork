#Asg 3

#Osmel Savon

import random

class Die(object):
    def __init__(self,sides=6):
        self.sides = sides
        self.cside = random.randrange(1,self.sides)
        
    def get(self):
        return self.cside
    def roll(self):
        self.cside = random.randrange(1,self.sides)
    def numSides(self):
        return self.sides
    def __repr__(self):
        return '[%s]'\
               % (self.cside)
    def __str__(self):
        return '[%s]'\
        % (self.cside)
class Craps(object):
    def __init__(self):
        Die.__init__(self)
        d1 = Die()
        d2 = Die()
        tot = d1.cside + d2.cside
        self.tot = tot
        if self.tot == [7,11]:
            print ('Throw total: {}. You win!'.format(self.tot))
        elif self.tot == [2,3,12]:
            print ('Throw total: {}. You lose!'.format(self.tot))
        else:
            print ('Throw total: {}. Throw for point!'.format(self.tot))
        
                    
    def forPoint(self):
        roll1 = Die()
        roll2 = Die()
        tot = roll1.cside + roll2.cside
        self.roll = tot
        if self.roll == 7:
            print ('Throw total: {}. You lose!'.format(self.roll))
        elif self.roll == self.tot:
             print ('Throw total: {}. You win!'.format(self.roll))
        else:
            print ('Throw total: {}. Throw for point!'.format(self.roll))

class Collection(object):
    def __init__(self, maxSize=10):
        self.col = []
        self.maxSize = maxSize

    def __contains__(self, newItem):
        if item in self.col:
            return False
        else:
            return True

    def add(self,newItem):
        self.newItem = newItem
        if len(self.col) > self.maxSize or self.newItem in self.col:
            return False
        else:
            self.col.append(newItem)
            return True

    def size(self):
        print (len(self.col))

    def __repr__(self):
        return '%s'\
               % (self.col)

    def __str__(self):
        return '%s' \
               %(self.col)        
        
        
        
   
