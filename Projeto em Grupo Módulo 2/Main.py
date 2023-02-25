# etapa 1 - main.py:

from csv import *
from time import *
from Censo import *

class main():
    pass

lista=[]
idade=int(input('idade:'))
genero=input('gênero:')
q1=input('reforma previdenciária? (s/n/nsr) \n')
q2=input('reforma trabalhista? (s/n/nsr) \n')
q3=input('reforma tributária? (s/n/nsr) \n')
q4=input('reforma do código penal? (s/n/nsr) \n')
info=Entrevistado(idade,genero)
quest=Questoes(q1,q2,q3,q4)
lista.append(info.idade)
lista.append(info.genero)
lista.append(quest.q1)
lista.append(quest.q2)
lista.append(quest.q3)
lista.append(quest.q4)
print(lista)



'''teste=Final()
print(teste.__init__)'''


