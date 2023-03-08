###########################################################################################################

## Descrição ##

Este repositório (FAD-PGM2) contém os arquivos utilizados para disponibilizar a infraestrutura necessária à execução do projeto em grupo do Módulo 2 (Estrutura de Dados e Inteligência Emocional) do curso de Formação em Análise de Dados promovido pela parceria SENAC/Resilia.

Sua equipe recebeu uma nova solicitação de projeto! Dessa vez, o objetivo é desenvolver um censo digital com a população de várias cidades do Brasil acerca das últimas reformas governamentais realizadas e com potencial andamento ou atualização por emendas constitucionais.
Para isso, será necessário armazenar os dados dessa pesquisa em um arquivo .csv para utilização em análises futuras. A pesquisa será feita a partir de um levantamento ativo, realizado pelos funcionários da empresa que irão sair com o projeto nas ruas para coletar as respostas.


###########################################################################################################

## Arquivos ##

* **Main.py**: arquivo contendo o código programado em python para execução do projeto de censoriamento.
* **Censo.py**: arquivo contendo o código programado em python com as classes que definem os dados pedidos para cada entrevistado e que são importadas no Main.py.
* **dadoscoletados.csv**: resultados-teste armazenados para demonstração do funcionamento do projeto durante a apresentação.
* **requirements.txt**: arquivo que contém as informações e versões dos pacotes utilizados pelo interpretador necessários ao pleno funcionamento do código.
* **README_PGM2.md**: arquivo que abriga uma breve descrição do projeto com o título, suas funcionalidades e detalhes de implementação.


###########################################################################################################

## Funcionalidades ##

### * 1: Programação Orientada a Objetos ###

```python
class Entrevistado:
    def __init__(self, idade, genero):
        self.idade = idade
        self.genero = genero

class Questoes(Entrevistado):
    def __init__(self, idade, genero, q1, q2, q3, q4, dataehora):
        super().__init__(idade, genero)
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.dataehora = dataehora
```
    
<sub>***No arquivo Censo.py, utiliza-se o paradigma de POO, onde as classes foram criadas para armazenar os dados que serão informados por cada entrevistado. No caso, trabalhamos com o conceito de herança, onde a classe Questoes herda as informações de idade e gênero da classe Entrevistado para associar com cada uma das respostas.***</sub>



### * 2: Importação de bibliotecas para o funcionamento do código principal ###

```python
import csv
import datetime
from time import *
from Censo import *
```

<sub>***Em várias etapas da execução do projeto, alguns comandos necessitam de importação de bibliotecas específicas para o que foi proposto. No caso importamos, respectivamente, bibliotecas para a criação e edição de arquivos CSV através do python, inserção de logs de períodos de tempo de acordo com a execução do código, intervalos de tempo para melhor interface do terminal e utilização de informações de outro código através de classes.***</sub>



### * 3: Início do método para o preparo de cabeçalho e comandos de data/hora ###

```python
class main():
    pass

def Pesquisa():
    idade = ''
    dados = []
    arquivar = open("Projeto em Grupo Módulo 2/dadoscoletados.csv", "w", newline="", encoding="utf-8")
    print('Bem vindx ao censoriamento FAD Census!\nCaso deseje parar, por favor digite 00 quando a idade for pedida.')
    sleep(2)
    gravador = csv.writer(arquivar)
    cabecalho = ['Idade', 'Gênero', 'Questão1', 'Questão2', 'Questão3', 'Questão4', 'Data/Hora']
    gravador.writerow(cabecalho)
    data_e_hora_atuais = datetime.datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y, %H:%M'))
```

<sub>***Inicia-se a classe Main para instanciar as funcionalidades anteriores. Cria-se a função Pesquisa onde há duas variáveis que receberão informações posteriormente e gera-se um arquivo CSV para a adição do cabeçalho da entrevista externamente. Em seguida, criam-se variáveis para salvar data e hora locais da máquina que são, depois, convertidas para o padrão brasileiro.***</sub>



### * 4: Looping para a captação das informações de cada entrevista e prevenção de respostas inválidas  ### 

```python
while idade != '00':
        respostas_permitidas = ['S', 'N', 'NSR']
        identifica = ['M', 'F', 'NSR']
        idade = input('Quantos anos você tem? \n')
        sleep(1)
        idade_limpeza = idade.isdigit()
        if idade_limpeza is False:
            print('Você não digitou uma idade válida!')
            continue
        if idade == '00':
            sleep(3)
            print('Dados coletados com sucesso.')
            sleep(3)
            print('Obrigadx por colaborar com essa pesquisa!')
            sleep(3)
            break
        genero = input('Com qual gênero você se identifica? (m/f/nsr)\n').upper()
        sleep(1)
        if genero not in identifica:
            print('Resposta inválida. Tente novamente no formato m/f/nsr (masculino/feminino/não sei responder).')
            continue
```

<sub>***O looping utiliza-se da idade '00' justamente como forma de interromper os ciclos de informações, permitindo que controlemos a quantidade de entrevistados. Duas listas-padrão são criadas para impedir a inserção de respostas inválidas quanto ao gênero dx entrevistadx e às perguntas propostas do censo. Pelo mesmo princípio, a variável seguinte a essas recebe o comando .isdigit para filtrar respostas inválidas relativas ao formato da idade. Condicionais são adicionadas posteriormente para comparar os inputs realizados com os padrões de respostas que foram definidos, validando-os para serem armazenados ou não.***</sub>



