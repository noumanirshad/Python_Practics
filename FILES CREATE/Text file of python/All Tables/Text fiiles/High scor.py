def HighScore(a):
    return(a)
n = int(input("ENTER the score: "))
score = HighScore(n)
with open("HighScore.txt")as f:
    g = (f.read())
if g == '':
    with open("HighScore.txt", 'w') as f:
        f.write(str(score))

elif score > int(g):
    with open("HighScore.txt", 'w') as f:
        f.write(str(score))