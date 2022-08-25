import numpy as np

# def gradient_discent(x,y):
x = [1,2,3,4,5,6]
y = [61, 22, 32, 41]
m_curr = b_curr = 0
iterations = 1000
n = len(x)
l = 0.001

for i in range(iterations):
    yp = (m_curr)*x + (b_curr)
    cost = (1/n)*sum([b**2 for b in (y-yp)])
    md = -2/n*sum(x*(y-yp))
    bd = -2/n*sum(y-yp)
    m_curr = m_curr - l*md
    b_curr = b_curr - l*md
    print("m {} ,,, b {} ,, cost {} ,, iteration {}".format(m_curr, b_curr, cost, i))

# x = [1,2,3,4,5,6]
# y = [61, 22, 32, 41]
# gradient_discent(x,y)