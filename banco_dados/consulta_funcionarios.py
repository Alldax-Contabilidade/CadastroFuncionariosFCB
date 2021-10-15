import pyodbc
import datetime


class ConsultaFuncionarios:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = [1]

    def cadastro_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, i_depto, i_servicos, i_cargos, cpf, pis, i_sindicatos, admissao, venc_ferias,"
            " vinculo, categoria, sindicalizado, salario, ini_praz_det, fim_praz_det, pro_praz_det, cart_prof,"
            "serie_cart_prof, dt_exp_cprof, uf_cart_prof, TIPO_HORARIO, num_cart_ponto, horas_mes, horas_semana,"
            "horas_dia, forma_pagto, i_bancos, conta_corr, TIPO_CONTA, I_OPERADORAPLANOSAUDE, PLANO_SAUDE_OPTANTES, "
            "OPCAO_PLANO_SAUDE "
            " identidade, org_exp_ident, uf_exp_ident, dt_exp_ident, NUMERO_PASSAPORTE, EMISSOR_PASSAPORTE, "
            "UF_PASSAPORTE, DATA_EMISSAO_PASSAPORTE, DATA_VALIDADE_PASSAPORTE, PAIS_PASSAPORTE, titulo_eleit, "
            "zona_eleit, secao_eleit, cart_motorista, categ_cart_mot, ORGAO_EMISSOR_CNH, DATA_EXPEDICAO_CNH,"
            " estado, cart_reservista,"
            "cate_reservista, venc_cart_mot, ENDERECO_COMERCIAL, cep, TIPO_ENDERECO, endereco, RESIDENTE_EXTERIOR,"
            "numero_end, complemento, bairro, MUNICIPIO_ENDERECO, PAIS_ENDERECO, RESIDENCIA_PROPRIA,"
            " IMOVEL_ADQUIRIDO_RECURSOS_FGTS,"
            "EMAIL_ALTERNATIVO, EMAIL, fone, fone2, data_nascimento,uf_nascimento, PAIS_NACIONALIDADE,"
            " MUNICIPIO_NASCIMENTO,"
            "PAIS_NASCIMENTO, naturalizado, DATA_NATURALIZACAO, ALVARA_JUDICIAL, NUMERO_ALVARA, nome_mae, nome_pai,"
            "nome_conjuge, sexo, estado_civil, cor, grupo_sanguineo, rh_sanguineo, grau_instrucao, CASADO_BRASILEIRO,"
            "POSSUI_DEFICIENCIA, POSSUI_DEFICIENCIA_MOTORA, deficiente_fisico, POSSUI_DEFICIENCIA_VISUAL,"
            "POSSUI_DEFICIENCIA_AUDITIVA, POSSUI_DEFICIENCIA_OUTRAS, POSSUI_DEFICIENCIA_REABILITADO, "
            "OBSERVACAO_DEFICIENCIA, POSSUI_DEFICIENCIA_MENTAL  FROM externo.bethadba.foempregados "
            "WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()
        # print(info_funcionarios)
        return info_funcionarios

    def verificando_situacao_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados FROM externo.bethadba.foempregados "
            "WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()

        self.cursor.execute(
            "SELECT i_empregados FROM externo.bethadba.forescisoes WHERE codi_emp = 221"
        )
        info_rescisoes = self.cursor.fetchall()

        for codigo in info_funcionarios:

            if codigo in info_rescisoes:
                self.lista_situacao.append((codigo[0], "Demitido"))

            else:
                self.lista_situacao.append((codigo[0], "Trabalhando"))

        return self.lista_situacao

    def consulta_departamento(self):
        self.cursor.execute(
            "SELECT i_depto, nome FROM externo.bethadba.fodepto "
            "WHERE codi_emp = 221"
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
            "SELECT codi_mun, nome_mun FROM externo.bethadba.efmunici"
        )
        info_municipio = self.cursor.fetchall()
        return info_municipio

# Função para consulta da tabela fofilhos
    def consulta_filhos(self):
        self.cursor.execute(
            "SELECT codi_emp, i_empregados, nome, data_nascto, CPF, i_filhos FROM externo.bethadba.fofilhos "
            "WHERE codi_emp = 221"
        )
        info_filhos = self.cursor.fetchall()
        return info_filhos

# Função para consulta de dados do plano de saúde na tabela foempregados_plano
    def consulta_plano(self):
        self.cursor.execute(
            "SELECT CODI_EMP, DATA_INICIO FROM externo.bethadba.foempregados_plano_saude "
            "WHERE codi_emp = 221"
        )
        info_plano = self.cursor.fetchall()
        return info_plano

# Função para consulta de dados do plano de saúde na tabela fooperadoraplanosaude
    def consulta_operadora(self):
        self.cursor.execute(
            "SELECT I_OPERADORAPLANOSAUDE, NOME FROM externo.bethadba.fooperadoraplanosaude "

        )
        info_operadora = self.cursor.fetchall()
        return info_operadora

# Função para consulta do nome do cargo
    def consulta_cargos(self):
        self.cursor.execute(
            "SELECT i_cargos, nome FROM externo.bethadba.focargos"
            " WHERE codi_emp = 221"
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
            "SELECT codi_emp, i_servicos, nome FROM externo.bethadba.foservicos")
        info_servico = self.cursor.fetchall()
        return info_servico

# nome, i_depto, i_servicos, i_cargos


# Teste de funcionalidade da classe ConsultaFuncionarios()
consulta = ConsultaFuncionarios()
print(consulta.consulta_servico())
#consulta.verificando_situacao_funcionario()
#consulta.consulta_departamento()

