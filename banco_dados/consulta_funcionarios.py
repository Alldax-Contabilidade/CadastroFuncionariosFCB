import pyodbc


class ConsultaFuncionarios:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = []

    def cadastro_funcionario(self):
        self.cursor.execute(
            "SELECT i_empregados, nome, i_depto, i_servicos, i_cargos FROM externo.bethadba.foempregados "
            "WHERE codi_emp = 221"
        )
        info_funcionarios = self.cursor.fetchall()
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

# consulta = ConsultaFuncionarios()
# consulta.verificando_situacao_funcionario()
# consulta.consulta_departamento()
