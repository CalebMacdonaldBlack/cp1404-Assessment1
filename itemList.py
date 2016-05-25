from item import Item
import equipmenthireconsole


class ItemList:
    def __init__(self):
        """
        Constructor: Gets all the items from the csv file using the equipmenthireconsole module and appends them the
        item lists's instance of items
        """
        self.items = []
        for i, item_tuple in enumerate(equipmenthireconsole.create_list_from_file()):
            item = Item(item_tuple[0], item_tuple[1], item_tuple[2], item_tuple[3], i)
            self.items.append(item)

    def save_items(self):
        """
        Using the equipmenthireconsole module this saves the items by converting the item instance to a list and
        passes it to the modules save_item function
        """
        item_list = []
        for item in self.items:
            item_as_list = [item.name, item.description, str(item.price), item.location]
            item_list.append(item_as_list)
        equipmenthireconsole.save_item(item_list)

    def flip_item_location_by_id(self, id):
        """
        Changes the location of the item depending on its current location. If the item is 'in' it will change it to
        'out'
        :param id: the id of the item
        """
        item = self.find_item_by_id(id)
        if item.location == 'in':
            item.location = 'out'
        else:
            item.location = 'in'

    def find_item_by_id(self, id):
        """
        Removes the number from the item and returns the item at that index in the items list.
        :param id: The id of the item
        :return: the item instance at the index
        """
        return self.items[int(id.split('_')[1])]

    def create_and_add_item(self, name, description, price, location='in'):
        """
        used to create a new instance of an item and add that to the list of items
        :param name: name of the item
        :param description: short description of the item
        :param price: price of the item
        :param location: whether the item is in or out
        :return: returns the new item instance
        """
        item = Item(name, description, price, location, len(self.items))
        self.items.append(item)
        return item
