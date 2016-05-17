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


class EquipmentHireGui(App):
    status_text = StringProperty()

    def __init__(self):
        super(EquipmentHireGui, self).__init__()
        self.item_list = None  # this wont go into build
        self.program_state = State.LIST_ITEMS
        self.item_list = ItemList()
        self.items_selected_id_and_button_dictionary = {}
        self.status_text = ''

    def build(self):
        self.title = 'Hello World!'
        self.root = Builder.load_file('app.kv')
        for item in self.item_list.items:
            self.add_item_to_display(item)
        # press list_items to engage button and set status text
        self.list_items_pressed(self.root.ids.list_items)
        return self.root

    def item_button_pressed(self, button):
        item = self.item_list.find_item_by_id(button.id)
        # this can all be reduced
        if self.program_state == State.HIRE_ITEMS or self.program_state == State.RETURN_ITEMS:

            if item.location == 'out' and self.program_state == State.RETURN_ITEMS:
                if button.id in self.items_selected_id_and_button_dictionary:
                    button.background_color = ITEM_OUT_COLOR
                    del self.items_selected_id_and_button_dictionary[button.id]
                else:
                    #button.background_color = ITEM_SELECTED_COLOR
                    button.state = 'down'
                    self.items_selected_id_and_button_dictionary[button.id] = button
            elif item.location == 'in' and self.program_state == State.HIRE_ITEMS:
                if button.id in self.items_selected_id_and_button_dictionary:
                    button.background_color = ITEM_IN_COLOR
                    del self.items_selected_id_and_button_dictionary[button.id]
                else:
                    #button.background_color = ITEM_SELECTED_COLOR
                    button.state = 'down'
                    self.items_selected_id_and_button_dictionary[button.id] = button

            self.display_items_selected_in_status()

        elif self.program_state == State.LIST_ITEMS:
            self.status_text = '{} ({}), ${:.2f} is {}'.format(item.name, item.description, item.price, item.location)

    def list_items_pressed(self, button):
        self.release_buttons()
        self.status_text = LIST_ITEMS_STATUS_MESSAGE
        button.state = 'down'
        # empty selected items list
        self.deselect_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.LIST_ITEMS

    def hire_items_pressed(self, button):
        self.release_buttons()
        button.state = 'down'
        # empty selected items list
        self.deselect_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.HIRE_ITEMS
        self.display_items_selected_in_status()

    def return_items_pressed(self, button):
        self.release_buttons()
        self.status_text = RETURN_ITEMS_STATUS_MESSAGE
        button.state = 'down'
        # empty selected items list
        self.deselect_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.program_state = State.RETURN_ITEMS

    def confirm_pressed(self):
        if self.program_state == State.HIRE_ITEMS or self.program_state == State.RETURN_ITEMS:
            for button in self.root.ids.boxLayout_item_buttons.children:

                self.item_list.flip_item_location_by_id(button.id)
                item = self.item_list.find_item_by_id(button.id)
                if item.location == 'in':
                    button.background_color = ITEM_IN_COLOR
                else:
                    button.background_color = ITEM_OUT_COLOR

                self.display_items_selected_in_status()

            # for id, button in self.items_selected_id_and_button_dictionary.items():
            #     self.item_list.flip_item_location_by_id(id)
            #     item = self.item_list.find_item_by_id(button.id)
            #     if item.location == 'in':
            #         button.background_color = ITEM_IN_COLOR
            #     else:
            #         button.background_color = ITEM_OUT_COLOR
            #     self.items_selected_id_and_button_dictionary = {}
            #     self.display_items_selected_in_status()

    def add_new_pressed(self):
        self.release_buttons()
        self.status_text = ADD_NEW_ITEM_STATUS_MESSAGE
        # empty selected items list
        self.deselect_item_buttons()
        self.items_selected_id_and_button_dictionary = {}
        self.root.ids.popup.open()

    def release_buttons(self):
        for button in self.root.ids.menu_buttons.children:
            button.state = 'normal'

    def deselect_item_buttons(self):
        for button in self.root.ids.boxLayout_item_buttons.children:
            button.state = 'normal'

        # for id, button in self.items_selected_id_and_button_dictionary.items():
        #     item = self.item_list.find_item_by_id(id)
        #     if item.location == 'out':
        #         button.background_color = ITEM_OUT_COLOR
        #     else:
        #         button.background_color = ITEM_IN_COLOR

    def display_items_selected_in_status(self):
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
        if self.are_text_fields_valid(name, description, price):
            item = self.item_list.create_and_add_item(name, description, float(price))
            self.add_item_to_display(item)
            self.exit_popup_and_clear_fields()
            # press list_items to engage button and set status text
            self.list_items_pressed(self.root.ids.list_items)

    def are_text_fields_valid(self, name, description, price):
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
        self.root.ids.popup.dismiss()
        self.root.ids.item_name_input.text = ''
        self.root.ids.item_description_input.text = ''
        self.root.ids.item_price_input.text = ''

    def add_item_to_display(self, item):
        btn = Button(text=item.name)
        btn.bind(on_release=self.item_button_pressed)
        btn.size_hint = (1, None)
        btn.size = (0, 40)
        btn.id = 'item_{}'.format(item.index)
        if item.location == 'out':
            btn.background_color = ITEM_OUT_COLOR
        else:
            btn.background_color = ITEM_IN_COLOR
        self.root.ids.boxLayout_item_buttons.add_widget(btn)

    def on_stop(self):
        self.item_list.save_items()

EquipmentHireGui().run()
