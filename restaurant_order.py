# User Stories

# As a User I want to be able to see the menu in a formated way, so that I can order my meal.
menu = ["Chicken curry", "Vegetable curry", "Lamb curry", "Chips", "Chicken Wrap", "Veggie Wrap",
        "Dr Pepper", "Fanta", "Coke", "Water"]
for i in menu:
    print(i)

# AS a User I want to be able to order 3 times,
# and have my responses added to a list so they aren't forgotten
new_order = []

order_length = 3         #only 3 items can be ordered

for food in range(order_length):        #loops through the list untill order length is reached
    item = input('Enter item to order: ')
    new_order.append(item)              #adds the item to the list

print(new_order)        #prints the order