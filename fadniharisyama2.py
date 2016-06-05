from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)


    def build(self):
        self.title = "My App"
        self.root = Builder.load_file('app.kv')
        self.itemlist()
        return self.root

    def create_buttons(self):
        file = open('items.csv', 'r')
        for each_line in file:
            name, item_desc, cost, status = each_line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0, 0.9, 1))
            self.root.ids.items_buttons.add_widget(temp_button)
        file.close()

    def itemlist(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def itemreturn(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def itemhire(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def additem(self):
        self.root.ids.popup.open()

    def saveitem(self, name, item_desc, cost):
        add_item = "\n{},{},{},in".format(name, item_desc, cost)
        with open("items.csv", "a") as file:
            file.writelines(add_item)
        print('Writing success')
        self.exit_popup()
        self.itemlist()

    def exit_popup(self):
        self.root.ids.popup.dismiss()

    def press_cancel(self):
        self.root.ids.iteminput.text = ""
        self.root.ids.descinput.text = ""
        self.root.ids.ppdinput.text = ""
        self.root.ids.popup_label.text = "Enter details for new item"

MyApp().run()