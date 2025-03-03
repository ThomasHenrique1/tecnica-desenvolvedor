# faturamento.py
import json

def calcular_faturamento():
    with open('dados.json', 'r') as file:
        dados = json.load(file)

    faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

if __name__ == "__main__":
    calcular_faturamento()