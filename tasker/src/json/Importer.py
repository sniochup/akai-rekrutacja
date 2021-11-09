import json


class Importer:

    def __init__(self):
        self.data = {}
        pass

    def read_tasks(self):
        with open('taski.json', 'r', encoding="utf-8") as file:
            self.data = json.load(file)
        file.close()
        pass

    def get_tasks(self):
        return self.data
        pass
