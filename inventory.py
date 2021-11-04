#program stores the inventory of items
#string values are keys describing the item in the inventory and their respective value is an integer value of the amount of the item
#function takes the inventory and displays the inventory

#storing the items in a dictionary
item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#function to display and sum the items in the inventory.
def displayInventory(inventory):
    total_items = 0 
    for key,value in inventory.items():
        print(f'{value} {key}')
        total_items += value
    print(f'Total number of items: {total_items}')

#calling the function
displayInventory(item)