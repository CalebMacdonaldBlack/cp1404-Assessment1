from item import Item
import equipmenthireconsole


class ItemList:
    def __init__(self):
        self.items = []
        for i, item_tuple in enumerate(equipmenthireconsole.create_list_from_file()):
            item = Item(item_tuple[0], item_tuple[1], item_tuple[2], item_tuple[3], i)
            self.items.append(item)

    def save_items(self):
        item_list = []
        for item in self.items:
            item_as_list = [item.name, item.description, str(item.price), item.location]
            item_list.append(item_as_list)
        equipmenthireconsole.save_item(item_list)

    def flip_item_location_by_id(self, id):
        item = self.find_item_by_id(id)
        if item.location == 'in':
            item.location = 'out'
        else:
            item.location = 'in'

    def find_item_by_id(self, id):
        # Remove the index from the id and return that item from the 'items' list
        return self.items[int(id.split('_')[1])]

    def create_and_add_item(self, name, description, price, location='in'):
        item = Item(name, description, price, location, len(self.items))
        self.items.append(item)
        return item
