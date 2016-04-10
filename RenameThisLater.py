"""

function main()
    get items_file from items.csv file

    print welcome message with author name

    display menu
    get menu choice from user
    while choice isn't q

        if choice is l
            print "All items on file (* indicates item is currently out):"
            for item in items_file
                print item removing commas, add selection index, format neatly and adding astrix if item is out
        else if choice is h
            hire_item(items_file)
        else if choice is r
            item_list = return of display_and_get_item_list(choice, items_file)
            if item_list contains values
                return_item(items_file, choice)
            else
                print "No items are currently on hire"
        else if choice is a
            add_new_item()
        else
            display invalid choice message

        display menu
        get menu choice from user
    save items_file
    print amount of items saved to items_file and a fairwell message

function add_new_item()
    get item name from user
    while name is blank
        print blank name error
        get item name from user

    get item description from user
    while description is blank
        print blank description error
        get item description from user

    set price_is_invalid to true
    while price_is_invalid
        try
            get item price from user
            convert item price to number
            set price_is_invalid to false
        error value error
            print price not a number error
            set price_is_invalid to true

    print item added as available to hire

function hire_item(items_file)

    set has_item_been_listed to false
    for item in items_file
        if item has not already been hired
            print item removing commas, add selection index, format neatly
            set has_item_been_listed to true

    if has_item_been_listed is false
        print "All items are currently on hire"
    else
        print "Enter the number of the item to hire"
        set index_choice_is_a_number to false
        while index_choice_is_valid is false
            try
                get index_choice from user
                convert index_choice to number
                index_choice_is_a_number = true
            error value error
                print invalid input error

        if item in items_file at the index of index_choice is able to be hired
            print the selected items name and cost
            set the item selected to "out" in items_file
        else
            print "That item is not available for hire"

function return_item(items_file)

    set has_item_been_listed to false
    for item in items_file
        if item is currently out on hire
            print item removing commas, add selection index, format neatly
            set has_item_been_listed to true

    if has_item_been_listed is false
        print "No items are currently on hire"
    else
        print "Enter the number of the item to return"
        set index_choice_is_a_number to false
        while index_choice_is_valid is false
            try
                get index_choice from user
                convert index_choice to number
                index_choice_is_a_number = true
            error value error
                print invalid input error

        if item in items_file at the index of index_choice is able to be hired
            print the selected items name and say it was returned
            set the item selected to "in" in items_file
        else
            print "That item has already been returned"
"""

PROGRAM_NAME = 'Items for Hire'
AUTHOR = 'Caleb Macdonald Black'
FILE_NAME = 'items.csv'
MENU = 'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n'


# TODO change items.csv file to original one

def main():
    """
    Main function: This calls the necessary functions to load the csv file, display menu and handle menu interaction
    from the user and save the updated information to the csv file before exiting
    """
    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))
    read_file = open(FILE_NAME, 'r')
    items_list = create_list_from_file(read_file)
    read_file.close()

    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            if len(items_list) > 0:
                outputted_items(items_list, 'all')
            else:
                print('There are currently no items')

        elif menu_choice == 'H':
            if outputted_items(items_list, 'out'):
                items_list = hire_item(items_list)
            else:
                print('All items are currently on hire')

        elif menu_choice == 'R':
            if outputted_items(items_list, 'in'):
                items_list = return_item(items_list)
            else:
                print('No items are currently on hire')

        elif menu_choice == 'A':
            items_list = add_new_item(items_list)

        else:
            print('Invalid menu choice')

        menu_choice = input(
            'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n').upper()
    save_item(items_list)
    print('Have a nice day :)')


def create_list_from_file(items_file):
    """
    Reads the file and returns a list of items as lists. This will also print to the console the amount of items loaded
    :param items_file: The read only csv file containing the items
    :return items_list: All Item information converted to a list and appended to another list
    """
    items_list = []

    for line in items_file.readlines():
        item_as_list = line.split(',')
        item_as_list[3] = item_as_list[3].replace('\n', '')
        items_list.append(item_as_list)

    # ensure grammar in 'loaded' message is correct
    if len(items_list) == 1:
        print('1 item loaded from {}'.format(FILE_NAME))
    elif len(items_list) == 0:
        print('No items loaded from {}'.format(FILE_NAME))
    else:
        print('{} items loaded from {}'.format(len(items_list), FILE_NAME))

    return items_list


