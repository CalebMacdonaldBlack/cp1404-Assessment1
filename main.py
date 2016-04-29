from kivy.app import App
from kivy.app import Builder
from kivy.app import StringProperty
from itemList import ItemList
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import equipmenthireconsole
from State import State

LIST_ITEMS_STATUS_MESSAGE = 'Choose action from the left menu, then select items on the right'
HIRE_ITEMS_STATUS_MESSAGE = 'Hiring No items for $0.00'
RETURN_ITEMS_STATUS_MESSAGE = 'Select available items to return'
ADD_NEW_ITEM_STATUS_MESSAGE = ''

ITEM_OUT_COLOR = [2, 1, 1, 1]
ITEM_IN_COLOR = [1, 2, 1, 1]
ITEM_SELECTED_COLOR = [2,2,2,1]


class HelloKv(App):
    message = StringProperty()
    root = None
    item_list = None
    program_state = None
    item_names_currently_selected = []

    def build(self):
        HelloKv.item_list = ItemList(equipmenthireconsole.create_list_from_file())

        self.title = "Hello world!"
        self.root = Builder.load_file('app.kv')
        HelloKv.root = self.root
        HelloKv.program_state = State.LIST_ITEMS
        for item in HelloKv.item_list.items:
            btn = Button(text=item.name)
            btn.bind(on_release=self.button_released)
            btn.size_hint = (1, None)
            btn.size = (0, 40)
            if item.location == 'out':
                btn.background_color = ITEM_OUT_COLOR
            else:
                btn.background_color = ITEM_IN_COLOR
            self.root.ids.boxLayout_item_buttons.add_widget(btn)
        return self.root

    @staticmethod
    def button_released(self):
        print('click')
        print(HelloKv.program_state)
        print(self.background_color)

        # toggle if return item state
        if self.background_color == ITEM_OUT_COLOR and HelloKv.program_state == State.RETURN_ITEMS:
            self.background_color = ITEM_SELECTED_COLOR
            HelloKv.item_names_currently_selected.append(self.text)
        elif self.background_color == ITEM_SELECTED_COLOR and HelloKv.program_state == State.RETURN_ITEMS:
            self.background_color = ITEM_OUT_COLOR
            HelloKv.item_names_currently_selected.remove(self.text)

        # toggle if hire item state
        elif self.background_color == ITEM_IN_COLOR and HelloKv.program_state == State.HIRE_ITEMS:
            self.background_color = ITEM_SELECTED_COLOR
            HelloKv.item_names_currently_selected.append(self.text)
        elif self.background_color == ITEM_SELECTED_COLOR and HelloKv.program_state == State.HIRE_ITEMS:
            self.background_color = ITEM_IN_COLOR
            HelloKv.item_names_currently_selected.remove(self.text)

        print(HelloKv.item_names_currently_selected)
        """
        HelloKv.item_list.flip_item_location_by_name(self.text)
        item = HelloKv.item_list.find_item_by_name(self.text)
        if item.location == 'out':
            self.background_color = (2,1,1,1)
        else:
            self.background_color = (1,2,1,1)
        print(self.text)
        """

    @staticmethod
    def list_items_released(self):
        HelloKv.unpress_buttons(HelloKv.root)
        HelloKv.root.ids.status_label.text = LIST_ITEMS_STATUS_MESSAGE
        self.state = 'down'
        HelloKv.program_state = State.LIST_ITEMS

    @staticmethod
    def hire_items_released(self):
        HelloKv.unpress_buttons(HelloKv.root)
        HelloKv.root.ids.status_label.text = HIRE_ITEMS_STATUS_MESSAGE
        self.state = 'down'
        HelloKv.program_state = State.HIRE_ITEMS

    @staticmethod
    def return_items_released(self):
        HelloKv.unpress_buttons(HelloKv.root)
        HelloKv.root.ids.status_label.text = RETURN_ITEMS_STATUS_MESSAGE
        self.state = 'down'
        HelloKv.program_state = State.RETURN_ITEMS

    @staticmethod
    def confirm_released(self):
        pass

    @staticmethod
    def add_new_released(self):
        HelloKv.unpress_buttons(HelloKv.root)
        HelloKv.root.ids.status_label.text = ADD_NEW_ITEM_STATUS_MESSAGE
        self.state = 'down'
        HelloKv.program_state = State.ADD_NEW_ITEM

    @staticmethod
    def unpress_buttons(root):
        root.ids.list_items.state = 'normal'
        root.ids.hire_items.state = 'normal'
        root.ids.return_items.state = 'normal'
        root.ids.add_new_item.state = 'normal'


HelloKv().run()
