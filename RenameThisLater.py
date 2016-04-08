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
def save_item(items_list):
    write_file = open(FILE_NAME, 'w')
    text_to_write = ''
    for item in items_list:
        line = ','.join(item)
        line += '\n'
        text_to_write += line
    write_file.write(text_to_write)
    write_file.close()
    print('{} items saved to {}'.format(len(items_list), FILE_NAME))


def main():

    read_file = open(FILE_NAME, 'r')
    items_list = create_list_from_file(read_file)
    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))

    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            output_items(items_list, 'all')
        elif menu_choice == 'H':
            if output_items(items_list, 'out'):
                items_list = hire_item(items_list)
            else:
                print('All items are currently on hire')
        elif menu_choice == 'R':
            if output_items(items_list, 'in'):
                items_list = return_item(items_list)
            else:
                print('No items are currently on hire')
        elif menu_choice == 'A':
            items_list = add_new_item(items_list)
        else:
            print('Invalid menu choice')

        menu_choice = input(
            'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n').upper()
    read_file.close()
    save_item(items_list)
    print('Have a nice day :)')


def create_list_from_file(items_file):

    items_list = []
    for line in items_file.readlines():
        item_as_list = line.split(',')

        if item_as_list[3] == 'in\n':
            item_as_list[3] = 'in'
        elif item_as_list[3] == 'out\n':
            item_as_list[3] = 'out'

        items_list.append(item_as_list)
    print(items_list)
    return items_list


def hire_item(items_list):

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
        print('{} hired for ${}'.format(items_list[index_choice][0], items_list[index_choice][2]))
    else:
        print('That item is not available for hire')
    return items_list


def return_item(items_list):

    index_choice_is_valid = False
    index_choice = input('Enter the number of the item to return\n')
    while not index_choice_is_valid:
        try:
            index_choice = int(index_choice)
            if index_choice >= len(items_list) or index_choice < 0:
                print('Invalid item number')
            else:
                index_choice_is_valid = True
        except ValueError:
            print('Invalid input; enter a valid number')

    if 'in' not in items_list[index_choice][3]:
        print('{} returned'.format(items_list[index_choice][0]))
        items_list[index_choice][3] = 'in'
        return items_list
        # set the item selected to "in" in items_file
    else:
        print('That item has already been returned')
    return items_list


def output_items(items_list, item_flag):

    has_item_been_listed = False
    if item_flag == 'all':
        print('All items on file (* indicates item is currently out):')
    # TODO formatting is all kinds of messed up. needs brackets for desc, 2 decimal places for price and formatting
    for i, item in enumerate(items_list):
        if item_flag == 'all' or item_flag not in item[3]:
            formatted_items_details = '{:<46} = $ {}'.format(
                str(i) + ' - ' + item[0] + ' ' + item[1], item[2])
            if item_flag == 'all' and 'out' in item[3]:
                print(formatted_items_details, '*')
            else:
                print(formatted_items_details)
            has_item_been_listed = True
    return has_item_been_listed


def add_new_item(items_list):

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
                # TODO fix the formatting here. needs 2 decimal places
                print(item_name, '(' + item_description + '),', '$' + str(item_price), 'now available for hire')
                items_list.append(','.join([item_name, item_description, str(item_price), 'in\n']))
                price_is_invalid = False
        except ValueError:
            print('Invalid input; enter a valid number')
    return items_list


main()
