actual_cost=float(input("Enter the actual product price please:"))
sale_amount=float(input("Enter the actual sales amount please:"))

if(sale_amount>actual_cost):
    amount=(sale_amount-actual_cost)
    print("Total profit={0}".format(amount))
else:
    print("No Profit!!!!!!")









