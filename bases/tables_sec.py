# Funções de chamamento das tabelas secundárias para append nas demais

import pyodbc
import datetime

class Consulta_Table_Sec:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    lista_situacao = []

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
            "SELECT codi_emp, i_empregados, nome, data_nascto, CPF, i_filhos FROM externo.bethadba.fofilhos"
        )
        info_filhos = self.cursor.fetchall()
        return info_filhos

# Função para consulta de dados do plano de saúde na tabela foempregados_plano
    def consulta_plano(self):
        self.cursor.execute(
            "SELECT CODI_EMP, DATA_INICIO FROM externo.bethadba.foempregados_plano_saude"
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

# Função para consulta do nome do departamento na tabela fodepto
     def consulta_depto(self):
            self.cursor.execute(
                "SELECT i_depto, nome FROM externo.bethadba.fodepto"
            )
            info_depto = self.cursor.fetchall()
            return info_depto

# Teste de funcionalidade
classe = Consulta_Table_Sec()
print(classe.consulta_filhos())