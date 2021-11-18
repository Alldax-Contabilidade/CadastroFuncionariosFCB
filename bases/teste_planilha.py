import openpyxl
from banco_dados.consulta_funcionarios import ConsultaFuncionarios


class FILHOS:
    def __init__(self):
        self.planilha = 'Funcionarios_FCB.xlsx'
        self.wb = openpyxl.load_workbook(self.planilha)
        self.ws = self.wb.active

        self.ws2 = self.wb.create_sheet('Filhos')

        self.filhos = ConsultaFuncionarios().consulta_filhos()

        self.lista_filhos_geral = []
        self.lista_cadastro = []

    def tratando_filhos(self):
        for filhos in self.filhos:
            lista_filhos = []
            for dado in filhos:
                lista_filhos.append(dado)

            self.lista_filhos_geral.append(lista_filhos)

    def adicionado_nome_pai(self):
        for cadastro in self.lista_filhos_geral:
            i_empregado = cadastro[0]

            nome_funcionario = ConsultaFuncionarios().consulta_nome_funcionario(i_empregado)

            cadastro.insert(1, nome_funcionario)

    def escrevendo_planilha(self):
        self.ws2['A1'] = 'Código Funcionario'
        self.ws2['B1'] = 'Nome Funcionario'
        self.ws2['C1'] = 'Nome Dependente'
        self.ws2['D1'] = 'Data Nascimento'
        self.ws2['E1'] = 'CPF'
        self.ws2['F1'] = 'Código Dependente'

        for cadastro in self.lista_filhos_geral:
            cadastro_tupla = tuple(cadastro)

            self.lista_cadastro.append(cadastro_tupla)

        for linha in self.lista_cadastro:
            self.ws2.append(linha)

        self.wb.save(self.planilha)


ff = FILHOS()
ff.tratando_filhos()
ff.adicionado_nome_pai()
ff.escrevendo_planilha()
