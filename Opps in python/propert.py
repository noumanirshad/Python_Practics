class Employee:
    company = "Utube"
    salary = 4000
    bonus = 500
    @property
    def Totalsalary(self):
        return self.salary + self.bonus

    @Totalsalary.setter
    def Totalsalary(self, abc):
        self.bonus = (abc - self.salary)


c = Employee()
# print(c.Totalsalary)
c.Totalsalary = 4200
print(c.Totalsalary)
print(c.salary)
print(c.bonus)