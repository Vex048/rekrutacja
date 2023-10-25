import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open('taski.json', 'w') as f:
            f.write(json.dumps(tasks, indent=2))
        pass
