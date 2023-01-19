import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path, "r", encoding="utf-8") as lista:
            if path.endswith(".xml"):
                xmlfile = xmltodict.parse(lista.read())
                file = xmlfile["dataset"]["record"]
                return file
            raise ValueError("Arquivo inválido")
