import csv
from time import *
from datetime import date
from Censo import *


class main():
    pass


def Pesquisa():
    idade = ''
    dados = {}
    print('Seja bem vindo(a) a nossa pesquisa!\nCaso deseje parar, favor digitar 00 na idade.')
    while idade != '00':

        idade = input('idade:')
        if idade == '00':
            print('Dados coletados.\nObrigado por fazer parte da nossa pesquisa')
            break
        genero = input('gênero:')
        q1 = input('reforma previdenciária? (s/n/nsr) \n')
        q2 = input('reforma trabalhista? (s/n/nsr) \n')
        q3 = input('reforma tributária? (s/n/nsr) \n')
        q4 = input('reforma do código penal? (s/n/nsr) \n')
        quest = Questoes(idade, genero, q1, q2, q3, q4)
        dados[quest.idade, quest.genero] = (
            quest.q1, quest.q2, quest.q3, quest.q4)
        print('Você deseja continuar? Caso não, favor digitar 00 na idade.')
        print(dados)

        arquivar = open("Projeto em Grupo Módulo 2/csvteste.csv", "w", newline="", encoding="utf-8")
        gravador = csv.writer(arquivar)
        cabecalho=['cabecalho de teste']
        gravador.writerow(cabecalho)
        dadosk=dados.keys()
        dadosv=dados.values()
        for i,j in zip(dadosk,dadosv):
            gravador.writerow(i)
            gravador.writerow(j)
        arquivar.close()


Pesquisa()

