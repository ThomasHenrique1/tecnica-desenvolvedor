from fibonacci import verifica_fibonacci
from faturamento import calcular_faturamento
from representacao import calcular_representacao
from inversao import inverter_string

def questao_1():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print("O valor da variável SOMA ao final do processamento é:", SOMA)

if __name__ == "__main__":
    questao_1()
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    print(verifica_fibonacci(numero))
    calcular_faturamento()
    calcular_representacao()
    string = input("Informe uma string para inverter: ")
    print("String invertida:", inverter_string(string))