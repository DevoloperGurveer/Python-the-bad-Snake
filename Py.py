num1=[1,2,3]
num2=[2,55,66]
result=map(lambda x,y:x+y,num1,num2)
print("Addition of two lists")
print(list(result))
nums=[1,2,3,4,5,6,7,8,9]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("square of numbers in list")
print(square)