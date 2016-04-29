from item import Item


class ItemList:
    def __init__(self, item_list):
        self.items = []
        for item_tuple in item_list:
            item = Item(item_tuple[0], item_tuple[1], item_tuple[2], item_tuple[3])
            self.items.append(item)
