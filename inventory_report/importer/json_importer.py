import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path, "r", encoding="utf-8") as lista:
            if path.endswith(".json"):
                file = json.load(lista)
                return file
            raise ValueError("Arquivo inválido")
