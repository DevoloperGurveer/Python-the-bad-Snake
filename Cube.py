def cube(num):
    return num*num*num
def by_three(num):
    if num %3==0:
        return cube(num)
    else:
        return False
print(by_three (55623585832))
print(by_three (2088))