from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.items_listed = open("items.csv", "r+")


    def build(self):
        self.title = "My App"
        self.root = Builder.load_file('app.kv')
        self.itemlist()
        return self.root

    def create_buttons(self):
        for each_line in self.items_listed:
            name, item_desc, cost, status = each_line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0, 0.9, 1))
            self.root.ids.items_buttons.add_widget(temp_button)

    def itemlist(self):
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def itemreturn(self):
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (1, 1, 1, 1)
        self.root.ids.return_item.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def itemhire(self):
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = (1, 1, 1, 1)
        self.root.ids.hire_item.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.return_item.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

MyApp().run()