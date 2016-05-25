class Item:
    def __init__(self, name, description, price, location, id):
        """
        Item instance for each item and all its information
        :param name: name of the item
        :param description: short information about the item
        :param price:  price of the item
        :param location: whether the item is 'in' or 'out'
        :param id: id for distinguishing between two items that are the same
        :return:
        """
        self.name = name
        self.description = description
        self.price = price
        self.location = location
        self.index = id
