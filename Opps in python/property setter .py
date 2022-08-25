class Employee:
    salary = 4000
    increment= 0.5
    
    @property
    def pro(self):
        return self.salary * self.increment

    @pro.setter
    def pro(self , vac):
        self.increment = (vac/self.salary)
c = Employee()
print(c.pro)
print(c.increment)
c.pro = 6000
print(c.increment)
print(c.salary)