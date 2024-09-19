# Dashboard de Controle de Estoque de Água

Este projeto é um dashboard para visualização e previsão de saída de garrafões de água, desenvolvido como parte de um projeto de extensão.

## Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```bash
   git clone [URL_DO_SEU_REPOSITÓRIO]
   cd [NOME_DO_DIRETÓRIO]
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install pandas matplotlib statsmodels streamlit openpyxl
   ```

## Uso

1. Certifique-se de que seu arquivo Excel com os dados de estoque está no mesmo diretório e nomeado como 'controle-entrada-saida-agua.xlsx'.

2. Execute o dashboard com o seguinte comando:
   ```bash
   streamlit run dashboard.py
   ```

3. O dashboard será aberto automaticamente em seu navegador padrão.

## Funcionalidades

- Visualização dos dados de saída de garrafões de água
- Gráfico de saída histórica
- Previsão de saída para os próximos 6 meses
- Tabela detalhada de previsão
- Resumo mensal da previsão

