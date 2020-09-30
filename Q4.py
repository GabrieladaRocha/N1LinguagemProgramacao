#- Explique o que é decorator e padrões de projeto. Crie um decorator que mostre
#o tempo de execução de uma função que soma 4 números aleatórios.

import datetime

"""
Decorator ->  “O padrão Decorator atribui dinamicamente responsabilidades adicionais a um objeto. 
Os decoradores fornecem uma alternativa de subclasse flexível para estender a funcionalidade. ”

Padrões de Projeto -> são soluções para problemas que alguém já teve e resolveu.
Podendo ser aplicados de acordo com a necessidade do projeto (seguindo um modelo documentado)
"""

def calculate_time(function):
    def calculate_time():
        start = datetime.datetime.now()
        function()
        end = datetime.datetime.now()
        time = end - start
        print("\nO tempo de execução é: ", time)

    return calculate_time


@calculate_time
def ask_numbers():
    number1 = int(input("Digite um número inteiro"))
    number2 = int(input("Digite um número inteiro"))
    number3 = int(input("Digite um número inteiro"))
    number4 = int(input("Digite um número inteiro"))

    result = number1 + number2 + number3 + number4
    print("\nO resultado da soma é: ", result)


ask_numbers()
