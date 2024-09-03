# Esta função inverte a string recebida
def inverter_string(s):
    # Cria uma variável para armazenar a string invertida
    string_invertida = '' 
    
    # O loop percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):

         # Adiciona cada caractere da string a nova string invertida
        string_invertida += s[i]
    
    # Retorna string invertida
    return string_invertida

def main():
    
    # Solicita ao usuário que insira uma string para inverter
    string_original = input("Digite a string a ser invertida: ")
    
    # Chama função inverter_string para inverter a string inserida pelo usuário
    resultado = inverter_string(string_original)
    
    # Imprime string invertida
    print("String invertida:", resultado)

if __name__ == "__main__":
    # Executa a função main
    main()