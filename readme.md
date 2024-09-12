# 📝 Instruções para Rodar o Script `main.py`

## 🔍 Visão Geral

Este script utiliza **pandas** para ler e processar vários arquivos parquets relacionados ao estado de nutrição da população. O objetivo é carregar os dados em um único DataFrame e realizar análises básicas, como visualização de uma amostra dos dados e verificação dos tipos de dados.

## 🛠️ Passos para Configurar e Executar o Projeto

### 1. Instalar a Extensão do Jupyter no VSCode (ou outro editor) 🧩

Para facilitar a visualização e execução do código no formato de células, recomendamos instalar a extensão do Jupyter:

1. Abra o VSCode (ou outro editor de sua preferência).
2. Vá até a aba de **Extensões** (ícone de quadrado à esquerda).
3. Pesquise por **"Jupyter"** e clique em **Instalar**.

Isso permitirá que você execute o código em células diretamente no seu editor.

### 2. Instalar as Dependências 📦

Antes de rodar o script, é necessário instalar as bibliotecas Python que o projeto utiliza. Para isso, siga os passos abaixo:

1. Certifique-se de estar no diretório raiz do projeto.
2. Abra o terminal e execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### 3. Organizar os Arquivos PARQUET 📁

Para que o script funcione corretamente, você precisará baixar os arquivos parquet e organizá-los da seguinte maneira:

1. Crie uma pasta chamada `data` na raiz do projeto.
2. Dentro da pasta `data`, crie uma subpasta chamada `sisvan.parquet`.
3. Coloque todos os arquivos CSV relacionados a planos de saúde nessa subpasta (`data/sisvan.parquet`).

A estrutura de diretórios deve ficar assim:

    ```
    seu_projeto/
    ├── data/
    │   └── df_novo.parquet/
    │       ├── arquivo1.parquet
    │       ├── arquivo2.parquet
    │       └── ...
    ├── main.py
    ├── requirements.txt
    └── README.md
    ```

### 4. Executar o Script 🚀

Agora que você configurou tudo, basta executar o script `main.py`. Se estiver utilizando o Jupyter, você pode rodar célula por célula diretamente no seu editor.

Para rodar o script completo, use o comando abaixo no terminal:

    ```bash
    python main.py
    ```


Se tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para pedir ajuda! 😊


## 📂 Datasets

Datasets a serem capturados:

1. **SISVAN (Nacional)**: Informações sobre o estado de nutrição e em nível nacional. ✅
2. **IBGE**: Dados do Instituto Brasileiro de Geografia e Estatística, que podem incluir informações demográficas e econômicas. 🔍

