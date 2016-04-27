from kivy.app import App
from kivy.app import Builder
from kivy.app import StringProperty


class HelloKv(App):
    message = StringProperty()

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('app.kv')
        return self.root

    def button_pressed(self, button_type):
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
