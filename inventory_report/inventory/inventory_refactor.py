from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def import_data(self, path, type):
        lista = self.importer.import_data(path)
        for elem in lista:
            self.data.append(elem)
        if type == "simples":
            return SimpleReport.generate(lista)
        elif type == "completo":
            return CompleteReport.generate(lista)

    def __iter__(self):
        return InventoryIterator(self.data)
