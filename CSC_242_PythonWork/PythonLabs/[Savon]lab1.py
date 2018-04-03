# Lab 1

# Osmel Savon - Ozzy


class Animal(object):
    def __init__(self, species='default', language='default', age=0, weight = 0):
        self.species = species
        self.language = language
        self.age = age
        self.weight = weight
    def __repr__(self):
        return 'Animal(age=%s, species = %s, language = %s)'\
               % (self.age, self.species, self.language)   
    def setAge(self,n):
        self.age = n
    
    def getAge(self):
        print (self.age)
    
    def setWeight(self, n):
        self.weight = n
        
    def getKilos(self):
        return (self.weight/2.2)
    
    def setSpecies(self, species):
        self.species = species
        
    def setLanguage(self, language):
        self.language = language
        
    def speak(self):
        print ('I am a {} year old {} and I {}'.format(self.age,self.species, self.language))

    def __str__(self):
        return ('I am a {} year old {} and I {}'.format(self.age,self.species, self.language))

def processAnimals(filename):
    'This program processes animals from a file'
    lst = []
    ifile = open(filename)
    hold = ifile.readlines()
    
    try:
        if hold != []:
            for i in hold:
                strip = i.strip('\n')
                temp = strip.split(',')
                temp = Animal(temp[0],temp[1],temp[2])
                lst.append(temp)
                temp.speak()
        else:
            raise ValueError()
    except ValueError:
        print ('The file {} could not be opened. Exiting...'.format(filename))
        return lst
    ifile.close()

    
