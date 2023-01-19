from inventory_report.reports.colored_report import ColoredReport

# from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    list = [
        {
            "id": 1,
            "nome_da_empresa": "Trybe",
            "nome_do_produto": "Full Stack Web Development Course",
            "data_de_fabricacao": "2023-01-17",
            "data_de_validade": "2024-01-17",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "full time",
        }
    ]

    resultSimples = ColoredReport(SimpleReport).generate(list)
    coloredResultSimples = (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2023-01-17\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2024-01-17\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mTrybe\033[0m"
    )

    assert resultSimples == coloredResultSimples
