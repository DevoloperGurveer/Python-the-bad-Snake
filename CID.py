import random
Metashot=True
number=str(random.randint(0,25))
print ("I am doing my doing my work you guess the hardest number of your life")
print("The game ends when it realizes that you are mad")
while Metashot:
    guess=input("Give me your brain \n")
    if number==guess:
        print("Get lost,let me sleep")
        print("The no. was",number)
        break
    else:
        print("You are mad \n")

