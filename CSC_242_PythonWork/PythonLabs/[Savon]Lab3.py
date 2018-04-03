
# Osmel Savon
# Collaborators- Micheal Barcroft, Micheal Inzyskind - for problem #1


#1
#Subclass of list tat iterates over odd indices
class OddList(list):
    def __init__(self,lst):
        self.oddlst = lst
        ListIterator(self.oddlst)

    def __iter__(self):
        return ListIterator(self.oddlst)

class ListIterator:
    def __init__(self,oddlst):
        self.lst = oddlst
        self.i = -1

    def __next__(self):
        if self.i >= len(self.lst) - 2:
            raise StopIteration
        else:
            self.i +=2
            return self.lst[self.i]
#2
#Modified Animal class with InvalidAge exception for negative ages
class InvalidAge(Exception):
    pass
        

class Animal:

    #modify __init__
    def __init__(self, newSpecies="default", newLanguage="default", newAge=0):
        if newAge < 0:
            raise InvalidAge('{} is an invalid age'.format(newAge))
        else:
            self.species = newSpecies
            self.language = newLanguage
            self.age = newAge

    def __repr__(self):
        return "Animal('{}','{}',{})".format(self.species, self.language, self.age)

    def __eq__(self, otherAnimal):
        return self.species == otherAnimal.species and self.language == otherAnimal.language and self.age == otherAnimal.age

    def setSpecies(self, newSpecies):
        self.species = newSpecies

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    #modify setAge()
    def setAge(self, newAge):
        if newAge < 0:
            raise InvalidAge('{} is an invalid age'.format(newAge))
        else:
            self.newAge = newAge

    def speak(self):
        print("I am a {} year-old {} and I {}.".format(self.age, self.species, self.language))

#3
#Modified processAnimals function with InvalidAge exception
def processAnimals(file):
    animalList = []

    inFile = open(file)
    lineList = inFile.readlines()
    inFile.close()

    #modify the code in loop to handle Animals being made with negative ages (refer to lab for output examples)
    for line in lineList:
        try:
            data = line.strip('\n').split(',')
            newAnimal = Animal(data[0], data[1], eval(data[2]))
            animalList.append(newAnimal)
            newAnimal.speak()
        except InvalidAge:
            print ('Animal skipped in file {}: {} is an invalid age'.format(file,data[2]))
            continue
    return animalList
