import json

# Função para carregar dados do arquivo JSON
def carregar_dados(ficheiro_json):
    # Abre o arquivo JSON para leitura
    with open(ficheiro_json, 'r') as file:
         # Carrega o conteúdo do arquivo JSON para a variável dados
        dados = json.load(file)
    # Retorna lista do faturamento diário
    return dados['faturamento_diario']

# Função para calcular informações do faturamento
def calcular_faturamento(faturamento_diario):
    # Cria uma lista com os valores de faturamento ignorando os dias com valor 0
    valores = [item['valor'] for item in faturamento_diario if item['valor'] > 0]

    # Verifica se a lista de valores está vazia
    if not valores:
        # Retorna None para menor e maior faturamento e 0 para dias acima da média
        return None, None, 0

    # Calcula o menor valor do faturamento
    menor_faturamento = min(valores)

    # Calcula o maior valor do faturamento
    maior_faturamento = max(valores)

    # Calcula a média dos valores do faturamento
    media_mensal = sum(valores) / len(valores)

     # Conta o número de dias com faturamento acima da média mensal
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    # Retorna os resultados calculados
    return menor_faturamento, maior_faturamento, dias_acima_media

# Função que executa o programa
def main():
    # Carrega os dados do arquivo JSON
    faturamento_diario = carregar_dados('faturamento.json')
    # Calcula as informações do faturamento
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

     # Verifica se o menor valor do faturamento é None
    if menor is not None:
        # Imprime o menor valor do faturamento
        print(f"Menor valor do faturamento: {menor}")
         # Imprime o maior valor do faturamento
        print(f"Maior valor do faturamento: {maior}")
        # Imprime o número de dias com faturamento acima da média mensal
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    else:
        # Caso não haja dados de faturamento disponíveis imprime uma mensagem
        print("Não há dados de faturamento disponíveis.")

# Verifica se o script está sendo executado
if __name__ == "__main__":
    # Executa função principal
    main()