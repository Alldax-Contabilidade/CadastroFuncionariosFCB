import pyodbc
import datetime

class ConsultaFuncionarios:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = [1]

    def cadastro_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, i_depto, i_servicos, i_cargos, cpf, pis, i_sindicatos, admissao, venc_ferias,"
            " vinculo, categoria, sindicalizado, salario, ini_praz_det, fim_praz_det, pro_praz_det, cart_prof"
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
            "nome_conjuge, sexo,  FROM externo.bethadba.foempregados "
            "WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()
        print(info_funcionarios)
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


# nome, i_depto, i_servicos, i_cargos

consulta = ConsultaFuncionarios()
consulta.cadastro_funcionario()
#consulta.verificando_situacao_funcionario()
#consulta.consulta_departamento()
