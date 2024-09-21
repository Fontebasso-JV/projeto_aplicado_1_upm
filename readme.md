## Projeto de Saúde e Nutrição com base nos dados do Sisvan

Este projeto tem intuito de contribuir para o planejamento de políticas públicas estaduais, fundamentado nos dados disponíveis na base nacional do Sistema de Vigilância Alimentar e Nutricional (Sisvan). 

## Objetivo

O objetivo do projeto é elaborar um estudo de Análise Exploratória de Dados sobre o contexto do estado nutricional da população brasileira, em específico das crianças com idades compreendidas entre 0 e 6 anos.

## Estrutura do Projeto

- Extrair Dados: Acessar os dados disponíveis sobre estado de nutrição infantil disponível no Datasus e extrair os dados necessários;

- Transformar Dados: Após a etapa de extração, seguiremos com as etapas de filtragem dos dados, processamento e apresentação das informações; 

- Análise e Visualização: Estudo de investigação um conjunto de
dados e sintetizar as suas características principais, usando técnicas e métodos
quantitativos e de visualização de dados, que ampare o planejamento de políticas públicas no combate a desnutrição infantil;

- Relatório Final: Destacaremos as principais descobertas, oferecendo algumas recomendações com base nas percepções encontradas na análise. Com isso, visamos elaborar índices que amparem o Ministério da Saúde e as Secretarias Estaduais a tomar decisões baseadas em dados.

## Recursos Utilizados

- Python

- Google Colab

- Visual Studio Code

- Github


## Bibliotecas Python

- Pandas

- PySpark


## Docentes:

- Professor Thiago Graziani Traue

- Professor Tutor Vinicius Piro Barragam 


## Discentes:

- Bruna Freitas Soares

- Heverton Valerio de Lima

- João Victor Fontebasso Alves

- Mariana Silva de Oliveira


###
---
## Variáveis utilizadas

### **Código do Indivíduo**
> #### CO_PESSOA_SISVAN   
> Código único que identifica
o acompanhamento
realizado pelo indivíduo
> ***  

&nbsp;

### **Código do Município**
> #### CO_MUNICIPIO_IBGE   
> Código IBGE do município.
Identifica o município onde
foi realizado o acompanhamento do
indivíduo.
> ***

&nbsp;

### **Idade em Anos**
> #### NU_IDADE_ANO   
> Anos de vida de uma
pessoa no momento do
acompanhamento.
Cálculo gerado no sistema
de acordo com a Data de
Nascimento
> ***

&nbsp;

### **Sexo**
> #### SG_SEXO   

|Código|Descrição|
|---|---|
|0|Masculino|
|1|Feminino|

&nbsp;


### **Código do Povo ou Comunidade Tradicional**
> #### CO_POVO_COMUNIDADE   

|Código|Descrição|
|---|---|
|1|POVOS QUILOMBOLAS|
|2 | AGROEXTRATIVISTAS|
|3 | CAATINGUEIROS|
|4 | CAIÇARAS|
|5 | COMUNIDADES DE FUNDO E FECHO DE PASTO|
|6 | COMUNIDADES DO CERRADO|
|7 | EXTRATIVISTAS|
|8 | FAXINALENSES|
|9 | GERAIZEIROS|
|10 | MARISQUEIROS|
|11 | PANTANEIROS|
|12 | PESCADORES ARTESANAIS|
|13 | POMERANOS|
|14 | POVOS CIGANOS|
|15 | POVOS DE TERREIRO|
|16 | QUEBRADEIRAS DE COCO-DE-BABAÇU|
|17 | RETIREIROS|
|18 | RIBEIRINHOS|
|19 | SERINGUEIROS|
|20 | VAZANTEIROS|
|21 | OUTROS|

&nbsp;

### **Código da Escolaridade**
> #### CO_ESCOLARIDADE   

|Código|Descrição|
|---|---|
|1|Creche|
|2 | Pré-escola (exceto CA)|
|3 | Classe Alfabetizada - CA|
|4 | Ensino Fundamental 1ª a 4ª séries|
|5 | Ensino Fundamental 5ª a 8ª séries|
|6 | Ensino Fundamental Completo|
|7 | Ensino Fundamental Especial|
|8 | Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª)|
|9 | Ensino Fundamental EJA - séries iniciais (Supletivo 5ª a 8ª)|
|10 | Ensino Médio, Médio 2º Ciclo (Científico, Técnico e etc)|
|11 | Ensino Médio Especial|
|12 | Ensino Médio EJA (Supletivo)|
|13 | Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado|

&nbsp;

### **Estado Nutricional de Peso para Idade de Crianças (0 a 10 anos)**
> #### PESO X IDADE   
> Anos de vida de uma
A fase da vida é calculada
de acordo com a
quantidades de dias de
vida de um indivíduo no
momento do
acompanhamento.
> ***

&nbsp;

### **Estado Nutricional de Altura para Idade de Crianças (0 a 10 anos)**
> #### CRI. ALTURA X IDADE   
> Cálculo Nutricional de
crianças (0 a 10 anos) com
as seguintes informações:
'Muito baixa estatura para
idade', 'Baixa estatura para
idade', 'Estatura
adequada para a idade' 
> ***

&nbsp;

### **Estado Nutricional de IMC para Idade de Crianças (0 a 10 anos)**
> #### CRI. IMC X IDADE
> Cálculo Nutricional de
crianças (0 a 10 anos) com
as seguintes informações:
'Magreza acentuada’,
‘Magreza’, ‘Eutrofia', 'Risco
de sobrepeso',
'Sobrepeso', 'Obesidade' 
> ***

&nbsp;
