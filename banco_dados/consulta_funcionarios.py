import pyodbc


class ConsultaFuncionarios:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = []

    def cadastro_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, i_depto, i_servicos, i_cargos,i_sindicatos, TIPO_HORARIO, i_bancos,"
            " MUNICIPIO_ENDERECO, PAIS_ENDERECO, PAIS_NASCIMENTO, PAIS_PASSAPORTE,"
            " MUNICIPIO_NASCIMENTO, TIPO_CONTA, cor, grau_instrucao,categoria, EMISSOR_PASSAPORTE, RESIDENCIA_PROPRIA,"
            "POSSUI_DEFICIENCIA, sindicalizado, OPCAO_PLANO_SAUDE, forma_pagto, cpf, pis,admissao, venc_ferias, "
            "salario, ini_praz_det, fim_praz_det, pro_praz_det, cart_prof,serie_cart_prof, dt_exp_cprof, uf_cart_prof,"
            " num_cart_ponto, horas_mes, horas_semana,horas_dia, conta_corr, identidade, org_exp_ident, uf_exp_ident,"
            " dt_exp_ident, NUMERO_PASSAPORTE,UF_PASSAPORTE, DATA_EMISSAO_PASSAPORTE, DATA_VALIDADE_PASSAPORTE, "
            "titulo_eleit, zona_eleit, secao_eleit, cart_motorista, categ_cart_mot, ORGAO_EMISSOR_CNH,"
            " DATA_EXPEDICAO_CNH, estado, cart_reservista,cate_reservista, venc_cart_mot, cep, endereco, numero_end,"
            " complemento, bairro, EMAIL_ALTERNATIVO, EMAIL, fone, fone2, data_nascimento,uf_nascimento,naturalizado,"
            " DATA_NATURALIZACAO, nome_mae, nome_pai,nome_conjuge, sexo, estado_civil, grupo_sanguineo, rh_sanguineo"
            "FROM externo.bethadba.foempregados WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()
        return info_funcionarios

    def verificando_situacao_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados FROM externo.bethadba.foempregados WHERE codi_emp = 221"
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
            "SELECT i_depto, nome FROM externo.bethadba.fodepto WHERE codi_emp = 221"
        )
        info_departamentos = self.cursor.fetchall()
        return info_departamentos

    def consulta_pais(self):
        self.cursor.execute(
            "SELECT codigo_pais, nome_pais FROM externo.bethadba.gepais"
        )
        info_pais = self.cursor.fetchall()
        return info_pais

    def consulta_municipio(self):
        self.cursor.execute(
            "SELECT codigo_municipio, nome_municipio FROM externo.bethadba.gemunicipio"
        )
        info_municipio = self.cursor.fetchall()
        return info_municipio

    def consulta_filhos(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, data_nascto, CPF, i_filhos, grau_parentesco, dependente, SAL_FAM_FIM,"
            "SAL_FAM_FIM_DETERMINADO, DEPEND_IRRF_FIM, DEPEND_IRRF_FIM_DETERMINADO,RECEBE_PENSAO_ALIMENTICIA,"
            "DETERMINAR_FIM_PENSAO_ALIMENTICIA, DATA_FIM_PENSAO_ALIMENTICIA"
            "FROM externo.bethadba.fofilhos WHERE codi_emp = 221"
        )
        info_filhos = self.cursor.fetchall()
        return info_filhos

    def consulta_plano(self, id):
        self.cursor.execute(
            f"SELECT TOP 1 I_OPERADORAPLANOSAUDE, DATA_INICIO FROM externo.bethadba.foempregados_plano_saude "
            f"WHERE codi_emp = 221 AND I_EMPREGADOS = {id} ORDER BY DATA_INICIO desc"
        )
        info_plano = self.cursor.fetchall()
        return info_plano

    def consulta_operadora(self):
        self.cursor.execute(
            "SELECT I_OPERADORAPLANOSAUDE, NOME FROM externo.bethadba.fooperadoraplanosaude")
        info_operadora = self.cursor.fetchall()
        return info_operadora

    def consulta_cargos(self):
        self.cursor.execute(
            "SELECT i_cargos, nome FROM externo.bethadba.focargos WHERE codi_emp = 221")
        info_cargos = self.cursor.fetchall()
        return info_cargos

    def consulta_sindicato(self):
        self.cursor.execute(
            "SELECT i_sindicatos, nome FROM externo.bethadba.fosindicatos")
        info_sindicato = self.cursor.fetchall()
        return info_sindicato

    def consulta_banco(self):
        self.cursor.execute(
            "SELECT i_bancos, nome FROM externo.bethadba.fobancos")
        info_banco = self.cursor.fetchall()
        return info_banco

    def consulta_servico(self):
        self.cursor.execute(
            "SELECT i_servicos, nome FROM externo.bethadba.foservicos WHERE codi_emp = 221")

        info_servico = self.cursor.fetchall()
        return info_servico

    def consulta_toxicologico(self, id):
        self.cursor.execute(
            f"SELECT TOP 1 DATA, TIPO FROM externo.bethadba.FOEMPREGADOS_EXAMES_TOXICOLOGICOS  "
            f"WHERE codi_emp = 221 AND I_EMPREGADOS = {id} ORDER BY DATA desc"
        )
        info_toxicologico = self.cursor.fetchall()

        return info_toxicologico

    def consulta_ocupacional(self, id):
        self.cursor.execute(
            f"SELECT TOP 1 I_ATESTADO_OCUPACIONAL, DATA, RESULTADO ,DATA_VENCIMENTO "
            f"FROM externo.bethadba.FOEMPREGADOS_ATESTADOS_OCUPACIONAIS  WHERE codi_emp = 221"
            f"AND I_EMPREGADOS = {id} ORDER BY DATA desc"
        )
        info_ocupacional = self.cursor.fetchall()
        return info_ocupacional

    def consulta_nome_funcionario(self, id):
        self.cursor.execute(
            f"SELECT nome FROM externo.bethadba.foempregados WHERE codi_emp = 221 AND "
            f"i_empregados = {id}"
        )
        nome_funcionario = self.cursor.fetchone()[0]
        return nome_funcionario
