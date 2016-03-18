"""

function main()
    get items_file from items.csv file

    print welcome message with author name

    display menu
    get menu choice from user
    while choice isn't q

        if choice is l
            print "All items on file (* indicates item is currently out):"
            for item in item_file
                print item removing commas, add selection index, format neatly and adding astrix if item is out
        else if choice is h
                                                            item_list = return of display_and_get_item_list(choice, items_file)
                                                            if item_list contains values
            hire_item(items_file)
                                                            else
                                                                print "All items are currently on hire"
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
    print amount of items saved to items_file

                                                            function display_and_get_item_list(choice, items_file)
                                                                define new items list
                                                                set index to 1
                                                                for each item in items_file
                                                                    put item in items

                                                                output_items(items, choice)
                                                                return items

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
            


    if

function return_item(items)

                                                function output_items(items, choice)
                                                    if choice is a
                                                        print "All items on file (* indicates item is currently out):"
                                                    for each item in items
                                                        if choice is a
                                                            print item removing commas, add selection index, format neatly and adding astrix if item is out
                                                        else
                                                        if item is able to be chosen
                                                            print item removing commas, add selection index, format neatly
"""