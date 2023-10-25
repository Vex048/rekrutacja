import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        global json_data
        with open('taski.json', 'r') as f:
            json_data = json.loads(f.read())
        pass

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return json_data
        pass