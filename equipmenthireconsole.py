"""
Caleb Macdonald Black
22/March/2015
https://github.com/CalebMacdonaldBlack/cp1404-Assessment1
"""

PROGRAM_NAME = 'Items for Hire'
AUTHOR = 'Caleb Macdonald Black'
FILE_NAME = 'items.csv'
MENU = 'Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit\n'


def main():
    """
    Main function: This calls the necessary functions to load the csv file, display menu and handle menu interaction
    from the user and save the updated information to the csv file before exiting
    """
    print('{} - by {}'.format(PROGRAM_NAME, AUTHOR))

    items_list = create_list_from_file()

    menu_choice = input(MENU + '>>> ').upper()
    while menu_choice != 'Q':

        if menu_choice == 'L':
            output_all_items(items_list)

        elif menu_choice == 'H':
            items_list = hire_item(items_list)

        elif menu_choice == 'R':
            items_list = return_item(items_list)

        elif menu_choice == 'A':
            items_list = add_new_item(items_list)

        else:
            print('Invalid menu choice')

        menu_choice = input(MENU + '>>> ').upper()
    save_item(items_list)
    print('Have a nice day :)')


"""
function load_items()
    read_file = open and get items.csv file
    items_list = new empty list

    for each line in read_file
        item_as_a_list = line converted to list
        append item_as_a_list to items_list

    print amount of items loaded and from what file
    close read_file
    return items_list
"""


def create_list_from_file():
    """
    Reads the file and returns a list of items as lists. This will also print to the console the amount of items loaded
    :return items_list: All Item information converted to a list and appended to another list
    """
    items_file = open(FILE_NAME, 'r')
    items_list = []

    for line in items_file.readlines():
        item_as_list = line.split(',')
        item_as_list[3] = item_as_list[3].replace('\n', '')
        item_as_list[2] = float(item_as_list[2])
        items_list.append(tuple(item_as_list))

    # ensure grammar in 'loaded' message is correct
    if len(items_list) == 1:
        print('1 item loaded from {}'.format(FILE_NAME))
    elif len(items_list) == 0:
        print('No items loaded from {}'.format(FILE_NAME))
    else:
        print('{} items loaded from {}'.format(len(items_list), FILE_NAME))

    items_file.close()
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


"""
function hire_an_item(items_list)
    was_item_listed = false

    for each item in items_list
        if item state is 'in'
            print item with item index
            was_item_listed = true

    choice = get index from user

    choice_valid = true
    while choice_valid = false
        try
            convert choice to integer
            if choice is between 0 and the number of items minus 1
                choice_valid = true
            else
                print not in range error and get choice again
        catch a valueError
            print not a number error and get choice again
    if item state is 'in'
        print item hired
    else
        print not able to be hired error
    return items_list

"""


def hire_item(items_list):
    """
    Through user input and validation, this function will attempt to change the item from an 'in' state to an 'out'
    state. Basically updating an item in the list to indicated that it has been hired out.
    :param items_list: List of lists containing item information
    :return items_list: List of lists containing item information with the item state
    modified (will be unmodified if the item cannot be hired)
    """

    has_item_been_listed = False
    for i, item in enumerate(items_list):
        if 'out' not in item[3]:
            formatted_items_details = '{} - {:42} = $ {:>6.2f}'.format(
                i, item[0] + ' (' + item[1] + ')', item[2])
            print(formatted_items_details)
            has_item_been_listed = True

    if not has_item_been_listed:
        print('All items are currently on hire')
        return items_list

    index_choice_is_valid = False

    index_choice = input('Enter the number of an item to hire\n>>> ')
    while not index_choice_is_valid:
        try:
            index_choice = int(index_choice)
            if index_choice >= len(items_list) or index_choice < 0:
                index_choice = input('Invalid item number\n>>> ')
            else:
                index_choice_is_valid = True
        except ValueError:
            index_choice = input('Invalid input; enter a number\n>>> ')

    if 'out' not in items_list[index_choice][3]:
        items_list[index_choice] = (
            items_list[index_choice][0], items_list[index_choice][1], items_list[index_choice][2], 'out')
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

    has_item_been_listed = False
    for i, item in enumerate(items_list):
        if 'in' not in item[3]:
            formatted_items_details = '{} - {:42} = $ {:>6.2f}'.format(
                i, item[0] + ' (' + item[1] + ')', item[2])
            print(formatted_items_details)
            has_item_been_listed = True

    if not has_item_been_listed:
        print('No items are currently on hire')
        return items_list

    index_choice_is_valid = False

    index_choice = input('Enter the number of an item to return\n>>> ')
    while not index_choice_is_valid:
        try:
            index_choice = int(index_choice)
            if index_choice >= len(items_list) or index_choice < 0:
                index_choice = input('Invalid item number\n>>> ')
            else:
                index_choice_is_valid = True
        except ValueError:
            index_choice = input('Invalid input; enter a number\n>>> ')

    if 'in' not in items_list[index_choice][3]:
        print('{} returned'.format(items_list[index_choice][0]))
        items_list[index_choice] = (
            items_list[index_choice][0], items_list[index_choice][1], items_list[index_choice][2], 'in')
        return items_list
        # set the item selected to "in" in items_file
    else:
        print('That item is not on hire')
    return items_list


def output_all_items(items_list):
    """
    Prints a formatted, ordered list of all items to the console.
    :param items_list: List of lists containing item information
    """
    has_item_been_listed = False
    print('All items on file (* indicates item is currently out):')

    for i, item in enumerate(items_list):
        formatted_items_details = '{} - {:42} = $ {:>6.2f}'.format(
            i, item[0] + ' (' + item[1] + ')', item[2])
        if 'out' in item[3]:
            print(formatted_items_details, '*')
        else:
            print(formatted_items_details)
        has_item_been_listed = True

    if not has_item_been_listed:
        print('There are currently no items')


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
            item_price = float(input('Price per day: $'))
            if item_price < 0:
                print('Price must be >= $0')
                print('Invalid input; enter a valid number')
            else:
                print('{} ({}), ${:.2f} now available for hire'.format(item_name, item_description, item_price))
                items_list.append((item_name, item_description, item_price, 'in'))
                price_is_invalid = False
        except ValueError:
            print('Invalid input; enter a valid number')
    return items_list


# call main and start the program
if __name__ == '__main__':
    main()
