import csv
from time import *
import datetime
from Censo import *


class main():
    pass


def Pesquisa():
                  ################ Variáveis ################
#######################################################################################
    idade = ''
    dados = []
    arquivar = open("csvteste.csv", "w", newline="", encoding="utf-8")
    print('Seja bem vindo(a) a nossa pesquisa!\nCaso deseje parar, favor digitar 00 na idade.')
    gravador = csv.writer(arquivar)
    cabecalho=['Idade','Genero','Questão 1','Questão 2','Questão 3','Questão 4','Data e Hora']
    gravador.writerow(cabecalho)    
    data_e_hora_atuais = datetime.datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y , %H:%M')
#######################################################################################
    while idade != '00':
        respostas_permitidas = 'S'and'N'and'NSR'
        idade = input('Quantos anos você tem? \n')
        idade_limpeza = idade.isdigit() #Variável que retorn true se idade é válida.
        if idade_limpeza is False: #Se o usuario digitar uma idade invalida irá aparecer essa mensagem.
            print('Você não digitou uma idade válida!')
            continue
        if idade == '00':
            print('Dados coletados.\nObrigado por fazer parte da nossa pesquisa')
            break
        genero = input('Qual gênero você se identifica?\n').upper()
        #Primeira pergunta e tratamendo de dados.
        q1 = input('Você é a favor da reforma previdenciária? (s/n/nsr) \n').upper()
        if q1 not in respostas_permitidas:
            print('Resposta Inválida.')
            continue
        #Segunda pergunta e tratamendo de dados.
        q2 = input('Você é a favor da reforma trabalhista? (s/n/nsr) \n').upper()
        if q2 not in respostas_permitidas:
            print('Resposta Inválida.')
            continue 
        #Terceira pergunta e tratamendo de dados.
        q3 = input('Você é a favor da reforma tributária? (s/n/nsr) \n').upper()
        if q3 not in respostas_permitidas:
            print('Resposta Inválida.')
            continue 
        #Quarta pergunta e tratamendo de dados.               
        q4 = input('Você é a favor da reforma do código penal? (s/n/nsr) \n').upper()
        if q4 not in respostas_permitidas:
            print('Resposta Inválida.')
            continue
            
        dataehora = data_e_hora_em_texto
        #Declarando os paramentros da Classe Questões.
        quest = Questoes(idade, genero, q1, q2, q3, q4, dataehora)
        #Lista onde os dados estão sendo guardados.
        dados = [quest.idade, quest.genero,
            quest.q1, quest.q2, quest.q3, quest.q4, dataehora]
        print('Você deseja continuar? Caso não, favor digitar 00 na idade.')
        print(dados)
        #Criando o arquivo CSV onde será guardado os dados.
        arquivar = open("csvteste.csv", "a", newline="", encoding="utf-8") #arquivar = open("Projeto em Grupo Módulo 2/csvteste.csv", "w", newline="", encoding="utf-8")

        #Gravando dados no CSV.
        gravador = csv.writer(arquivar)
        gravador.writerow(dados)
        #Fechando Arquivo.
        arquivar.close()


Pesquisa()
