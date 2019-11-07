# classes and inheritance
# debugging using print function

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        # print(self.pay)

    def firstName(self):
        return self.name.split()[0]
        # print(self.name)

    def lastName(self):
        return self.name.split()[-1]
    
    def GiveRaise(self, percent):
        # print(self.pay)
        self.pay = int(self.pay*(1+percent) )
        # return self.pay = int(self.pay*(1+parent))
        print('test #001 starts')
        print(self.pay)
        print('test #001 ends')


class Manager:
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def GiveRaise(self, percent, bonus=0.10):
        Person.GiveRaise(self, percent + bonus)

if __name__ == '__main__':
    John = Manager('James Bond', 50000)
    John.GiveRaise(.20)
print(John)