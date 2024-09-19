import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_excel(file_path)
    df['Data'] = pd.to_datetime(df['Data'])
    return df

def prepare_forecast_data(df):
    daily_sales = df.groupby('Data')['Saída'].sum().resample('D').sum()
    return daily_sales

def forecast_sales(data, periods=180):  # Alterado para 180 dias (aproximadamente 6 meses)
    model = ARIMA(data, order=(1,1,1))
    results = model.fit()
    forecast = results.forecast(steps=periods)
    return forecast

def plot_sales(data):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data, label='Saída')
    ax.set_title('Saída de Garrafões de Água')
    ax.set_xlabel('Data')
    ax.set_ylabel('Quantidade')
    ax.legend()
    return fig

def plot_forecast(data, forecast):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data, label='Saída Real')
    ax.plot(forecast.index, forecast, label='Previsão', color='red')
    ax.set_title('Previsão de Saída para os Próximos 6 Meses')
    ax.set_xlabel('Data')
    ax.set_ylabel('Quantidade')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig