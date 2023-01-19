from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, inventory):
        # data de fabricacao minima
        lista_de_datas = [item["data_de_fabricacao"] for item in inventory]
        data_de_fabricacao = min(lista_de_datas)
        # data de validade
        nova_lista_de_datas = [
            item["data_de_validade"]
            for item in inventory
            if item["data_de_validade"] >= str(datetime.today())
        ]
        data_de_validade = min(nova_lista_de_datas)
        # nome_da_empresa
        lista_de_nomes = [item["nome_da_empresa"] for item in inventory]
        nome_da_empresa = Counter(lista_de_nomes).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {nome_da_empresa}"
        )
