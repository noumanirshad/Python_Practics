class Employee():
    salary = 5000
    increment = 0.6
     
    @property
    def totalsalary(self):
        print(self.salary * self.increment)


    @totalsalary.setter
    def totalsalary(self, val):
       n.increment = val / self.salary

    
n = Employee()
print(n.increment)
n.totalsalary
n.totalsalary = 8000.0
print(n.increment)
n.totalsalary   