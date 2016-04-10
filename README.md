# cp1404-Assessment1

## Details
### Caleb Macdonald Black
### 22/March/2015
### https://github.com/CalebMacdonaldBlack/cp1404-Assessment1

## Sudo Code

### load_items()
    function load_items()
        read_file = open and get items.csv file
        items_list = new empty list
    
        for each line in read_file
            item_as_a_list = line converted to list
            append item_as_a_list to items_list
    
        print amount of items loaded and from what file
        close read_file
        return items_list
    
### hire_an_item(items_list)
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
