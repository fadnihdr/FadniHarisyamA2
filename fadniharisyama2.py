from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import *
"""
Name: Fadni Harisyam
Student ID: 13269323
Repository link: https://github.com/fadnihdr/FadniHarisyamA2
Date submitted: 08/6/2016
This program is projected to create a functional GUI for the previous item hire porgram.
Same as before, this program should import anything from the csv files and show them as buttons.
The program is also able to take and validate input from user and append it into the csv file.
"""

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

    def itemlist(self):
        """
        list items
        """
        self.root.ids.items_buttons.clear_widgets()  # remove item buttons from the previous session
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_button.background_color = (0, 0.5, 0.5, 1)
        self.root.ids.hire_button.background_color = (1, 1, 1, 1)
        self.root.ids.return_button.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.add_item.background_color = (1, 1, 1, 1)
        self.create_buttons()



    def create_buttons(self):
        """
        create item buttons for list,hire,return
        """
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
        """
            this function will show the description of the selected item by changing the label.
            the label will also change when the item_return or item_hire button is being selected
            :param instance:
            :return:
        """
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
        """
            this function will commit changes to the csv file
            :return:
        """
        items = 0
        with open("items.csv") as file:
            read_items = file.readlines()
        for line in read_items:
            name, item_desc, cost, status = line.split(",")
            if name in self.root.ids.label.text:
                if self.root.ids.hire_button.background_color == [0, 0.5, 0.5, 1]:
                    self.item_list.clear()
                    read_items[items] = read_items[items].replace("in", "out")
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)
                    for line in read_items:
                        self.item_list.add(line)
                    file.close()
                    self.itemlist()
                elif self.root.ids.return_button.background_color == [0, 0.5, 0.5, 1]:
                    self.item_list.clear()
                    read_items[items] = read_items[items].replace("out", "in")
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)
                    for line in read_items:
                        self.item_list.add(line)
                    file.close()
                    self.itemlist()
            items += 1

    def additem(self):
        """
            this function will display the popup window
            :return:
        """
        self.root.ids.popup.open()

    def saveitem(self, name, item_desc, cost):
        """
            when save item is pressed, this function will run
            this function will take and verify inputs from the kv file and store them into the csv file
            :param name:
            :param item_desc:
            :param cost:
            :return:

        """
        if len(name) == 0 or len(item_desc) == 0 or len(str(cost)) == 0:
            self.root.ids.popup_label.text = "All fields must be completed"
        elif self.valid(cost) == False:
            self.press_clear()
            self.root.ids.popup_label.text = "Price must be valid number"
        elif self.valid(cost) == True and float(cost) < 0:
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
        """
        checks if cost is valid
        """
        try:
            float(cost)
            return True
        except ValueError:
            return False

    def exit_popup(self):
        """
        close popup window
        """
        self.root.ids.popup.dismiss()

    def press_clear(self):
        """
        remove inputs in popup window
        """
        self.root.ids.iteminput.text = ""
        self.root.ids.descinput.text = ""
        self.root.ids.ppdinput.text = ""
        self.root.ids.popup_label.text = "Enter details for new item"


MyApp().run()

"""
Known bugs:
1. after a successful hire, when the user wants to return an available item(cannot be returned), the returned item will
    be the previous item that was hired.
2. items with the same name, although assigned to have different price and description will have the same values
3. hire/return only affects the oldest item, if duplicated items are present
"""