from banco_dados.consulta_funcionarios import ConsultaFuncionarios
import openpyxl
from lista_util.listas_sem_tabelas import lista_util, dicionario_ocupacional
import datetime


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
    # toxicologico = consulta.consulta_toxicologico()
    #ocupacional= consulta.consulta_ocupacional()

    tipo_horario, cor_raca, grau_instrucao, tipo_conta, categoria, emissor, residencia, deficiencia, \
    sindicalizado = lista_util()

    wb = openpyxl.Workbook()
    ws = wb.active
    ordem_paramentro = [departamentos, servico, cargos, sindicato, tipo_horario, banco, municipio, pais,
                        pais, pais, municipio, tipo_conta, cor_raca, grau_instrucao, categoria, emissor,
                        residencia, deficiencia, sindicalizado]
    lista_cadastro = []
    lista_geral_cadastro = []

    # criação de função para conectar planilhas e modificar números por nomes
    def trocar_id_nomes(self):
        for cadastro in self.cadastro_funcionario:
            lista_cadastro = list(cadastro)

            self.lista_geral_cadastro.append(lista_cadastro)

        posicao = 2
        for parametro in self.ordem_paramentro:
            # print(posicao)
            self.troca_nome(parametro, posicao)
            posicao += 1

        # print(self.lista_geral_cadastro[2073])

    # Criação de função para buscar nome baseado no cod
    def troca_nome(self, listagem_parametros, posicao):
        for cadastro in self.lista_geral_cadastro:

            for listagem in listagem_parametros:

                if cadastro[posicao] == listagem[0]:
                    cadastro[posicao] = listagem[1]

    # criação de função para conectar planilhas e modificar números por nomes
    def plano_saude(self):

        for funcionario in self.lista_geral_cadastro:
            cod_funcionario = funcionario[0]
            plano_saude = funcionario[21]

            if plano_saude == 1:
                for plano_funcionario in self.planos:
                    cod_emp = plano_funcionario[0]
                    cod_operadora = plano_funcionario[1]
                    data_inicio = plano_funcionario[2]

                    if cod_funcionario == cod_emp:
                        for operadora in self.operadora:
                            id_operadora = operadora[0]
                            nome_operadora = operadora[1]

                            if cod_operadora == id_operadora:
                                #print(f"{cod_funcionario} | {nome_operadora} | {data_inicio}")
                                funcionario[21] = nome_operadora
                                funcionario.insert(22, data_inicio)

            else:
                funcionario[21] = ''
                funcionario.insert(22, '')

    # criação de função para conectar planilhas e modificar números por nomes
    def exame_toxicologico(self):
        for cadastro in self.lista_geral_cadastro:
            codi_func = cadastro[0]

            toxicologico = self.consulta.consulta_toxicologico(codi_func)

            if len(toxicologico) == 0:
                cadastro.append('')
                cadastro.append('')

            else:
                if toxicologico[0][1] == 1:
                    cadastro.append(toxicologico[0][0])
                    cadastro.append('Admissional')
                else:
                    cadastro.append(toxicologico[0][0])
                    cadastro.append('Demissional')


        # print(self.lista_geral_cadastro[2218])
        # print(self.lista_geral_cadastro[0])
#criação de função para conectar planilhas e modificar números por nomes
    def exame_ocupacional(self):
        for cadastro in self.lista_geral_cadastro:
            codi_func = cadastro[0]

            ocupacional = self.consulta.consulta_ocupacional(codi_func)

            if len(ocupacional) == 0:
                cadastro.append('')
                cadastro.append('')
                cadastro.append('')
                cadastro.append('')
            else:
                dicionario, resultado = dicionario_ocupacional()
                tipo = dicionario[ocupacional[0][0]]
                result= resultado[ocupacional[0][2]]
                cadastro.append(tipo)
                cadastro.append(ocupacional[0][1])
                cadastro.append(result)
                cadastro.append(ocupacional[0][3])
        # print(self.lista_geral_cadastro[362])
# criação de função para definir situação de atividade
    def situacao_funcionario(self):
        for cadastro in self.lista_geral_cadastro:
            codi_funcionario = cadastro[0]
            for situacao in self.situacao:
                if codi_funcionario == situacao[0]:
                    cadastro.insert(2, situacao[1])
                    break
        print(self.lista_geral_cadastro[2078])


    def escrevendo_planilha(self):
        self.ws['A1'] = "Codigo"
        self.ws['B1'] = "Nome Funcionário"
        self.ws['C1'] = "Situação"

        for row in self.lista_teste:
            self.ws.append(row)

        self.wb.save("Funcionarios_FCB.xlsx")

Planilha().trocar_id_nomes()
Planilha().plano_saude()
Planilha().exame_toxicologico()
Planilha().exame_ocupacional()
Planilha().situacao_funcionario()