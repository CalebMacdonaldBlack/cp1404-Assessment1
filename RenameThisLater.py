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
ALL_ITEMS_ON_HIRE_MESSAGE = "All items are currently on hire"
ENTER_NUMBER_TO_HIRE_MESSAGE = "Enter the number of the item to hire\n"
INVALID_INPUT_ERROR_MESSAGE = "Invalid input; enter a number"
ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE = "That item is not available for hire"
INVALID_MENU_CHOICE_ERROR_MESSAGE = "Invalid menu choice"
ITEM_ALREAD_RETURNED_MESSAGE = "That item has already been returned"


def main():
    items_file = open('items.csv', 'r')
    items_list = items_file.readlines()

    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))

    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':

        if menu_choice == 'L':
            print(LIST_ALL_ITEMS_MESSAGE)

            for i, item in enumerate(items_list):

                item_details = item.split(',')
                # ToDo This isnt how this is done. fix this
                formatted_items_details = '{:<46} = $ {}'.format(
                    str(i) + ' - ' + item_details[0] + ' ' + item_details[1], item_details[2])
                if item_details[3] == 'out\n':
                    print(formatted_items_details, '*')
                else:
                    print(formatted_items_details)
        elif menu_choice == 'H':
            move_item(items_list, 'out\n')
        elif menu_choice == 'R':
            move_item(items_list, 'in\n')
        elif menu_choice == 'L':
            x = 1
            # add_new_item()
        else:
            print(INVALID_MENU_CHOICE_ERROR_MESSAGE)

        menu_choice = input(MENU).upper()
    items_file.close()
    # print amount of items saved to items_file and a fairwell message


def move_item(items_list, where_to_move_item):
    has_item_been_listed = False
    for i, item in enumerate(items_list):
        (name, description, price, location) = item.split(',')
        if location != where_to_move_item:
            formatted_items_details = '{:<46} = $ {}'.format(
                str(i) + ' - ' + name + ' ' + description, price)
            print(formatted_items_details)
            has_item_been_listed = True

    if not has_item_been_listed:
        print(ALL_ITEMS_ON_HIRE_MESSAGE)
    else:
        index_choice_is_a_number = False
        while not index_choice_is_a_number:
            try:
                index_choice = input(ENTER_NUMBER_TO_HIRE_MESSAGE)
                index_choice = int(index_choice)
                index_choice_is_a_number = True
            except ValueError:
                print(INVALID_INPUT_ERROR_MESSAGE)

        (indexed_name, indexed_description, indexed_price, indexed_location) = items_list[index_choice].split(',')

        if indexed_location != where_to_move_item:
            if where_to_move_item == 'out\n':
                print('{} hired  for ${}'.format(indexed_name, indexed_price))
                # set the item selected to "out" in items_file
            else:
                print('{} returned'.format(indexed_name))
                # set the item selected to "in" in items_file
        else:
            if where_to_move_item == 'out\n':
                print(ITEM_NOT_AVAILABLE_FOR_HIRE_MESSAGE)
            else:
                print(ITEM_ALREAD_RETURNED_MESSAGE)


main()
