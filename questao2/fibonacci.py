def fibonacci_numero(n):
     # Verifica se o número n é menor que 0
    # Se for retorna False por que números negativos não fazem parte da sequência de Fibonacci
    if n < 0:
        return False

    # Função que verifica se um número é um quadrado perfeito
    def quadrado_perfeito(x):
        # Se x é negativo não pode ser um quadrado perfeito então retorna False
        if x < 0:
            return False
        # Calcula a raiz quadrada inteira de x
        s = int(x**0.5)
        # Verifica se o quadrado dessa raiz é igual a x
        return s * s == x
    
    # Verifica se n é um número de Fibonacci utilizando a fórmula matemática
    # A fórmula é baseada na propriedade de que um número é Fibonacci se e somente se
    # um ou os dois valores dos (5*n^2 + 4) ou (5*n^2 - 4) é um quadrado perfeito
    return quadrado_perfeito(5 * n * n + 4) or quadrado_perfeito(5 * n * n - 4)