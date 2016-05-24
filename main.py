from kivy.app import App
from kivy.app import Builder
from kivy.app import StringProperty
from itemList import ItemList
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import equipmenthireconsole
from State import State

LIST_ITEMS_STATUS_MESSAGE = 'Choose action from the left menu, then select items on the right'
RETURN_ITEMS_STATUS_MESSAGE = 'Select available items to return'
ADD_NEW_ITEM_STATUS_MESSAGE = 'Enter details for new item'

ITEM_OUT_COLOR = [2, 1, 1, 1]  # Red
ITEM_IN_COLOR = [1, 2, 1, 1]  # Green
ITEM_SELECTED_COLOR = [2, 2, 2, 1]  # Light Grey

# TODO is this name correct?
TITLE = 'Equipment Hire Gui'
KV_FILE_NAME = 'app.kv'


class EquipmentHireGui(App):
    status_text = StringProperty()

    def __init__(self):
        """
        Constructor
        Initializes variables
        """
        super(EquipmentHireGui, self).__init__()
        self.item_list = None  # this wont go into build
        self.program_state = State.LIST_ITEMS
        self.item_list = ItemList()
        self.items_selected_id_and_button_dictionary = {}
        self.status_text = ''

    def build(self):
        self.title = TITLE
        self.root = Builder.load_file(KV_FILE_NAME)

        # add all items to the display
        for item in self.item_list.items:
            self.add_item_to_display(item)

        # press list_items to engage button and set status text
        self.list_items_pressed(self.root.ids.list_items)
        return self.root

    def item_button_pressed(self, button):
        """
        Invoked when an item button is pressed. This will select the item that was pressed
        :param button:
        :return:
        """
        item = self.item_list.find_item_by_id(button.id)
        # this can all be reduced
        if self.program_state == State.HIRE_ITEMS or self.program_state == State.RETURN_ITEMS:

            if item.location == 'out' and self.program_state == State.RETURN_ITEMS:
                if button.id in self.items_selected_id_and_button_dictionary:
                    button.background_color = ITEM_OUT_COLOR
                    del self.items_selected_id_and_button_dictionary[button.id]
                else:
                    # button.background_color = ITEM_SELECTED_COLOR
                    button.state = 'down'
                    self.items_selected_id_and_button_dictionary[button.id] = button
            elif item.location == 'in' and self.program_state == State.HIRE_ITEMS:
                if button.id in self.items_selected_id_and_button_dictionary:
                    button.background_color = ITEM_IN_COLOR
                    del self.items_selected_id_and_button_dictionary[button.id]
                else:
                    # button.background_color = ITEM_SELECTED_COLOR
                    button.state = 'down'
                    self.items_selected_id_and_button_dictionary[button.id] = button

            self.display_items_selected_in_status()

        elif self.program_state == State.LIST_ITEMS:
            self.status_text = '{} ({}), ${:.2f} is {}'.format(item.name, item.description, item.price, item.location)

    def list_items_pressed(self, button):
        """
        Invoked when the 'list items' button is pressed on the gui. Updates the programs state to 'LIST_ITEMS'.
        :param button: The button that was pressed
        """
        self.release_menu_buttons()
        self.status_text = LIST_ITEMS_STATUS_MESSAGE
        button.state = 'down'
        # empty selected items list
        self.release_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.LIST_ITEMS

    def hire_items_pressed(self, button):
        """
        Invoked when the 'hire item' button is pressed on the gui. Updates the programs state to 'HIRE_ITEMS'.
        :param button: The button that was pressed
        """
        self.release_menu_buttons()
        button.state = 'down'
        # empty selected items list
        self.release_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.HIRE_ITEMS
        self.display_items_selected_in_status()

    def return_items_button_pressed(self, button):
        """
        Invoked when the 'return item' button is pressed on the gui. Updates the programs state to 'RETURN_ITEMS'.
        :param button: The button that was pressed
        """
        self.release_menu_buttons()
        self.status_text = RETURN_ITEMS_STATUS_MESSAGE
        button.state = 'down'
        # empty selected items list
        self.release_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.RETURN_ITEMS

    def confirm_button_pressed(self):
        """
        This is used to flip the location of the items that are selected and update the location property of the items
        selected. This will also update the background color of item.
        """
        if self.program_state == State.HIRE_ITEMS or self.program_state == State.RETURN_ITEMS:
            for button in self.root.ids.boxLayout_item_buttons.children:
                if button.state == 'down':
                    button.state = 'normal'
                    self.item_list.flip_item_location_by_id(button.id)
                    item = self.item_list.find_item_by_id(button.id)

                    if item.location == 'in':
                        button.background_color = ITEM_IN_COLOR
                    else:
                        button.background_color = ITEM_OUT_COLOR

                    self.display_items_selected_in_status()

    def add_new_button_pressed(self):
        """
        Invoked when the 'add new' button is pressed on the gui. This will open a popup window for adding a new item
        :return:
        """
        self.release_menu_buttons()
        self.status_text = ADD_NEW_ITEM_STATUS_MESSAGE
        # empty selected items list
        self.release_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.root.ids.popup.open()

    def release_menu_buttons(self):
        """
        releases (deselects) all menu buttons. Used when changing states.
        """
        for button in self.root.ids.menu_buttons.children:
            button.state = 'normal'

    def release_item_buttons(self):
        """
        releases (deselects) all item buttons. Mostly used when changing states.
        """
        for button in self.root.ids.boxLayout_item_buttons.children:
            button.state = 'normal'

    def display_items_selected_in_status(self):
        """
        Used to display information about the current item/s selected. displayed information will change depending on
        the current state of the program and what is selected.
        """
        price = 0
        selected_item_names = []
        for id, button in self.items_selected_id_and_button_dictionary.items():
            item = self.item_list.find_item_by_id(id)
            price += item.price
            selected_item_names.append(self.item_list.find_item_by_id(id).name)

        if self.program_state == State.HIRE_ITEMS:
            self.status_text = 'Hiring: {} for ${:.2f}'.format(', '.join(selected_item_names) or 'No items', price)
        elif self.program_state == State.RETURN_ITEMS:
            if selected_item_names:
                self.status_text = 'Returning: {}'.format(
                    ', '.join(selected_item_names) or 'Select available items to return')
            else:
                self.status_text = 'Select available items to return'

    def save_pressed(self, name, description, price):
        """
        Invoked when the save button is pressed on the 'create item' popup. if all fields are valid, it will create
        and add the new item to the item list. It will also call the function to add the item to the item list gui, and
        dismiss the popup window
        :param name:
        :param description:
        :param price:
        """
        if self.are_text_fields_valid(name, description, price):
            item = self.item_list.create_and_add_item(name, description, float(price))
            self.add_item_to_display(item)
            self.exit_popup_and_clear_fields()
            # press list_items to engage button and set status text
            self.list_items_pressed(self.root.ids.list_items)

    def are_text_fields_valid(self, name, description, price):
        """
        Returns whether or not the text fields are valid as a boolean. Updates the status text label with the current
        error message
        :param name: name value of the item
        :param description: description value for the item
        :param price: price of the item
        :return : True if all fields are valid and false if any of the fields aren't valid
        """
        # TODO is it a bad idea for this function update the status text and return a boolean? should I separate this?
        # TODO Should I separate this into multiple verification functions?
        if name == '' or description == '' or price == '':
            self.status_text = 'All fields must be completed'
            return False
        try:
            if float(price) >= 0:
                return True
            else:
                self.status_text = 'Price must not be negative'
                return False
        except ValueError:
            self.status_text = 'Price must be a valid number'
            return False

    def exit_popup_and_clear_fields(self):
        """
        Clears the values of the item field widgets and dismisses (exits) the 'create item' popup window
        """
        self.root.ids.popup.dismiss()
        self.root.ids.item_name_input.text = ''
        self.root.ids.item_description_input.text = ''
        self.root.ids.item_price_input.text = ''

    def add_item_to_display(self, item):
        """
        Creates buttons for each item and add it to the item list in the gui. Sets the background color of that button
        to green if the item is able to be hired (in) and to red if the item is not able to be hired (out)
        :param item: The item instance that contains all the properties of the item button
        """
        btn = Button(text=item.name)
        btn.bind(on_release=self.item_button_pressed)
        btn.size_hint = (1, None)
        btn.size = (0, 40)

        # ID assigned to allow items with the same name and avoid weird behaviour
        btn.id = 'item_{}'.format(item.index)

        if item.location == 'out':
            btn.background_color = ITEM_OUT_COLOR
        else:
            btn.background_color = ITEM_IN_COLOR

        self.root.ids.boxLayout_item_buttons.add_widget(btn)

    def on_stop(self):
        """
        Invokes the save function on the item_list to save all the items and their current properties to the csv file
        """
        self.item_list.save_items()


EquipmentHireGui().run()
