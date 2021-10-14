from banco_dados.consulta_funcionarios import ConsultaFuncionarios
from bases.tables_sec import ConsultaPais

import openpyxl

class Planilha:

    consulta = ConsultaFuncionarios()
    cadastro_funcionario = consulta.cadastro_funcionario()
    situacao = consulta.verificando_situacao_funcionario()
    departamentos = consulta.consulta_departamento()

    wb = openpyxl.Workbook()
    ws = wb.active

    lista_teste = []

    def tratamento_inicial(self):
        for cadastro in self.cadastro_funcionario:
            codi_func = cadastro[0]
            nome_func = cadastro[1]

            for situacao in self.situacao:

                if codi_func == situacao[0]:
                    self.lista_teste.append((codi_func, nome_func, situacao[1]))
                    break

    def escrevendo_planilha(self):
        self.ws['A1'] = "Codigo"
        self.ws['B1'] = "Nome Funcionário"
        self.ws['C1'] = "Situação"

        for row in self.lista_teste:
            self.ws.append(row)

        self.wb.save("Funcionarios_FCB.xlsx")

Planilha().tratamento_inicial()
Planilha().escrevendo_planilha()