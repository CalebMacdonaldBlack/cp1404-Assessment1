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
MENU = 'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n'
LIST_ALL_ITEMS_MESSAGE = 'All items on file (* indicates item is currently out):'
ALL_ITEMS_ON_HIRE_MESSAGE = 'All items are currently on hire'
ENTER_NUMBER_TO_HIRE_MESSAGE = 'Enter the number of the item to hire\n'
INVALID_INPUT_ERROR_MESSAGE = 'Invalid input; enter a number'
ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE = 'That item is not available for hire'
INVALID_MENU_CHOICE_ERROR_MESSAGE = 'Invalid menu choice'
ITEM_ALREAD_RETURNED_MESSAGE = 'That item has already been returned'
INVALID_INDEX_ERROR_MESSAGE = 'Invalid item number'
GET_ITEM_NAME_MESSAGE = 'Item name: '
NAME_IS_BLANK_ERROR_MESSAGE = 'Invalid name'
GET_ITEM_DESCRIPTION_MESSAGE = 'Description: '
DESCRIPTION_IS_BLANK_ERROR_MESSAGE = 'Invalid description'
GET_ITEM_PRICE_MESSAGE = 'Price per day: $'


def main():
    items_file = open('items.csv', 'r')
    items_list = items_file.readlines()

    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))

    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':

        if menu_choice == 'L':
            output_items(items_list, None, True)
        elif menu_choice == 'H':
            items_list = move_item_in_list(items_list, 'out\n')
        elif menu_choice == 'R':
            items_list = move_item_in_list(items_list, 'in\n')
        elif menu_choice == 'A':
            items_list = add_new_item(items_list)
        else:
            print(INVALID_MENU_CHOICE_ERROR_MESSAGE)

        menu_choice = input(MENU).upper()
    items_file.close()
    # print amount of items saved to items_file and a farewell message


def move_item_in_list(items_list, where_to_move_item):
    has_item_been_listed = False
    has_item_been_listed = output_items(items_list, where_to_move_item, False)

    if not has_item_been_listed:
        print(ALL_ITEMS_ON_HIRE_MESSAGE)
    else:
        index_choice_is_valid = False
        index_choice = input(ENTER_NUMBER_TO_HIRE_MESSAGE)
        while not index_choice_is_valid:
            try:
                index_choice = int(index_choice)
                if index_choice >= len(items_list) or index_choice < 0:
                    print(INVALID_INDEX_ERROR_MESSAGE)
                    index_choice = input(ENTER_NUMBER_TO_HIRE_MESSAGE)
                else:
                    index_choice_is_valid = True
            except ValueError:
                print(INVALID_INPUT_ERROR_MESSAGE)
                index_choice = input(ENTER_NUMBER_TO_HIRE_MESSAGE)

        (indexed_name, indexed_description, indexed_price, indexed_location) = items_list[index_choice].split(',')

        if indexed_location != where_to_move_item:
            if where_to_move_item == 'out\n':
                print('{} hired for ${}'.format(indexed_name, indexed_price))
                items_list[index_choice] = items_list[index_choice].replace('in\n', where_to_move_item)
                # set the item selected to "out" in items_file
            else:
                print('{} returned'.format(indexed_name))
                items_list[index_choice] = items_list[index_choice].replace('out\n', where_to_move_item)
                return items_list
                # set the item selected to "in" in items_file
        else:
            if where_to_move_item == 'out\n':
                print(ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE)
            else:
                print(ITEM_ALREAD_RETURNED_MESSAGE)
    return items_list


def output_items(items_list, where_to_move_item, display_all_items):
    has_item_been_listed = False
    for i, item in enumerate(items_list):
        (name, description, price, location) = item.split(',')
        if display_all_items or location != where_to_move_item:
            formatted_items_details = '{:<46} = $ {}'.format(
                str(i) + ' - ' + name + ' ' + description, price)
            if display_all_items and location == 'out\n':
                print(formatted_items_details, '*')
            else:
                print(formatted_items_details)
            has_item_been_listed = True
    return has_item_been_listed


def add_new_item(items_list):
    item_name = input(GET_ITEM_NAME_MESSAGE)
    while item_name == '':
        print(NAME_IS_BLANK_ERROR_MESSAGE)
        item_name = input(GET_ITEM_NAME_MESSAGE)

    item_description = input(GET_ITEM_DESCRIPTION_MESSAGE)
    while item_description == '':
        print(DESCRIPTION_IS_BLANK_ERROR_MESSAGE)
        item_description = input(GET_ITEM_DESCRIPTION_MESSAGE)
    price_is_invalid = True
    while price_is_invalid:
        try:
            item_price = input(GET_ITEM_PRICE_MESSAGE)
            item_price = float(item_price)
            items_list.append(','.join([item_name, item_description, str(item_price), 'in\n']))
            price_is_invalid = False
        except ValueError:
            print(INVALID_INPUT_ERROR_MESSAGE)
    return items_list


main()
