lower=int(input("Enter the lower range:"))
lower2=int(input("Enter the upper range:"))
print("Prime numbers between",lower,"to",lower2,"are:")
for num in range(lower+lower2):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)








