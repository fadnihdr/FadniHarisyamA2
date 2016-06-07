"""
itemlist.py

any input that goes here will be stored in a list, for
"""

class ItemList:
    def __init__(self):
        self.temp = []

    def __getitem__(self, item):
        return self.temp[item]

    def __len__(self):
        return len(self.temp)

    def add(self, item):
        self.temp.append(item)

    def clear(self):
        self.temp = []
