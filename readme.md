Instruções para Rodar o Script main.py

Visão Geral
Este script utiliza pandas para ler e processar vários arquivos CSV relacionados a planos de saúde de abrangência nacional. O objetivo é carregar os dados em um único DataFrame e realizar análises básicas, como visualização de uma amostra dos dados e verificação dos tipos de dados.

Passos para Configurar e Executar o Projeto
1. Instalar a Extensão do Jupyter no VSCode (ou outro editor)
Para facilitar a visualização e execução do código no formato de células, recomendamos instalar a extensão do Jupyter:

Abra o VSCode (ou outro editor de sua preferência).
Vá até a aba de Extensões (ícone de quadrado à esquerda).
Pesquise por "Jupyter" e clique em Instalar.
Isso permitirá que você execute o código em células, diretamente no seu editor.

2. Instalar as Dependências
Antes de rodar o script, é necessário instalar as bibliotecas Python que o projeto utiliza. Para isso, siga os passos abaixo:

Certifique-se de estar no diretório raiz do projeto.

Abra o terminal e execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt

3. Organizar os Arquivos CSV
Para que o script funcione corretamente, você precisará baixar os arquivos CSV e organizá-los da seguinte maneira:

Crie uma pasta chamada data na raiz do projeto.
Dentro da pasta data, crie uma subpasta chamada planos_saude_abrangencia_nacional.
Coloque todos os arquivos CSV relacionados a planos de saúde nessa subpasta (data/planos_saude_abrangencia_nacional).
A estrutura de diretórios deve ficar assim:


seu_projeto/
│
├── data/
│   └── planos_saude_abrangencia_nacional/
│       ├── arquivo1.csv
│       ├── arquivo2.csv
│       └── ...
│
├── main.py
├── requirements.txt
└── README.md

4. Executar o Script
Agora que você configurou tudo, basta executar o script main.py. Se estiver utilizando o Jupyter, você pode rodar célula por célula diretamente no seu editor.


Datasets:
1. Planos de saúde (Nacional)
2. IBGE
3. Orçamento público saúde Brasil