from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import *


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.item_list = ItemList()
        self.instance_down = [] # placeholder for selected items
        read_items = open('items.csv', 'r+')
        # read_items = open('items.csv', 'a') --> io.UnsupportedOperation: not readable


    def build(self):
        self.title = "My App"
        self.root = Builder.load_file('app.kv')
        self.itemlist()
        return self.root

    def itembuttons(self):
        file = open('items.csv', 'r')
        for each_line in file:
            name, item_desc, cost, status = each_line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0, 0.9, 1))
            temp_button.bind(on_press=self.press_item)
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
        self.itembuttons()

    def itemreturn(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.itembuttons()

    def itemhire(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (0, 0.5, 0.8, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.itembuttons()

    def additem(self):
        self.root.ids.popup.open()

    def saveitem(self, name, item_desc, cost):

        def valid(cost):
            try:
                float(cost)
                return True
            except ValueError:
                return False

        if len(self.root.ids.iteminput.text.strip()) == 0 or len(self.root.ids.descinput.text.strip()) == 0 or len(
                self.root.ids.ppdinput.text.strip()) == 0:
            self.root.ids.popup_label.text = "All fields must be completed"
        elif valid(cost) == False:
            self.press_cancel()
            self.root.ids.popup_label.text = "Price must be valid number"
        elif valid(cost) == True and float(
                self.root.ids.ppdinput.text) < 0:
            self.press_cancel()
            self.root.ids.popup_label.text.text = "Price cannot be negative"
        else:
            add_item = "\n{},{},{},in".format(name, item_desc, cost)
            with open("items.csv", "a") as file:
                file.writelines(add_item)
            print('Writing success')
            self.press_cancel()
            self.exit_popup()
            self.itemlist()

    def exit_popup(self):
        self.root.ids.popup.dismiss()

    def press_cancel(self):
        self.root.ids.iteminput.text = ""
        self.root.ids.descinput.text = ""
        self.root.ids.ppdinput.text = ""
        self.root.ids.popup_label.text = "Enter details for new item"

    def press_item(self, instance):
        file = open('items.csv', 'r')
        for line in file:
            name, item_desc, cost, status = line.split(",")
            if instance.text == name:
                if self.root.ids.list_button.background_color == [0, 0.5, 0.8, 1]:
                    self.root.ids.label.text = "{} ({}), ${} is {}".format(name, item_desc, float(cost), status)
                elif self.root.ids.hire_button.background_color == [0, 0.5, 0.8, 1]:
                    if "in" in status:
                        self.root.ids.label.text = "Hiring: {} for ${}".format(name, float(cost))
                    else:
                        self.root.ids.label.text = "Cannot hire that item"
                elif self.root.ids.return_button.background_color == [0, 0.5, 0.8, 1]:
                    if "out" in status:
                        self.root.ids.label.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.label.text = "Cannot return that item"


MyApp().run()