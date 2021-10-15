import pyodbc
import datetime

# Classe para conexão com o B.D. assim como definição de funções para captura de outras tabelas
class ConsultaFuncionarios:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = []

# Função para buscar dados específicos do cadastro de funcionários
    def cadastro_funcionario(self):

# O método execute permite a execução de uma query SQL
        self.cursor.execute(
            "SELECT i_empregados, nome, i_depto, i_servicos, i_cargos,i_sindicatos, TIPO_HORARIO, i_bancos,"
            " I_OPERADORAPLANOSAUDE, MUNICIPIO_ENDERECO, PAIS_ENDERECO, PAIS_NASCIMENTO, PAIS_PASSAPORTE,"
            " OPCAO_PLANO_SAUDE, MUNICIPIO_NASCIMENTO, TIPO_CONTA, cor, grau_instrucao,categoria, EMISSOR_PASSAPORTE,"
            "RESIDENCIA_PROPRIA,POSSUI_DEFICIENCIA, cpf, pis,admissao, venc_ferias,sindicalizado, salario,"
            " ini_praz_det, fim_praz_det, pro_praz_det, cart_prof,serie_cart_prof, dt_exp_cprof, uf_cart_prof,"
            " num_cart_ponto, horas_mes, horas_semana,horas_dia, forma_pagto,  conta_corr, PLANO_SAUDE_OPTANTES,"
            " identidade, org_exp_ident, uf_exp_ident, dt_exp_ident, NUMERO_PASSAPORTE,UF_PASSAPORTE,"
            " DATA_EMISSAO_PASSAPORTE, DATA_VALIDADE_PASSAPORTE, titulo_eleit, zona_eleit, secao_eleit, cart_motorista,"
            " categ_cart_mot, ORGAO_EMISSOR_CNH, DATA_EXPEDICAO_CNH, estado, cart_reservista,cate_reservista,"
            " venc_cart_mot, ENDERECO_COMERCIAL, cep, endereco, numero_end, complemento, bairro, EMAIL_ALTERNATIVO,"
            " EMAIL, fone, fone2, data_nascimento,uf_nascimento,naturalizado, DATA_NATURALIZACAO, nome_mae, nome_pai,"
            " nome_conjuge, sexo, estado_civil, grupo_sanguineo, rh_sanguineo,  CASADO_BRASILEIRO"
            " FROM externo.bethadba.foempregados WHERE codi_emp = 221"
        )

# O método fetchall armazena o valor recebido no último execute podendo ser armazendo em uma variável
        info_funcionarios = self.cursor.fetchall()
        # print(info_funcionarios)
        return info_funcionarios

# Função para definir a situação dos funcionários como 'Demitido' ou 'Trabalhando'
# Nova busca da foempregados, retornando somente o i_empregados para comparação com a forescisoes
    def verificando_situacao_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados FROM externo.bethadba.foempregados WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()

# Captura dos i_empregados da forescisoes para comparação com a foempregados
        self.cursor.execute(
            "SELECT i_empregados FROM externo.bethadba.forescisoes WHERE codi_emp = 221"
        )
        info_rescisoes = self.cursor.fetchall()

# Definição de um for...in que percorre a tabela foempregados e armazena em codigo
        for codigo in info_funcionarios:

# Durante o loop se um dos valores de codigo estiver presente em forescisoes, o if inclui
# o primeiro elemento de codigo na variável global lista_situacao através de um append
# seguido de uma string com valor 'Demitido'
            if codigo in info_rescisoes:
                self.lista_situacao.append((codigo[0], "Demitido"))

# Faz o mesmo processo da linha anterior, mas inclui a string 'Trabalhando'
            else:
                self.lista_situacao.append((codigo[0], "Trabalhando"))

# Após a conclusão to if...else, todos os valores terão sido percorridos e estarão com a situação
# preenchida. Com o consequente retorno da lista_situacao atualizada
        return self.lista_situacao

    # Função para consulta do nome dos departamentos
    def consulta_departamento(self):
        self.cursor.execute(
            "SELECT i_depto, nome FROM externo.bethadba.fodepto WHERE codi_emp = 221"
        )
        info_departamentos = self.cursor.fetchall()
        return info_departamentos

# Função para consulta do nome do País na tabela gepais
    def consulta_pais(self):
        self.cursor.execute(
            "SELECT codigo_pais, nome_pais FROM externo.bethadba.gepais"
        )
        info_pais = self.cursor.fetchall()
        return info_pais

# Função para consulta do nome do Município na tabela efmunici
    def consulta_municipio(self):
        self.cursor.execute(
            "SELECT codigo_municipio, nome_municipio FROM externo.bethadba.gemunicipio"
        )
        info_municipio = self.cursor.fetchall()
        return info_municipio

# Função para consulta da tabela fofilhos
    def consulta_filhos(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, data_nascto, CPF, i_filhos FROM externo.bethadba.fofilhos "
            "WHERE codi_emp = 221"
        )
        info_filhos = self.cursor.fetchall()
        return info_filhos

# Função para consulta de dados do plano de saúde na tabela foempregados_plano
    def consulta_plano(self):
        self.cursor.execute(
            "SELECT DATA_INICIO FROM externo.bethadba.foempregados_plano_saude WHERE codi_emp = 221"
        )
        info_plano = self.cursor.fetchall()
        return info_plano

# Função para consulta de dados do plano de saúde na tabela fooperadoraplanosaude
    def consulta_operadora(self):
        self.cursor.execute(
            "SELECT I_OPERADORAPLANOSAUDE, NOME FROM externo.bethadba.fooperadoraplanosaude"

        )
        info_operadora = self.cursor.fetchall()
        return info_operadora

# Função para consulta do nome do cargo
    def consulta_cargos(self):
        self.cursor.execute(
            "SELECT i_cargos, nome FROM externo.bethadba.focargos WHERE codi_emp = 221"
        )
        info_cargos = self.cursor.fetchall()
        return info_cargos

# Função para consulta do nome do sindicato
    def consulta_sindicato(self):
        self.cursor.execute(
            "SELECT i_sindicatos, nome FROM externo.bethadba.fosindicatos")
        info_sindicato = self.cursor.fetchall()
        return info_sindicato

# Função para consulta do nome do banco
    def consulta_banco(self):
        self.cursor.execute(
            "SELECT i_bancos, nome FROM externo.bethadba.fobancos")
        info_banco = self.cursor.fetchall()
        return info_banco

# Função para consulta do nome do servico
    def consulta_servico(self):
        self.cursor.execute(
            "SELECT i_servicos, nome FROM externo.bethadba.foservicos WHERE codi_emp = 221")

        info_servico = self.cursor.fetchall()
        return info_servico

"""
Testes de funcionalidade

consulta = ConsultaFuncionarios()
print(consulta.consulta_servico())

consulta.verificando_situacao_funcionario()
consulta.consulta_departamento()

consulta = ConsultaFuncionarios()
print(consulta.lista_situacao)
consulta.verificando_situacao_funcionario()
print(consulta.lista_situacao)
"""

