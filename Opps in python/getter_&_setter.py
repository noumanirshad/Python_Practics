class Preston:
    uni = '"preston"'
    fine = 500
    fee = 9000

    @property
    def totalfees(self):
        print(f"Total fee of {lab.student} is {self.fee + self.fine}")
        
    @totalfees.setter
    def totalfees(self, val):
        self.fine = val - self.fee


lab = Preston()
lab.student = '"Nouman"'
lab.totalfees
print(f"Total fine : {lab.fine}")
lab.totalfees = 9300
print(f"Total fine after Consection: {lab.fine}")
lab.totalfees
print(f"Fee of {lab.student}: {lab.fee}")



