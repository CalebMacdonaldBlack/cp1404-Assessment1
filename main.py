from kivy.app import App
from kivy.app import Builder
from kivy.app import StringProperty
from itemList import ItemList
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import equipmenthireconsole


class HelloKv(App):
    message = StringProperty()

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('app.kv')

        item_list = ItemList(equipmenthireconsole.create_list_from_file())
        for item in item_list.items:
            btn = Button(text=item.name)
            btn.bind(state=self.button_pressed)
            btn.size_hint = (1, None)
            btn.size = (0, 40)
            self.root.ids.boxLayout_item_buttons.add_widget(btn)
        return self.root

    @staticmethod
    def button_pressed(self, button_type):
        print('hello')
        if button_type == 'list_items':
            print('list_items')
        elif button_type == 'hire_items':
            print('hire_items')
        elif button_type == 'return_items':
            print('return_items')
        elif button_type == 'confirm':
            print('confirm')
        elif button_type == 'add_new_items':
            print(button_type)


HelloKv().run()
