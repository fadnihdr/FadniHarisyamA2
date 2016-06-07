num_lines = sum(1 for line in open('items.csv'))
"""count the lines in a file"""
print("Items for Hire - by Fadni Harisyam\n{} items loaded".format(num_lines))


menu = ("Menu:\n (L)ist all items\n (H)ire an item\n (R)eturn an item\n (A)dd new item to stock\n (Q)uit")
"""this will be my main menu"""
openItem = open('items.csv', 'r')
userInput = input(menu).lower() #all inputs will be treated as lowercase


def item_list():
    item_num = 0
    with open('items.csv') as items:
        for words in items:
            name,item_desc,cost,status = words.split(',')
            if "in" in status:
                print("{:} - {:<40s} = ${:>7,.2f}".format(item_num, name + "(" + item_desc + ")", float(cost)))
            elif 'out' in status:
                print("{:} - {:<40s} = ${:>7,.2f} *".format(item_num, name + "(" + item_desc + ")", float(cost)))
            item_num += 1
    items.close()
    """
    A function to load and show items from the csv file

    and will remove the commas, removing 'in' and replacing 'out' with an asterisk '*'

    the values for each line are name,item_desc,cost,status
    """


def item_hire():
    item_count = 0
    list_num = []
    line_list = list()
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index, line in enumerate(item_lines_list):
        line_list.append(line)
        name, item_desc, cost, status = line_list[index].split(',')
        if 'in' in status:
            print("{:} - {:<40s} = ${:>7,.2f}".format(item_count, name + " (" + item_desc + ") ", float(cost)))  #(1)
            list_num.append(item_count)
        item_count += 1

    if len(list_num) == 0:
        print("No item is currently available for hire")  #(3)
    else:
        try:

            replace = int(input("Enter the number of an item to hire:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('in', 'out')  #(2)
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list)
                    name, item_desc, cost, status = line_list[replace].split(',')
                    print("{} is hired for ${:.2f}".format(name, float(cost)))  #(4)
            else:
                print("That item is not available for hire")  #(5)
        except:
            print("Invalid input")
    """
    this function will modify the status element in the strings in items.csv
    (1)it will display the items that are present in items.csv
    (2)it will change the hired item's status from "in" to "out"
    (3)if there is no item available for hire, it will display "No item is currently available for hire"
    (4)after the user successfully hired an item, the confirmation message will show up
    (5)if the user input a number thats not in the list, an message will show up "That item is not available for hire"
    """

def item_return():
    item_count = 0
    list_num = []
    line_list = list()
    with open('items.csv') as file:
        item_lines_list = file.readlines()
    for index, line in enumerate(item_lines_list):
        line_list.append(line)
        name, item_desc, cost, status = line_list[index].split(',')
        if 'out' in status:
            print("{:} - {:<40s} = ${:>7,.2f} *".format(item_count, name + " (" + item_desc + ") ", float(cost)))
            list_num.append(item_count)
        item_count += 1

    else:
        try:

            replace = int(input("Enter the number of an item to return:\n"))
            if replace in list_num:
                item_lines_list[replace] = item_lines_list[replace].replace('out', 'in')  #(1)
                with open('items.csv', 'w') as file:
                    file.writelines(item_lines_list)
                    name, desc, price, hire = line_list[replace].split(',')
                    print(name, "returned.")  #(2)
            else:
                print("That item is not available for rent.")   #(3)
        except:
            print("Invalid input")
    file.close()


"""
this function will modify the status element in the strings in items.csv
(1)it will change the hired item's status from "out" to "in"
this function will only show hired items
(2)after the user successfully returned an item, the confirmation message will show up
(3)if the user input a number thats not in the list, an message will show up "That item is not available for rent"
"""

def item_append():
    """when the user enters "a" it will ask the user's item name,
        description, and cost, and add them to the csv file"""


    name = (input("Name:"))
    while len(name) <= 0:
        print("Please input a valid name")
        name = (input("Name:"))
    item_desc = (input("Description:"))
    while len(item_desc) <= 0:
        print("Please input a valid description")
        item_desc = (input("Description:"))
    try:  # to error check the cost by putting a ValueError exception
        cost = int(input("Cost:"))
    except ValueError:
        print("Please enter a valid integer")
        cost = int(input("Cost:"))
    items_write = open('items.csv', 'a')
    print((name + "," + item_desc + "," + str(cost) + "," + "in"), file=items_write)
    items_write.close()
    print(name, item_desc, cost)
    print("\n{} ({}), ${:.2f} now available for hire.".format(name, item_desc, cost))
    userInput = input(menu).lower()
    num_lines += 1
