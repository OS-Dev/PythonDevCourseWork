# Lab 2
#
# Osmel Savon
#
class Worker(object):
    def __init__ (self,name='Jane Doe',rate=8.25):
        self.name = name
        self.rate = float(rate)
    def changeRate(self,nrate):
       self.rate = nrate
    def weeklyPay(self,hours):
        self.hours = hours
        self.tot = self.hours * self.rate
        print (self.tot)
        return ('Not Implemented')
    def __repr__(self):
        return 'Worker(%s,%s)'\
               %(self.name,format(self.rate, '.2f'))        

class HourlyWorker(Worker):
    def __init__ (self):
        Worker.__init__(self)
    def weeklyPay(self,hours):
        if hours > 40:
            temp = 40 * self.rate
            ot = hours - 40
            otr = (ot*(2*self.rate))
            self.tot = otr + temp
            print (self.tot)
        else:
            self.tot = hours * self.rate
            print (self.tot)

class SalariedWorker(Worker):
    def __init__ (self):
        Worker.__init__(self)
    def weeklyPay(self,hours):
        self.hours = hours
        self.tot = self.hours * self.rate
        print (self.tot)
