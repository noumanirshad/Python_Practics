class Number:
    
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return self.num

numi = Number("5")
print(numi)