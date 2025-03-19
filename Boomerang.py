test_dict={'Chicken':2,'is':2,'the':2,'best':2,'for':2,'hunting':2}
print("The Original dictionary:"+str(test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print("Frequency of K is :"+str(res))