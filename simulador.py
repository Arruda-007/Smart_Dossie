# simulador_smart_office.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ------------------------------
# CONFIGURAÇÕES DA SIMULAÇÃO
# ------------------------------
# Período de simulação: 7 dias
dias = 7

# Intervalo entre registros: 15 minutos
intervalo = 15  # em minutos

# Data inicial da simulação
inicio = datetime(2025, 10, 1, 0, 0, 0)  # pode mudar a data se quiser

# ------------------------------
# LISTAS PARA ARMAZENAR DADOS
# ------------------------------
registros = []

# ------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------

def gerar_temperatura(hora):
    """
    Simula temperatura variando ao longo do dia:
    - Mais baixa de madrugada (~20°C)
    - Mais alta à tarde (~26°C)
    """
    if 0 <= hora < 6:
        return np.random.normal(20, 1)  # média 20°C, desvio 1
    elif 6 <= hora < 12:
        return np.random.normal(23, 1)
    elif 12 <= hora < 18:
        return np.random.normal(26, 1)
    else:
        return np.random.normal(22, 1)

def gerar_luminosidade(hora):
    """
    Simula luminosidade em lux:
    - 0 lux à noite
    - Pico entre 10h e 16h (~800 lux)
    """
    if 6 <= hora < 18:
        return np.random.normal(800, 100)  # horário do dia
    else:
        return 0  # noite

def gerar_ocupacao(hora, dia_semana):
    """
    Simula ocupação (0 = livre, 1 = ocupado):
    - Mais pessoas no horário comercial (8h às 18h, dias úteis)
    - Menos pessoas à noite e fins de semana
    """
    if dia_semana < 5:  # dias úteis (0=segunda, 4=sexta)
        if 8 <= hora < 18:
            return np.random.choice([0, 1], p=[0.3, 0.7])  # 70% ocupado
        else:
            return np.random.choice([0, 1], p=[0.8, 0.2])  # 20% ocupado
    else:  # sábado e domingo
        return np.random.choice([0, 1], p=[0.9, 0.1])  # 10% ocupado

# ------------------------------
# LOOP PARA GERAR OS DADOS
# ------------------------------

tempo_atual = inicio
fim = inicio + timedelta(days=dias)

while tempo_atual < fim:
    hora = tempo_atual.hour
    dia_semana = tempo_atual.weekday()  # 0 = segunda, 6 = domingo

    # Gera dados dos três sensores
    temperatura = gerar_temperatura(hora)
    luminosidade = gerar_luminosidade(hora)
    ocupacao = gerar_ocupacao(hora, dia_semana)

    # Adiciona cada dado como um "registro"
    registros.append([tempo_atual, "sensor_temp", "temperatura", round(temperatura, 2)])
    registros.append([tempo_atual, "sensor_lux", "luminosidade", round(luminosidade, 2)])
    registros.append([tempo_atual, "sensor_occ", "ocupacao", ocupacao])

    # Avança 15 minutos
    tempo_atual += timedelta(minutes=intervalo)

# ------------------------------
# TRANSFORMA EM DATAFRAME E SALVA
# ------------------------------

df = pd.DataFrame(registros, columns=["timestamp", "sensor_id", "tipo", "valor"])

# Salva em CSV
df.to_csv("smart_office_data.csv", index=False)

print("Simulação concluída! Arquivo 'smart_office_data.csv' gerado com sucesso.")
