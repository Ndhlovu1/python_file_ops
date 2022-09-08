# menu = {
#     1: {"name": 'espresso',
#         "price": 1.998},
#     2: {"name": 'coffee', 
#         "price": 2.50},
#     3: {"name": 'cake', 
#         "price": 2.79},
#     4: {"name": 'soup', 
#         "price": 4.50},
#     5: {"name": 'sandwich',
#         "price": 4.99}
# }

# def calc_subtotal(item):
#     return menu[item];

# print(calc_subtotal(1))
# print(menu.items())
# print()
# print(menu.values())
# print()

# espressor_price = menu[1]["price"]

# print(float(espressor_price))

# IDs = [1,2,3,4,5]

# prices = {"price"}

# Pricing = dict.fromkeys(IDs,prices)

# print("Below are the Prices -- \n",Pricing,"\n")


# def calc (*arrgs):
#     sum = 0
#     for values in arrgs:
#         sum += values
#         sum = round(sum, 2)
#     return float(sum)

# calc(menu[1]["price"],menu[2]["price"], menu[3]["price"])


from functools import total_ordering
from re import sub
from unicodedata import name



menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(*order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    total = 0
    
    
    for values in order:
        total = values
        # total = float(total)
        # total = round(total,2)
        
    
        item_1 = total[0]["price"]
        item_2 = total[1]["price"]
        item_3 = total[2]["price"]

        item_1 = float(item_1)
        item_2 = float(item_2)
        item_3 = float(item_3)

        sub_total = item_1 + item_2 + item_3
        sub_total = round(sub_total,2)
        sub_total = float(sub_total)
        #print("N$", sub_total)

    # print(total[1]["name"])
    # name_1 = total[0]["name"]
    # name_2 = total[1]["name"]
    # name_3 = total[2]["name"]

    # names = [name_1, name_2, name_3]
    # print("##################################",names,"##################################")

    return sub_total
    
   
    
    ##############################
    #print(final_list[::])
    #print(item_1, item_2, item_3)

    #     sum = 0
    # for values in arrgs:
    #     sum += values
    #     sum = round(sum, 2)
    # return float(sum)

    

    #################################
        
    #print(type(total))
   


    raise NotImplementedError()

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    subtot_value = subtotal

    subtotal_tax = (subtot_value * 15) / 100
    subtotal_tax = round(subtotal_tax,2)
    subtotal_tax = float(subtotal_tax)
    
    return subtotal_tax

    raise NotImplementedError()

def summarize_order(*order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    #print_order(order)
    ### WRITE SOLUTION HERE
    # Implement `summarize_order()` which returns a list of the names of the items   
    # that the customer ordered and the total amount (including tax) that they have to pay.  
    # The orders should show the name and price.
   
    #Names First   
     
    #TOTAL
    # all_names = ''
    # for item in order:
    #     all_names = item

    # print(all_names[1]["name"])

    # name_1 = all_names[0]["name"]
    # name_2 = all_names[1]["name"]
    # name_3 = all_names[2]["name"]

    # names = [name_1, name_2, name_3]
    # print(names)
   
    # return names

    all_names = ''
    total = 0

    for item in order:
        all_names = item
        total = item
        
    #print(all_names[1]["name"])

    name_1 = all_names[0]["name"]
    name_2 = all_names[1]["name"]
    name_3 = all_names[2]["name"]

    names = [name_1, name_2, name_3]
    print("#############TYPE IS ########## \n",type(names))

    item_1 = total[0]["price"]
    item_2 = total[1]["price"]
    item_3 = total[2]["price"]

    #tot_val = [item_1,item_2,item_3]
    #print(tot_val)

    item_1 = float(item_1)
    item_2 = float(item_2)
    item_3 = float(item_3)

    sub_total = item_1 + item_2 + item_3
    sub_total = round(sub_total, 2)
    sub_total = float(sub_total)
    print(sub_total)
    

    #Tax 
    tx = (sub_total * 15) / 100
    tx = round(tx, 2)
    tx = float(tx)

    #Total Calculation
    total = tx + sub_total

    return names, total


    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    tax,subtotal = summarize_order(order)

if __name__ == "__main__":
    main()
