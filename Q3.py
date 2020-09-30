"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido."""

class Number:
    def number(self):
        while True:
            print('Digite uma nota de 0 a 10:')
            note = int(input())
            if note >= 0 and note <= 10:
                break
            else:
                print('Nota invalida, digite uma nota entre 0 e 10')

        print("Nota Válida, obrigada!")

numero = Number()
numero.number()
