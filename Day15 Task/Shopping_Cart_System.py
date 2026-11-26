#Shopping Cart System 
""""Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except"""

prices = {"apple": 30, "milk": 50, "bread": 40}
 
# store items in list
cart = ["apple", "milk", "apple", "bread", "milk"]
 
# set removes duplicate items
unique_items = set(cart)
 
# calculate total cost
total = 0
for item in unique_items:
    if item in prices:
        total = total + prices[item]
 
print("Items:", unique_items)
print("Total cost:", total)
 
# try-except for invalid input
try:
    quantity = int(input("Enter quantity: "))
    print("Quantity:", quantity)
except ValueError:
    print("Invalid input! Enter a number.")


