# Importa a função fibonacci_numero que verifica se um número pertence à sequência de Fibonacci
from fibonacci import fibonacci_numero

def main():

    try:
        num = int(input("Digite um número para verificar se pertence à sequência do Fibonacci: "))
        # Solicita ao usuário para digitar um número inteiro e converte o input para um inteiro.
    except ValueError:
        # Se ocorrer uma exceção do tipo ValueError (por exemplo se o usuário não digitar um número inteiro)
        print("Por favor, digite um número inteiro")
        # Exibe uma mensagem de erro solicitando ao usuário que digite um número inteiro
        return
        # Sai da função main sem prosseguir já que o input não foi um número inteiro
    
    # Chama a função fibonacci_numero para verificar se o número pertence à sequência de Fibonacci
    if fibonacci_numero(num):
        # Se a função retornar True o número pertence à sequência
        print(f"O número {num} pertence à sequência do Fibonacci.")
    else:
        # Caso contrário o número não pertence à sequência
        print(f"O número {num} não pertence à sequência do Fibonacci.")

if __name__ == "__main__":
    # Chama a função main
    main()