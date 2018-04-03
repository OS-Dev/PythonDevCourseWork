# Assignment 2

# Osmel Savon

import time

class Vehicle(object):

    def __init__(self,modelt='Beater',year = 2016, age = 1):
        self.age = int(age)
        self.modelt = modelt
        new = time.localtime()
        if modelt =='Beater':
            self.year = 2000
            self.age = 17
        else:
            self.year = year
        self.age = new[0] - self.year        

    def age(self):
        age = int(new[0]) - int(self.year)
        return age

    def model(self):
        return self.modelt

    def __repr__(self):
        return 'Vehicle(%s,%s)' \
              % (self.modelt, self.age)

    def __str__(self):
        return ('This {} is {} years old.'.format(self.modelt,self.age))

class BasicCar(Vehicle):

    def __init__(self,modelt,year,MPG):
        self.modelt = modelt        
        self.MPG = MPG
        Vehicle.__init__(self,modelt,year)
            
    def milesPerGallon(self):
        return (self.MPG)

class GreenCar(Vehicle):

    def __init__(self,modelt='unknown',year = 2016,MPC='Unkown'):
        self.modelt = modelt 
        self.MPC = MPC
        Vehicle.__init__(self,modelt,year)

    def milesPerCharge(self):
        return (self.MPC)

def processVehicles(infile):
    lst = []
    ifile = open(infile)
    hold = ifile.readlines()
    try:
        for i in hold:
            i = i.strip()
            k = i.split(' ')
            lst.append(i)
            if len(k) == 2:
                x = Vehicle(k[0],k[1])
                print(x)
            else:
                x = Vehicle(k[0])
                print(x)
        print (lst)
    except:
        return ('File is empty')
    
    ifile.close()
        

if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
        
myCar=Vehicle('Focus')
print('myCar.age(): ' + check(myCar.age(),1))
print("check on repr -> myCar -> should be Vehicle(Focus, 1)")
print('need to run myCar check')
print("print check -> should be This Focus is 1 years old")
print(myCar)
yourCar=Vehicle()
print('yourCar.age(): '+check(yourCar.age(),17))
print('check on repr -> yourCar -> should be Vehicle(Beater, 17')
print('need to run yourCar check')
print("print check -> should be This Beater is 17 years old")
print(yourCar)
car1=BasicCar('Taurus',2007,35)
print('car1.MPG: '+check(car1.MPG,35))
print("print check - should be This Taurus is 10 years old")
print(car1)
print('check on repr -> car1 0> should be Vehicle(Taurus,10)')
print("car1.milesPerGallon(): "+ check(car1.milesPerGallon(),35))
car2=GreenCar('Prius',2016,200)
print('car2.MPC: '+check(car2.MPC,200))
print("print check - should be this prius is 1 years old")
print(car2)
car3=GreenCar()
print('print check - this unknown is 1 years old')
print(car3)
print('----')
print("processVehicles('try1.txt'): "+check(processVehicles('try1.txt'),['Ford Taurus 1', 'Volkswagon Bug 1']))
print("processVehicles('try2.txt'): "+check(processVehicles('try2.txt'),['Ford Taurus 17', 'Volkswagon Bug 6', 'Toyota Prius 1', 'Toyota Yaris 10']))
print("processVehicles('try3.txt'): " +check(processVehicles('try3.txt'),[]))
print("processVehicles('nosuchfile.txt'): " +check(processVehicles('nosuchfile.txt'),'No such file.'))
