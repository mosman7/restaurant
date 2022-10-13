# Restaurant task

First the customer needs to be able to see the menu so i have printed all available items in the form of a list
```python
menu = ["Chicken curry", "Vegetable curry", "Lamb curry", "Chips", "Chicken Wrap", "Veggie Wrap",
        "Dr Pepper", "Fanta", "Coke", "Water"]
for i in menu:
    print(i)
```

Next we need to take the customers order

```python
new_order = []

order_length = 3         #only 3 items can be ordered

for food in range(order_length):        #loops through the list untill order length is reached
    item = input('Enter item to order: ')
    new_order.append(item)              #adds the item to the list
```

Next we need to print the order back to the customer to confirm what they have ordered
```python
print(new_order)        #prints the order
```