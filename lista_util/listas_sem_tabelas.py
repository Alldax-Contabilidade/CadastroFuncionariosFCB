def lista_util():
    tipo_horario = [
        (1, "Submetidos a Horário de Trabalho (cap.II da CLT)"),
        (2, "Atividade Externa especificada no Inciso I do Art.62 da CLT"),
        (3, "Funções especificadas no Insciso II do Art.62 da CLT"),
        (4, "Horário de Motorista inciso V do Art.2 Lei 13103/2015"),
        (5, "Horário de Motorista Art. 235 C -CLT"),
        (6, "Teletrabalho, previsto no Inciso III do Art.62 da CLT")
    ]
    cor_raca = [
        (0, "Indigena"),
        (2, "Branca"),
        (4, "Negra"),
        (6, "Amarela"),
        (8, "Parda"),
        (9, "Não Informada")
    ]
    grau_instrucao = [
        (1, "Analfabeto"),
        (2, "Ensino fundamental até 5º incompleto"),
        (3, "Ensino fundamental até 5º completo"),
        (4, "Ensino fundamental 6º ao 9º"),
        (5, "Ensino fundamental completo"),
        (6, "Ensino medio incompleto"),
        (7, "Ensino medio completo"),
        (8, "Superior incompleto"),
        (9, "Superior completo"),
        (10, "Pós graduação"),
        (11, "Mestrado"),
        (12, "Doutorado"),
        (13, "PHD")
    ]
    tipo_conta = [
        (1, "Não Informada"),
        (2, "Conta Corrente"),
        (3, "Conta Salário"),
        (4, "Conta Poupança")
    ]
    categoria = [
        (1, "Mensalista"),
        (2, "Semanalista"),
        (3, "Diarista"),
        (4, "Horista"),
        (5, "Tarefeiro"),
        (6, "Comissionado")
    ]
    emissor = [
        (1, "Policia Federal"),
        (2, "Orgão Emissor Estrangeiro")
    ]
    residencia = [
        (0, "Não"),
        (1, "Sim")
    ]
    deficiencia = [
        (0, "Não"),
        (1, "Sim")
    ]
    plano_de_saude = [
        (0, "Não"),
        (1, "Sim")
    ]
    sindicalizado = [
        (0, "Não"),
        (1, "Sim")
    ]
    grau_parentesco = [
        (1, "conjuguê"),
        (2, "Filho(a) ou enteado(a) até 21 anos"),
        (3, "Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 anos"),
        (4, "Filho(a) ou enteado(a) em qualquer idade, quando incapacitado física e/ou mentalmente para o trabalho"),
        (5, "Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do qual detenha de guarda judicial, até 21 anos"),
        (6, "Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, com idade até 24 anos, se ainda estiver cursando "
            "estabelecimento de nível superior ou escola técnica de 2ºgrau, desde que tenha detido a sua guarda "
            "judicial até os 21 anos"),
        (7, "Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha guarda judicial, em qualquer "
            "idade, quando incapacitado física e/ou mentalmente para o trabalho"),
        (8, "Pais, avós e bisavós"),
        (9, "Menor pobre, até 21 anos, que crie e eduque e o qual detenha guarda judicial"),
        (10, "A pessoa absolutamente incapaz, da qual seja tutor ou curador"),
        (11, "Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 anos"),
        (12, "Ex-cônjugue que receba pensão de alimentos"),
        (13, "Agredado/Outros")
    ]
    return tipo_horario, cor_raca, grau_instrucao, tipo_conta, categoria, emissor, residencia, deficiencia, \
        plano_de_saude, sindicalizado, grau_parentesco


def lista():
    pagamento = [
        ('D', 'Dinheiro'),
        ('C', 'Crédito em Conta')

    ]
    estadoCivil = [
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('J', 'Separado(a) Judicialmente'),
        ('O', 'Concubinato(a)'),
        ('S', 'Solteiro'),
        ('U', 'União Estável'),
        ('V', 'Viúvo()a'),
    ]
    return pagamento, estadoCivil


def dicionario_ocupacional():
    ocupacional = {
        1: "Admissional",
        2: "Periodico",
        3: "Retorno ao Trabalho",
        4: "Manuntenção de Função",
        5: "Monitoração Pontual",
        6: "Demissional"
    }
    resultado = {
        1: "Apto",
        2: "Inapto"
    }
    return ocupacional, resultado

def cabecalho():
    cabecalho_excel = ["Código Funcionario", "Nome Funcionário", "Situação", "Departamento", "Serviço", "Cargo",
                       "Sindicato", "Horário", "Banco", "Município do Endereço", "País do Endereço",
                       "País do Nascimento", "País do Passaporte", "Município do Nascimento",
                       "Tipo de Conta", "Cor", "Grau de Instrução", "Categoria", "Emissor do Passaporte",
                       "Residente Própria", "Deficiência", "Optante Plano de Saúde", "Sindicalizado",
                       "Forma de Pagamento", "Operadora do Plano de Saúde",
                       "Data de adesão", "CPF", "PIS", "Data de Admissão", "Vencimento Férias",
                       "Salário", "Início da Experiência", "Final da Experiência", "Dias de Experiência",
                       "Prorrogação da Experiência", "CTPS", "Nº Série CTPS", "Expedição CTPS",
                       "UF CTPS", "Nº Cartão Ponto", "Horas Mês", "Horas Semana", "Horas Dias",
                        "Conta", "R.G.", "Orgão Exp. R.G.", "UF R.G.",
                       "Data Exp. R.G.", "Nº Passaporte", "UF Passaporte", "Emissão Passaporte",
                       "Validade Passaporte", "Nº Título Eleitor", "Zona Eleitoral",
                       "Seção Eleitoral", "CNH", "Cat. CNH", "Orgão Emissor CNH", "Dt. Exp. CNH",
                       "Estado", "Reservista", "Categoria Reservista", "Vencimento CNH", "CEP",
                       "Endereço", "Nº Endereço", "Complemento Endereço", "Bairro", "E-mail alternativo",
                       "E-mail", "Fone", "Fone 2", "Nascimento", "UF Nascimento", "Naturalizado",
                       "Data Naturalização", "Mãe", "Pai", "Conjugê", "Sexo", "Estado Civil",
                       "Grupo Sanguíneo", "RH Sanguíneo", "Toxicológico Data", "Toxocológico Tipo",
                       "Ex. Ocupacional Tipo", "Ex. Ocupacional Data", "Ex. Ocupacional Resultado",
                       "Ex. Ocupacional Dt. Vencimento", "Nome filho", "Nascimento filho", "CPF filho", "i_filho"]

    return cabecalho_excel
