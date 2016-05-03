from item import Item


class ItemList:
    def __init__(self, item_list):
        self.items = []
        for item_tuple in item_list:
            item = Item(item_tuple[0], item_tuple[1], item_tuple[2], item_tuple[3])
            self.items.append(item)

    def flip_item_location_by_name(self, name):
        for item in self.items:
            if item.name.upper() == name.upper():
                if item.location == 'in':
                    item.location = 'out'
                else:
                    item.location = 'in'
                return
        raise ValueError('Cannot find item with the name', name)

    def find_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        raise ValueError('Cannot find item with the name', name)

    def create_and_add_item(self, name, description, price, location='in'):
        item = Item(name, description, price, location)
        self.items.append(item)
        return item
