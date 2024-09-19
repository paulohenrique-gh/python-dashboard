import streamlit as st
import pandas as pd
from main import load_data, prepare_forecast_data, forecast_sales, plot_sales, plot_forecast

st.set_page_config(page_title="Dashboard de Saída de Água", layout="wide")

@st.cache_data
def get_data():
    return load_data('controle-entrada-saida-agua.xlsx')

def main():
    st.title('Dashboard de Saída de Garrafões de Água')

    df = get_data()
    
    st.subheader('Visão Geral dos Dados de Saída')
    st.dataframe(df[['Data', 'Saída']])

    daily_sales = prepare_forecast_data(df)

    st.subheader('Gráfico de Saída')
    st.pyplot(plot_sales(daily_sales))

    forecast = forecast_sales(daily_sales)

    st.subheader('Previsão de Saída para os Próximos 6 Meses')
    st.pyplot(plot_forecast(daily_sales, forecast))

    st.subheader('Tabela de Previsão')
    forecast_df = pd.DataFrame({'Data': forecast.index, 'Previsão de Saída': forecast.values.round().astype(int)})
    st.dataframe(forecast_df)

    st.subheader('Resumo Mensal da Previsão')
    monthly_forecast = forecast_df.set_index('Data').resample('M').sum()
    monthly_forecast.index = monthly_forecast.index.strftime('%B %Y')
    st.dataframe(monthly_forecast)

if __name__ == '__main__':
    main()