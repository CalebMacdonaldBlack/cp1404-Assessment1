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

# TODO organize this mess
PROGRAM_NAME = 'Items for Hire'
AUTHOR = 'Caleb Macdonald Black'
MENU = 'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n'
LIST_ALL_ITEMS_MESSAGE = 'All items on file (* indicates item is currently out):'
ALL_ITEMS_ON_HIRE_MESSAGE = 'All items are currently on hire'
ENTER_NUMBER_TO_HIRE_MESSAGE = 'Enter the number of the item to hire\n'
ALL_ITEMS_RETURNED_MESSAGE = 'No items are currently on hire'
ENTER_NUMBER_TO_RETURN_MESSAGE = 'Enter the number of the item to return\n'
INVALID_INPUT_ERROR_MESSAGE = 'Invalid input; enter a valid number'
ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE = 'That item is not available for hire'
INVALID_MENU_CHOICE_ERROR_MESSAGE = 'Invalid menu choice'
ITEM_ALREADY_RETURNED_MESSAGE = 'That item is not on hire'
INVALID_INDEX_ERROR_MESSAGE = 'Invalid item number'
GET_ITEM_NAME_MESSAGE = 'Item name: '
INPUT_IS_BLANK_ERROR_MESSAGE = 'Input cannot be blank'
GET_ITEM_DESCRIPTION_MESSAGE = 'Description: '
GET_ITEM_PRICE_MESSAGE = 'Price per day: $'
PRICE_TOO_SMALL_ERROR_MESSAGE = 'Price must be >= $0'


# TODO change items.csv file to original one
def main():
    items_file = open('items.csv', 'r')
    items_list = items_file.readlines()

    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))

    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':

        if menu_choice == 'L':
            output_items(items_list, display_all_items=True)
        elif menu_choice == 'H':
            items_list = move_item_in_list(items_list, 'out')
        elif menu_choice == 'R':
            items_list = move_item_in_list(items_list, 'in')
        elif menu_choice == 'A':
            items_list = add_new_item(items_list)
        else:
            print(INVALID_MENU_CHOICE_ERROR_MESSAGE)

        menu_choice = input(MENU).upper()
    items_file.close()
    # TODO print amount of items saved to items_file and a farewell message


def move_item_in_list(items_list: list, where_to_move_item: str) -> list:
    """
    Determines from user input what item should be moved and sets it to 'in' or 'out' depending on the specified param

    :param items_list: A list of Strings in csv format that contains the information for the items that can be hired
    :param where_to_move_item: Whether the item will be in or out. eg. 'in' or 'out'
    :return: Updated list with item moved
    """

    has_item_been_listed = False
    has_item_been_listed = output_items(items_list, item_in_or_out=where_to_move_item)
    if where_to_move_item == 'in':
        enter_number_message = ENTER_NUMBER_TO_RETURN_MESSAGE
        no_items_to_display_message = ALL_ITEMS_RETURNED_MESSAGE
        cannot_return_message = ITEM_ALREADY_RETURNED_MESSAGE
    else:
        enter_number_message = ENTER_NUMBER_TO_HIRE_MESSAGE
        no_items_to_display_message = ALL_ITEMS_ON_HIRE_MESSAGE
        cannot_return_message = ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE

    if not has_item_been_listed:
        print(no_items_to_display_message)
    else:
        index_choice_is_valid = False
        index_choice = input(enter_number_message)
        while not index_choice_is_valid:
            try:
                index_choice = int(index_choice)
                if index_choice >= len(items_list) or index_choice < 0:
                    print(INVALID_INDEX_ERROR_MESSAGE)
                else:
                    index_choice_is_valid = True
            except ValueError:
                print(INVALID_INPUT_ERROR_MESSAGE)

        (indexed_name, indexed_description, indexed_price, indexed_location) = items_list[index_choice].split(',')

        if where_to_move_item not in indexed_location:
            if where_to_move_item == 'out':
                items_list[index_choice] = ','.join(
                    [indexed_name, indexed_description, indexed_price, where_to_move_item + '\n'])
                print('{} hired for ${}'.format(indexed_name, indexed_price))
                # set the item selected to "out" in items_file
            else:
                print('{} returned'.format(indexed_name))
                items_list[index_choice] = ','.join(
                    [indexed_name, indexed_description, indexed_price, where_to_move_item + '\n'])

                return items_list
                # set the item selected to "in" in items_file
        else:
            print(cannot_return_message)
    return items_list


def output_items(items_list: list, item_in_or_out: str = None, display_all_items: bool = False) -> bool:
    """
    Displays the list of 'in' items or 'out' items. Will display all items if display_all_items is true

    :param items_list: A list of Strings in csv format that contains the information for the items that can be hired
    :param item_in_or_out: Items to display. eg. 'in\n' or 'out\n'. Will not be used if display_all_items is True and
    can be set to None
    :param display_all_items: Boolean to override item_in_or_out and display all the items
    :return: Boolean to determine whether or not an item was displayed
    """
    has_item_been_listed = False
    if display_all_items:
        print('All items on file (* indicates item is currently out):')
    # TODO formatting is all kinds of messed up. needs brackets for desc, 2 decimal places for price and formatting
    for i, item in enumerate(items_list):
        (name, description, price, location) = item.split(',')
        if display_all_items or item_in_or_out not in location:
            formatted_items_details = '{:<46} = $ {}'.format(
                str(i) + ' - ' + name + ' ' + description, price)
            if display_all_items and 'out' in location:
                print(formatted_items_details, '*')
            else:
                print(formatted_items_details)
            has_item_been_listed = True
    return has_item_been_listed


def add_new_item(items_list: list) -> list:
    # TODO lists are immutable. do i need to return this?
    """
    Adds a new item to the list of items through user input

    :param items_list: A list of Strings in csv format that contains the information for the items that can be hired
    :return: Updated list with item added
    """
    item_name = input(GET_ITEM_NAME_MESSAGE)
    while item_name == '':
        print(INPUT_IS_BLANK_ERROR_MESSAGE)
        item_name = input(GET_ITEM_NAME_MESSAGE)

    item_description = input(GET_ITEM_DESCRIPTION_MESSAGE)
    while item_description == '':
        print(INPUT_IS_BLANK_ERROR_MESSAGE)
        item_description = input(GET_ITEM_DESCRIPTION_MESSAGE)
    price_is_invalid = True
    while price_is_invalid:
        try:
            item_price = input(GET_ITEM_PRICE_MESSAGE)
            item_price = float(item_price)
            if item_price < 0:
                print(PRICE_TOO_SMALL_ERROR_MESSAGE)
                print(INVALID_INPUT_ERROR_MESSAGE)
            else:
                # TODO fix the formatting here. needs 2 decimal places
                print(item_name, '(' + item_description + '),', '$' + str(item_price), 'now available for hire')
                items_list.append(','.join([item_name, item_description, str(item_price), 'in\n']))
                price_is_invalid = False
        except ValueError:
            print(INVALID_INPUT_ERROR_MESSAGE)
    return items_list


main()
