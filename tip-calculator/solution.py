print("Welcome to tip calculator!")
print("==========")
total_bill_amount=float(input("What's the total bill amount? "))
tip_percentage=int(input("What is the percentage of tip you like to give? "))
no_of_persons=int(input("How many members sharing the bill? "))

amount_to_be_paid_by_each = round((((total_bill_amount + ((tip_percentage / 100) * total_bill_amount))) / no_of_persons) , 2)

print("")
print(f"Amount to be paid by each: Rs. {amount_to_be_paid_by_each}")
print("==========")