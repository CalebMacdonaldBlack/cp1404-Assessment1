from kivy.app import App
from kivy.app import Builder
from kivy.app import StringProperty
from itemList import ItemList
from kivy.uix.button import Button
import equipmenthireconsole


class HelloKv(App):
    message = StringProperty()

    def build(self):
        items = ItemList(equipmenthireconsole.create_list_from_file())
        self.title = "Hello world!"
        self.root = Builder.load_file('app.kv')
        btn = Button(text='hello world')
        btn.bind(state=self.button_pressed)
        self.root.add_widget(btn)
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
