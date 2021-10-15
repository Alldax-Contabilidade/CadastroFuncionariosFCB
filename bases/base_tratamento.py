from banco_dados.consulta_funcionarios import ConsultaFuncionarios
import openpyxl
from lista_util.listas_sem_tabelas import lista_util


class Planilha:

    consulta = ConsultaFuncionarios()
    cadastro_funcionario = consulta.cadastro_funcionario()
    situacao = consulta.verificando_situacao_funcionario()
    filhos = consulta.consulta_filhos()
    departamentos = consulta.consulta_departamento()
    servico = consulta.consulta_servico()
    cargos = consulta.consulta_cargos()
    sindicato = consulta.consulta_sindicato()
    banco = consulta.consulta_banco()
    operadora = consulta.consulta_operadora()
    municipio = consulta.consulta_municipio()
    pais = consulta.consulta_pais()
    planos = consulta.consulta_plano()

    tipo_horario, cor_raca, grau_instrucao, tipo_conta, categoria, emissor,residencia,deficiencia = lista_util()

    wb = openpyxl.Workbook()
    ws = wb.active
    ordem_paramentro = [departamentos, servico, cargos, sindicato, tipo_horario,  banco, operadora, municipio, pais,
                        pais, pais, planos, municipio, tipo_conta, cor_raca, grau_instrucao, categoria, emissor,
                        residencia,deficiencia]
    lista_cadastro = []
    lista_geral_cadastro = []

    def tratamento_inicial(self):
        for cadastro in self.cadastro_funcionario:
            codi_func = cadastro[0]
            nome_func = cadastro[1]

            for situacao in self.situacao:

                if codi_func == situacao[0]:
                    self.lista_teste.append((codi_func, nome_func, situacao[1]))
                    break

    def trocar_id_nomes(self):
        for cadastro in self.cadastro_funcionario:
            lista_cadastro = list(cadastro)

            self.lista_geral_cadastro.append(lista_cadastro)

        posicao = 2
        for parametro in self.ordem_paramentro:
            print(posicao)
            self.troca_nome(parametro, posicao)
            posicao += 1

        print(self.lista_geral_cadastro[2073])

# Criação de função para buscar nome baseado no cod
    def troca_nome(self, listagem_parametros, posicao):
        for cadastro in self.lista_geral_cadastro:

            for listagem in listagem_parametros:

                if cadastro[posicao] == listagem[0]:
                    cadastro[posicao] = listagem[1]




    def escrevendo_planilha(self):
        self.ws['A1'] = "Codigo"
        self.ws['B1'] = "Nome Funcionário"
        self.ws['C1'] = "Situação"

        for row in self.lista_teste:
            self.ws.append(row)

        self.wb.save("Funcionarios_FCB.xlsx")


Planilha().trocar_id_nomes()
