# From page 120 in 'Automate the Boring Stuff with Python' book



## Step 1 - make a function to display what is in the inventory 

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():                          # For dict k(key), in v(value) of the itens in the given dict,
        print(str(v) + ' ' + k)                             # Print it as a string, so it will be value ' ' key
        item_total += v                                     # Add this to the item total
    print("Total number of items: " + str(item_total))      # Print the total number of items, as a string :)


displayInventory(stuff)




## Step 2 - Make a function that will add items to the inventory 

# def addToInventory(inventory, addedItems):
#     inventory = 1
    


# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)