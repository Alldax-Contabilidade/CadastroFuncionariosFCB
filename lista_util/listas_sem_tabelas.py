

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
        (0, "indigena"),
        (2, "branca"),
        (4, "negra"),
        (6, "amarela"),
        (8, "parda"),
        (9, "não informada")
    ]
    grau_instrucao = [
        (1, "analfabeto"),
        (2, "ensino fundamental até 5º incompleto"),
        (3, "ensino fundamental até 5º completo"),
        (4, "ensino fundamental 6º ao 9º"),
        (5, "ensino fundamental completo"),
        (6, "ensino medio incompleto"),
        (7, "ensino medio completo"),
        (8, "superior incompleto"),
        (9, "superior completo"),
        (10, "pós graduação"),
        (11, "mestrado"),
        (12, "doutorado"),
        (13, "PHD")
    ]
    tipo_conta = [
        (1, "não informada"),
        (2, "conta corrente"),
        (3, "conta salario"),
        (4, "conta poupança")
    ]
    categoria = [
        (1, "mensalista"),
        (2, "semanalista"),
        (3, "diarista"),
        (4, "horista") ,
        (5, "tarefeiro"),
        (6, "comissionado")
    ]
    emissor = [
        (1, "policia federal"),
        (2, "orgão emissor estrangeiro")
    ]
    residencia = [
        (0, "não"),
        (1, "sim")

    ]
    deficiencia = [
        (0, "não"),
        (1, "sim")
    ]
    plano_de_saude = [
        (0, "não"),
        (1, "sim")
    ]
    sindicalizado = [
        (0, "não"),
        (1, "sim")
    ]

    return tipo_horario, cor_raca, grau_instrucao, tipo_conta, categoria, emissor, residencia, deficiencia, \
           sindicalizado


def dicionario_ocupacional():
    ocupacional = {
        1: "admissional",
        2: "periodico",
        3: "retorno ao trabalho",
        4: "manuntenção de função",
        5: "monitoração pontual",
        6: "demissional"
    }
    resultado= {
        1: "apto",
        2: "inapto"
    }
    return ocupacional, resultado
