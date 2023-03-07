###########################################################################################################

## Descrição ##

Este repositório (FAD-PGM2) contém os arquivos utilizados para disponibilizar a infraestrutura necessária à execução do projeto em grupo do Módulo 2 (Estrutura de Dados e Inteligência Emocional) do curso de Formação em Análise de Dados promovido pela parceria SENAC/Resilia.

Sua equipe recebeu uma nova solicitação de projeto! Dessa vez, o objetivo é desenvolver um censo digital com a população de várias cidades do Brasil acerca das últimas reformas governamentais realizadas e com potencial andamento ou atualização por emendas constitucionais.
Para isso, será necessário armazenar os dados dessa pesquisa em um arquivo .csv para utilização em análises futuras. A pesquisa será feita a partir de um levantamento ativo, realizado pelos funcionários da empresa que irão sair com o projeto nas ruas para coletar as respostas.


###########################################################################################################

## Arquivos ##

* **Main.py**: arquivo contendo o código programado em python para execução do ...
* **Censo.py**:
* **dadoscoletados.csv**:
* **requirements.txt**:
* **README_PGM2.md**: arquivo que abriga uma breve descrição do projeto com o título, suas funcionalidades e detalhes de implementação.


###########################################################################################################

## Funcionalidades ##

### * 1: Importação de bibliotecas para o aprimoramento da interface do usuário ###

```python
from os import system, name
from time import *


def limpaTela():
    if name == 'nt':
        X = system('cls')
    else:
        X = system('clear')
    return X
```
    
<sub>***Inicia-se o código com um import duplo das bibliotecas 'os' e 'time' com as funções de, respectivamente, permitir a limpeza do conteúdo do terminal ao final da execução do programa e adicionar intervalos de tempo (em segundos) entre etapas exibidas nesse mesmo terminal.***</sub>



### * 2: Recebimento dos dicionários-padrão e variáveis correlacionadas ###

```python
vaga1padrao = {'Vaga 1': 'Python, Programação, Desenvolvimento'}
vaga2padrao = {'Vaga 2': 'Análise de Dados, Dados, SQL'}
for i in vaga1padrao:
    for j in vaga2padrao:
        print(f"Opções: 1: {i} para {vaga1padrao['Vaga 1']}; \n"
              f"        2: {j} para {vaga2padrao['Vaga 2']}; \n"
              f"        0: para encerrar esta etapa."
              )
consulta = True
dictvaga1 = {}
dictvaga2 = {}
quanti_cv1 = 0
quanti_cv2 = 0
quanti_cand1 = 0
quanti_cand2 = 0
```

<sub>***Atribuem-se aos dicionários 'vaga1padrao' e 'vaga2padrao' a enumeração das vagas disponíveis e suas palavras-chave de acordo com o enunciado do projeto. Serão, respectivamente, as chaves e conteúdos daqueles. Depois, são utilizados dois laços 'for' em sequência para a construção da interface de opções que guiam o usuário na escolha das vagas. Em seguida, adicionam-se variáveis que serão chamadas posteriormente no looping e na função final do código.***</sub>



### * 3: Looping para comparação das candidaturas recebidas com as vagas dos dicionários-padrão ###

```python
while consulta != 0:
    consulta = int(input(
        "Informe para qual vaga deseja se inscrever:"))
    resumo = input("Informe seu resumo/minibio para a vaga anterior:")
    if consulta == 1:
        dictvaga1.update({quanti_cv1: resumo})
        quanti_cv1 = quanti_cv1+1
        resuminho = str.lower(resumo)
        resuminho_ = resuminho.split()
        if "python" in resuminho_ and 'programação' in resuminho_ and 'desenvolvimento' in resuminho_:
            quanti_cand1 = quanti_cand1+1
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
    elif consulta == 2:
        dictvaga2.update({quanti_cv2: resumo})
        quanti_cv2 = quanti_cv2+1
        resuminho2 = str.lower(resumo)
        resuminho2_ = resuminho2.split()
        if "análise" in resuminho2_ and 'de' in resuminho2_ and 'dados' in resuminho2_ and 'sql' in resuminho2_:
            quanti_cand2 = quanti_cand2+1
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
    else:
        print("Opção de vaga inválida.")
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
else:
    sleep(3)
    print("Pronto! Carregando análise dos currículos fornecidos...")
sleep(3)
```

<sub>***Cria-se um looping onde o código ficará pedindo para qual vaga a pessoa deseja se candidatar (consulta) e o seu respectivo resumo/minibio (resumo). Com a inserção da quantidade de candidaturas a gosto do usuário, o looping se encerra ao inserir '0' na pergunta das vagas. De acordo com a vaga escolhida, os dicionários vazios 'dictvaga1' e 'dictvaga2' serão atualizados guardando, nas chaves, a quantidade crescente de candidaturas; nos valores, o resumo/currículo das pessoas. Através de comandos para manipulação de strings (.lower e .split), tratam-se cada um dos resumos para checar (via if/elif/else) se temos as palavras-chave necessárias e marcar como um candidato válido para a vaga dento da função seguinte.***</sub>



### * 4: Procedimento para exibição dos resultados finais ### 

```python
def final(dictvaga1, dictvaga2, quanti_cand1, quanti_cand2):
    totais = len(dictvaga1)+len(dictvaga2)
    finalvaga1 = {len(dictvaga1): quanti_cand1}
    finalvaga2 = {len(dictvaga2): quanti_cand2}
    print(f"Foram recebidas {totais} candidaturas no total, sendo \n"
          f"{len(dictvaga1)} para a Vaga 1 e {len(dictvaga2)} para a Vaga 2. \n"
          f"Desse total foram encontrados, respectivamente, \n"
          f"{finalvaga1[len(dictvaga1)]} candidato(s) com currículos pertinentes à Vaga 1 \n"
          f"e {finalvaga2[len(dictvaga2)]} candidato(s) com currículos pertinentes à Vaga 2.")
    print('*'*100)


print(final(dictvaga1, dictvaga2, quanti_cand1, quanti_cand2))
```

<sub>***Cria-se a função 'final' que recebe como argumentos os dicionários atualizados e as variáveis que guardam a quantidade de pessoas aptas pelos seus currículos a cada uma das vagas. O procedimento, ao ser chamado, encerra o código exibindo as candidaturas totais, quantas pessoas estão inscritas em cada vaga e quantas tem o resumo/minibio com as palavras que foram buscadas.***</sub>


###########################################################################################################
