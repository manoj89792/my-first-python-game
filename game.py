import random
score = []
while (len(score) <= 5):
    print("your current score is : ", score)
    n = random.randint(0, 9)
    useri = int(input("Enter any value(0-9) : "))
    print("your input : ", useri)
    print("computer input : ", n)
    if useri == n:
        score.append(n)