### * 5: Continuação do looping para a captação das respostas acerca das reformas governamentais  ### 

```python
        q1 = input('Você é a favor da reforma previdenciária? (s/n/nsr) \n').upper()
        sleep(1)
        if q1 not in respostas_permitidas:
            print('Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
        
        q2 = input('Você é a favor da reforma trabalhista? (s/n/nsr) \n').upper()
        sleep(1)
        if q2 not in respostas_permitidas:
            print('Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
       
        q3 = input('Você é a favor da reforma tributária? (s/n/nsr) \n').upper()
        sleep(1)
        if q3 not in respostas_permitidas:
            print('Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
     
        q4 = input('Você é a favor da reforma do código penal? (s/n/nsr) \n').upper()
        sleep(1)
        if q4 not in respostas_permitidas:
            print('Resposta inválida. Tente novamente no formato s/n/nsr (sim/não/não sei responder).')
            continue
```

<sub>***Cada uma das quatro perguntas referentes aos modelos de reformas governamentais - cerne desse censoriamento - são feitas através de inputs e já tratadas pelo comando .upper() para seguir o padrão de comparação com as listas da etapa anterior. O esquema do uso de condicionais prossegue da mesma forma.***</sub>



### * 6: Declaração dos atributos das classes para serem armazenados no arquivo CSV  ### 

```python
        dataehora = data_e_hora_em_texto
        quest = Questoes(idade, genero, q1, q2, q3, q4, dataehora)
        dados = [quest.idade, quest.genero, quest.q1, quest.q2, quest.q3, quest.q4, dataehora]
        print('Você deseja continuar? Caso não, por favor digite 00 em seguida.')
        arquivar = open("Projeto em Grupo Módulo 2/dadoscoletados.csv", "a", newline="", encoding="utf-8")
        gravador = csv.writer(arquivar)
        gravador.writerow(dados)
        arquivar.close()
```

<sub>***Salvam-se os atributos dos objetos importados em variáveis que são, depois, organizados em uma lista. Pelo comando de escrita de arquivo csv.writer, cada lista com os dados de um entrevistadx é salva externamente numa linha do arquivo CSV. Por fim, esse mesmo arquivo é fechado e encerra-se o looping.***</sub>



### * 7: Formatação da exibição dos resultados do censo na interface do terminal  ### 

```python
        with open("Projeto em Grupo Módulo 2/dadoscoletados.csv", mode='r', newline='', encoding='utf-8') as arquivo:
        csv_reader = csv.DictReader(arquivo)
        data = list(csv_reader)

        col1 = 6
        col2 = 8
        col3 = 10
        col4 = 10
        col5 = 10
        col6 = 10
        col7 = 20

        sleep(1)
        print(f"{'Idade':<{col1}} {'Gênero':<{col2}} {'Questão1':<{col3}} {'Questão2':<{col4}} {'Questão3':<{col5}} {'Questão4':<{col6}} {'Data/Hora':<{col7}}")
        for row in data:
            sleep(1)
            print(f"{row['Idade']:<{col1}} {row['Gênero']:<{col2}} {row['Questão1']:<{col3}} {row['Questão2']:<{col4}} {row['Questão3']:<{col5}} {row['Questão4']:<{col6}} {row['Data/Hora']:<{col7}}")


Pesquisa()
```

<sub>***Através dos comandos 'with open()' e 'csv.DictReader()', os dados da entrevista são armazenados em diferentes colunas proporcionais ao cabeçalho feito em etapa anterior. Cada variável 'col(número)' corresponde, respectivamente, a um dos itens desse cabeçalho e armazena um número referente à quantidade de caracteres que serão espaçados. Finalizando, os prints organizam essa tabulação numa estrutura de dicionário, que une as chaves cabeçalho a cada valor coluna e as respostas posteriores  de forma semelhante. Na última linha do código, invoca-se a função Pesquisa para a execução de todo o escopo do projeto.***</sub>



### * 8: Censoriamento-teste demonstrativo  ### 

|Idade          |Gênero         |Questão1      |Questão2      |Questão3      |Questão4      |Data/Hora        |
| ------------- | ------------- |------------- |------------- |------------- |------------- |-------------    |
|31             |M	            |S             |S	          |S	         |S             |07/03/2023, 02:59| 
|19             |NSR            |NSR           |S	          |S	         |S             |07/03/2023, 02:59|
|45             |F	            |N             |N	          |N	         |N             |07/03/2023, 02:59|
|50             |M	            |S             |N	          |S	         |S             |07/03/2023, 02:59|
|29             |F	            |S             |S	          |S	         |NSR           |07/03/2023, 02:59|
|58             |M	            |S             |S	          |N	         |S             |07/03/2023, 02:59|
|21             |M	            |NSR           |NSR	          |S	         |N             |07/03/2023, 02:59|
|63             |F	            |S             |S	          |S	         |S             |07/03/2023, 02:59|
|42             |M	            |N             |N	          |N	         |NSR           |07/03/2023, 02:59|
|49             |F	            |NSR           |S	          |S	         |NSR           |07/03/2023, 02:59|


<sub>***Seguindo as propostas do projeto, guardamos entrevistas simuladas com o intuito de mostrar como o arquivo CSV pode ser manipulado, uma vez que é gerado direto pelo interpretador e, depois, aberto e tratado pelo Excel via Power Query.***</sub>



###########################################################################################################
