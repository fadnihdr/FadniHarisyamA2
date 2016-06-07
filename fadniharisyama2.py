from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import *

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.item_list = ItemList()                                 # (1)
        open_csv = open("items.csv", "r")
        for each_line in open_csv:
            self.item_list.add(each_line)                           # (2)

    """
    1) self.item_list will be referencing itemlist.py
    2) add files from items.csv to a list in itemlist.py, called temp
    """

    def build(self):
        self.title = "My App"
        self.root = Builder.load_file('app.kv')
        self.itemlist()
        return self.root

    def itemlist(self):                                             # (1)
        self.root.ids.items_buttons.clear_widgets()                 # (2)
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (0, 0.5, 0.5, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()                                       # (2)

    def create_buttons(self):
        for each_line in self.item_list:
            name, item_desc, cost, status = each_line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0, 0.9, 1))
            temp_button.bind(on_press=self.press_item)
            self.root.ids.items_buttons.add_widget(temp_button)

    def itemhire(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (0, 0.5, 0.5, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def itemreturn(self):
        self.root.ids.items_buttons.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (1, 1, 1, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (0, 0.5, 0.5, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()

    def press_item(self, instance):
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if instance.text == name:
                if self.root.ids.list_button.background_color == [0, 0.5, 0.5, 1]:  # when item_list is being selected
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(name, item_desc, float(cost), status)
                elif self.root.ids.hire_button.background_color == [0, 0.5, 0.5, 1]:  # when hire_item is being selected
                    if "in" in status:
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(name, float(cost))
                    else:
                        self.root.ids.label.text = "Cannot hire that item"
                elif self.root.ids.return_button.background_color == [0, 0.5, 0.5, 1]:  # when return_item is being selected
                    if "out" in status:
                        self.root.ids.label.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.label.text = "Cannot return that item"

    def confirm(self):
        items = 0
        with open("items.csv") as file:
            read_items = file.readlines()
        for line in read_items:
            name, item_desc, cost, status = line.split(",")
            if name in self.root.ids.label.text:
                if self.root.ids.hire_button.background_color == [0, 0.5, 0.5, 1]:  # will only be executed if hire_item is active and an item is being selected
                    self.item_list.clear()
                    read_items[items] = read_items[items].replace("in", "out")  # will change the status of an item from in to out
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)  # commit changes to the csv file
                    for line in read_items:
                        self.item_list.add(line)
                    file.close()
                    self.itemlist()
                elif self.root.ids.return_button.background_color == [0, 0.5, 0.5, 1]:  # will only be executed if return_item is active and an item is being selected
                    self.item_list.clear()
                    read_items[items] = read_items[items].replace("out","in")  # will change the status of an item from in to out
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)  # commit changes to the csv file
                    for line in read_items:
                        self.item_list.add(line)
                    file.close()
                    self.itemlist()
            items += 1

    def additem(self):
        self.root.ids.popup.open()



    def saveitem(self, name, item_desc, cost):
        if len(name) == 0 or len(item_desc) == 0 or len(str(cost)) == 0:
            self.root.ids.popup_label.text = "All fields must be completed"
        elif self.valid(cost) == False:
            self.press_clear()
            self.root.ids.popup_label.text = "Price must be valid number"
        elif self.valid(cost) == True and int(cost) < 0:
            self.press_clear()
            self.root.ids.popup_label.text.text = "Price cannot be negative"
        else:
            add_item = "{},{},{},in\n".format(name, item_desc, cost)
            file = open('items.csv', 'a')
            file.writelines(add_item)
            file.close()
            print('Writing success')
            self.press_clear()
            self.item_list.add(add_item)
            self.exit_popup()
            self.itemlist()

    def valid(self, cost):
        try:
            float(cost)
            return True
        except ValueError:
            return False

    def exit_popup(self):
        self.root.ids.popup.dismiss()

    def press_clear(self):
        self.root.ids.iteminput.text = ""
        self.root.ids.descinput.text = ""
        self.root.ids.ppdinput.text = ""
        self.root.ids.popup_label.text = "Enter details for new item"


MyApp().run()