def save_item(items_list):
    """
    Takes a list of items as lists and saves it to the the csv file. This function will also print the amount of items
    saved to the console
    :param items_list: All Item information converted to a list and appended to another list
    """
    write_file = open(FILE_NAME, 'w')
    text_to_write = ''

    for item in items_list:
        line = ','.join(item)
        line += '\n'
        text_to_write += line
    write_file.write(text_to_write)
    write_file.close()

    # ensure grammar in 'saved' message is correct
    if len(items_list) == 1:
        print('1 item saved to {}'.format(FILE_NAME))
    elif len(items_list) == 0:
        print('No items saved to {}'.format(FILE_NAME))
    else:
        print('{} items saved to {}'.format(len(items_list), FILE_NAME))


def hire_item(items_list):
    """
    Through user input and validation, this function will attempt to change the item from an 'in' state to an 'out'
    state. Basically updating an item in the list to indicated that it has been hired out.
    :param items_list: List of lists containing item information
    :return items_list: List of lists containing item information with the item state
    modified (will be unmodified if the item cannot be hired)
    """
    index_choice_is_valid = False

    index_choice = input('Enter the number of the item to hire\n')
    while not index_choice_is_valid:
        try:
            index_choice = int(index_choice)
            if index_choice >= len(items_list) or index_choice < 0:
                print('Invalid item number')
            else:
                index_choice_is_valid = True
        except ValueError:
            print('Invalid input; enter a valid number')

    if 'out' not in items_list[index_choice][3]:
        items_list[index_choice][3] = 'out'
        print('{} hired for ${:.2f}'.format(items_list[index_choice][0], float(items_list[index_choice][2])))
    else:
        print('That item is not available for hire')
    return items_list


def return_item(items_list):
    """
    Through user input and validation, this function will attempt to change the item from an 'out' state to an 'in'
    state. Basically updating an item in the list to indicated that it has been returned.
    :param items_list: List of lists containing item information
    :return items_list: List of lists containing item information with the item state
    modified (will be unmodified if the item cannot be hired)
    """
    index_choice_is_valid = False

    index_choice = input('Enter the number of the item to return\n')
    while not index_choice_is_valid:
        try:
            index_choice = int(index_choice)
            if index_choice >= len(items_list) or index_choice < 0:
                index_choice = input('Invalid item number\n')
            else:
                index_choice_is_valid = True
        except ValueError:
            index_choice = input('Invalid input; enter a number\n')

    if 'in' not in items_list[index_choice][3]:
        print('{} returned'.format(items_list[index_choice][0]))
        items_list[index_choice][3] = 'in'
        return items_list
        # set the item selected to "in" in items_file
    else:
        print('That item is not on hire')
    return items_list


def outputted_items(items_list, item_flag):
    """
    Prints a formatted, ordered list of specific items to the console based on the item_flag. Returns
    :param items_list: List of lists containing item information
    :param item_flag: 'in', 'out' or 'all'. Used to determine whether to display all items, hired items or returned
    items.
    :return has_item_been_listed: Boolean value that specifies if any items were listed or not
    """
    has_item_been_listed = False

    if item_flag == 'all':
        print('All items on file (* indicates item is currently out):')

    for i, item in enumerate(items_list):
        if item_flag == 'all' or item_flag not in item[3]:
            formatted_items_details = '{} - {:42} = $ {:>6.2f}'.format(
                i, item[0] + ' (' + item[1] + ')', float(item[2]))
            if item_flag == 'all' and 'out' in item[3]:
                print(formatted_items_details, '*')
            else:
                print(formatted_items_details)
            has_item_been_listed = True

    return has_item_been_listed


def add_new_item(items_list):
    """
    Through user input and validation, this function will add a new item to items_list
    :param items_list: List of lists containing item information
    :return items_list: List of lists containing item information with the new item added
    """
    item_name = input('Item name: ')
    while item_name == '':
        print('Input cannot be blank')
        item_name = input('Item name: ')

    item_description = input('Description: ')
    while item_description == '':
        print('Input cannot be blank')
        item_description = input('Description: ')
    price_is_invalid = True
    while price_is_invalid:
        try:
            item_price = input('Price per day: $')
            item_price = float(item_price)
            if item_price < 0:
                print('Price must be >= $0')
                print('Invalid input; enter a valid number')
            else:
                print(item_name, '(' + item_description + '),', '$' + str(item_price), 'now available for hire')
                items_list.append([item_name, item_description, str(item_price), 'in'])
                price_is_invalid = False
        except ValueError:
            print('Invalid input; enter a valid number')
    return items_list


# call main and start the program
main()
