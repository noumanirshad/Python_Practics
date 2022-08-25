class Number:

    def __init__(self, num):
        self.num = num
        print(self.num)

    def __add__(self, num2):
        print("lets add")
        print(self.num +  num2.num +self.num)
        # print(self.num *  num2.num)

    def __mul__(self, num3):
        print("lets multiply")
        print(self.num * num3.num)
        # print(self.num + num2.num)

numi = Number(4)
numi2 = Number(5)
numi3 = Number(9)
numi + numi2
numi * numi3
# print(sum)