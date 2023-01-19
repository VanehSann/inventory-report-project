import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".csv"):
            with open(path, "r", encoding="utf-8") as lista:
                file = list(csv.DictReader(lista))
            return file
        raise ValueError("Arquivo inválido")
