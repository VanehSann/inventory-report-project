from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, inventory):
        SimpleReportResult = SimpleReport.generate(inventory)
        lista = Counter([item["nome_da_empresa"] for item in inventory])
        completeReportResult = ""
        for company, quantity in lista.items():
            completeReportResult += f"- {company}: {quantity}\n"
        # return okay
        return (
            f"{SimpleReportResult}\n"
            f"Produtos estocados por empresa:\n"
            f"{completeReportResult}"
        )
