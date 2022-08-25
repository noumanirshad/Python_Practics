class Customer:
    name = "M.IRSHAD"
    place = "Dothan Khaigala"

    def __init__(self, budgect, salary, name):
        self.budgect = budgect
        self.salary = salary
        self.name = name

    def getdetails(self):
        print(
            f'Budgect of is "{self.budgect}"\nSalary of this employee is "{self.salary}"\nname of employee is "{self.name}"\n')


emp = Customer(25000, 10000, "ali")
afaq = Customer(35000, 12000, "numi")
emp.getdetails()
afaq.getdetails()
