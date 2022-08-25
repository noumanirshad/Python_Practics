class Programmer:
    company = "Microsoft"
    employee = "345"
    def __init__(self, subunit, salary):
        self.subunit = subunit
        self.salary = salary
    def getdetails(self):
        print(f"Subunit of {self.company} is {self.subunit}")
        print(f"Salary of {self.company} is {self.salary}")
        print(f"Employee of this {self.company} are {pro.employee}")
pro = Programmer("Printer", "35000")
pro.getdetails()
