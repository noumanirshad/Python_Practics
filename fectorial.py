from sklearn.metrics import jaccard_score


def fec(x):
    p = 1
    # n = 5
    for i in range(x):
        p = p*(i+1)
    return (p)
f = fec(5) 
print(f)