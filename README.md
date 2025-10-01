# 📌 Projeto Smart Office

Este repositório foi desenvolvido como parte do dossiê do **Projeto Smart Office**, cujo objetivo é **modernizar ambientes corporativos** por meio da implantação de sensores inteligentes de **temperatura, luminosidade e ocupação**.

## 🚀 Objetivo

O projeto visa simular e analisar dados coletados por sensores antes da instalação real, permitindo:

- Testes preliminares do sistema;  
- Avaliação da consistência dos dados;  
- Apoio na geração de relatórios automatizados (Fase 4 do dossiê);  
- Criação de uma base realista para comunicação com stakeholders.  

## 🛠️ Conteúdo do Repositório

- `simulador.py` → Script em **Python** que gera dados simulados dos sensores.  
- `smart_office_data.csv` → Arquivo com **2017 registros** (7 dias de simulação, intervalos de 15 minutos).  
- `README.md` → Explicação deste documento.  

## 📊 Estrutura dos Dados

Cada linha do CSV gerado contém:  
- `timestamp` → Data e hora da medição  
- `sensor_id` → Identificação do sensor  
- `tipo` → Categoria do sensor (temperatura, luminosidade ou ocupação)  
- `valor` → Dado coletado  

**Exemplo:**  
timestamp,sensor_id,tipo,valor
2025-10-01 00:00:00,sensor_temp,temperatura,20.5
2025-10-01 00:00:00,sensor_lux,luminosidade,0.0
2025-10-01 00:00:00,sensor_occ,ocupacao,0

## 🔧 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)  

## 📂 Como Executar

Clone o repositório:  
```bash
git clone https://github.com/Arruda-007/smart_dossie.git
```
Acesse a pasta do projeto:
```bash
cd smart_dossie
```
Instale as dependências:
```bash
pip install pandas numpy
```
Execute o simulador:
```bash
python simulador.py
```
