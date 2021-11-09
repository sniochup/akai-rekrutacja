import json


class Importer:

    def __init__(self):
        self.data = {}

    def read_tasks(self):
        with open('taski.json', 'r', encoding="utf-8") as file:
            self.data = json.load(file)

    def get_tasks(self):
        return self.data
