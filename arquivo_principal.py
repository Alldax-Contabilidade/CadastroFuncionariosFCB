from bases.base_tratamento import Planilha
import getpass
import datetime

print("   >> Iniciando Programa <<  ")
user = getpass.getuser()
horario = datetime.datetime.now()
with open(r"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Log_programs\log_sist.txt", 'a') as arquivo:
    arquivo.write(f"ConferênciaFCB | Iniciado | {user} | {horario} \n")

arquivo.close()

Planilha().trocar_id_nomes()
Planilha().plano_saude()
Planilha().exame_toxicologico()
Planilha().exame_ocupacional()
Planilha().situacao_funcionario()
Planilha().dias_exp()
Planilha().inserindo_filhos()
Planilha().escrevendo_planilha()

# Planilha().ordenando_colunas()

user = getpass.getuser()
horario = datetime.datetime.now()
with open(r"T:\DEPARTAMENTOS\AUTOMAÇÃO\DATABASES\Log_programs\log_sist.txt", 'a') as arquivo:
    arquivo.write(f"ConferênciaFCB | Finalizando | {user} | {horario} \n")

arquivo.close()

print("   >>> Finalizando Programa <<<  ")
