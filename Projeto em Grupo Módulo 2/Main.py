#########################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)                   #
#  Projeto em Grupo - Módulo 2 - Quero os Dados na Minha Mesa           #
#  !/usr/bin/env python3                                                #
#  -*- coding: utf-8 -*-                                                #
#  Criado por: Davi de Moraes Novaes e Douglas Klem Portugal do Amaral  #
#  Data de criação: 24/02/2023                                          #
#  versão = '3.11(64-bit)'                                              #
#########################################################################

import csv
import datetime
from time import *
from Censo import *


class main():
    pass


def Pesquisa():
    ################ Variáveis ################
    #######################################################################################
    idade = ''
    dados = []
    print('*'*100)
    arquivar = open("Projeto em Grupo Módulo 2/dadoscoletados.csv",
                    "w", newline="", encoding="utf-8")
    print('Bem vindx ao censoriamento FAD Census!\nCaso deseje parar, por favor digite 00 quando a idade for pedida.')
    print('*'*100)
    sleep(2)
    gravador = csv.writer(arquivar)
    cabecalho = ['Idade', 'Gênero', 'Questão 1',
                 'Questão 2', 'Questão 3', 'Questão 4', 'Data e Hora']
    gravador.writerow(cabecalho)
    data_e_hora_atuais = datetime.datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y, %H:%M')
#######################################################################################
    while idade != '00':
        respostas_permitidas = ['S', 'N', 'NSR']
        identifica = ['M', 'F', 'NSR']
        idade = input('Quantos anos você tem? \n')
        print('*'*100)
        sleep(1)
        # Variável que retorna True se a idade for válida.
        idade_limpeza = idade.isdigit()
        # Caso o usuário digite uma idade inválida, aparecerá uma mensagem confirmando isso.
        if idade_limpeza is False:
            print('Você não digitou uma idade válida!')
            continue
        if idade == '00':
            print(' ')
            print('...')
            sleep(3)
            print(' ')
            print('Dados coletados com sucesso.')
            sleep(3)
            print(' ')
            print('Obrigadx por colaborar com essa pesquisa!')
            print(' ')
            break
        genero = input(
            'Com qual gênero você se identifica? (m/f/nsr)\n').upper()
        print('*'*100)
        sleep(1)
        if genero not in identifica:
            print(
                'Resposta inválida. Tente novamente no formato m/f/nsr (masculino/feminino/não sei responder).')
            continue
        # Primeira pergunta e tratamento de dados.
        q1 = input(
            'Você é a favor da reforma previdenciária? (s/n/nsr) \n').upper()
        print('*'*100)
        sleep(1)
        if q1 not in respostas_permitidas:
            print(
                'Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
        # Segunda pergunta e tratamento de dados.
        q2 = input('Você é a favor da reforma trabalhista? (s/n/nsr) \n').upper()
        print('*'*100)
        sleep(1)
        if q2 not in respostas_permitidas:
            print(
                'Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
        # Terceira pergunta e tratamento de dados.
        q3 = input('Você é a favor da reforma tributária? (s/n/nsr) \n').upper()
        print('*'*100)
        sleep(1)
        if q3 not in respostas_permitidas:
            print(
                'Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
        # Quarta pergunta e tratamento de dados.
        q4 = input(
            'Você é a favor da reforma do código penal? (s/n/nsr) \n').upper()
        print('*'*100)
        sleep(1)
        if q4 not in respostas_permitidas:
            print(
                'Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue

        dataehora = data_e_hora_em_texto
        # Declarando os parâmetros da Classe Questoes.
        quest = Questoes(idade, genero, q1, q2, q3, q4, dataehora)
        # Lista onde os dados estão sendo guardados.
        dados = [quest.idade, quest.genero,
                 quest.q1, quest.q2, quest.q3, quest.q4, dataehora]
        print('Você deseja continuar? Caso não, por favor digite 00 em seguida.')
        print('\n')
        # Criando o arquivo CSV onde os dados ficarão armazenados.
        arquivar = open("Projeto em Grupo Módulo 2/dadoscoletados.csv",
                        "a", newline="", encoding="utf-8")
        # Gravando dados no CSV.
        gravador = csv.writer(arquivar)
        gravador.writerow(dados)
        # Fechando o arquivo.
        arquivar.close()

    with open("Projeto em Grupo Módulo 2/dadoscoletados.csv", mode='r', newline='', encoding='utf-8') as arquivo:
        csv_reader = csv.DictReader(arquivo)
        data = list(csv_reader)

        # Define o tamanho de cada coluna.
        col1 = 6
        col2 = 8
        col3 = 10
        col4 = 10
        col5 = 10
        col6 = 10
        col7 = 20

        # Imprime o cabeçalho das colunas.
        print('='*100)
        print(f"{'Idade':<{col1}} {'Gênero':<{col2}} {'Questão 1':<{col3}} {'Questão 2':<{col4}} {'Questão 3':<{col5}} {'Questão 4':<{col6}} {'Data e Hora':<{col7}}")

        # Imprime os dados em colunas.
        for row in data:
            print(f"{row['Idade']:<{col1}} {row['Gênero']:<{col2}} {row['Questão 1']:<{col3}} {row['Questão 2']:<{col4}} {row['Questão 3']:<{col5}} {row['Questão 4']:<{col6}} {row['Data e Hora']:<{col7}}")
        print('='*100)


Pesquisa()
