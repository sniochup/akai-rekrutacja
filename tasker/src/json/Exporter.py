import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        with open('taski.json', 'w', encoding="utf-8") as file:
            json.dump(tasks, file)
        file.close()
        pass
