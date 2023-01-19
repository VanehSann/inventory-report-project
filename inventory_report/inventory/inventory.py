import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        with open(path, "r", encoding="utf-8") as lista:
            if path.endswith(".csv"):
                file = list(
                    csv.DictReader(lista, delimiter=",", quotechar='"')
                )
            elif path.endswith(".json"):
                file = json.load(lista)
            elif path.endswith(".xml"):
                xmlfile = xmltodict.parse(lista.read())
                file = xmlfile["dataset"]["record"]
            else:
                raise ValueError("invalid file")

            if type == "simples":
                return SimpleReport.generate(file)
            else:
                return CompleteReport.generate(file)
