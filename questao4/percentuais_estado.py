# Função para calcular o percentual do faturamento por estado
def calcular_percentuais(faturamento_por_estado):
    # Calcula o total do faturamento somando todos os valores do dicionário
    total_faturamento = sum(faturamento_por_estado.values())
    
    # Cria um dicionário para armazenar informações sobre o faturamento
    percentuais = {}
    
    # Revisa sobre cada estado e seu faturamento no dicionário
    for estado, faturamento in faturamento_por_estado.items():
        # Calcula o percentual do faturamento do estado em relação ao total
        percentual = (faturamento / total_faturamento) * 100
        # Armazena o percentual calculado no dicionário de percentuais
        percentuais[estado] = percentual
    
    # Retorna o dicionário com percentuais do faturamento por estado
    return percentuais

# Função que executa o programa
def main():
    # Dicionário armazenando informações sobre o faturamento de diferentes estados
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    # Calcula os percentuais do faturamento usando função definida
    percentuais = calcular_percentuais(faturamento_por_estado)
    
    # Imprime o percentual do faturamento para cada estado
    for estado, percentual in percentuais.items():
        # Exibe o estado e seu percentual formatado com duas casas decimais
        print(f"{estado}: {percentual:.2f}%")

# Verifica se o script está sendo executado 
if __name__ == "__main__":
    # Executa função principal
    main()