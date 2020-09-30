"""Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
Faça um método para "traduzir", que recebe uma lista com uma mensagem
(secreta) e "traduz" a sequência armazenada em uma lista."""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


class Translate:
    def decoding(self, text):
        print("Decodificando Frase")
        result = ''
        var = text.split(',')
        for char in var:
            var = char.strip()
            if var == '0':
                result = result + ' '
            else:
                try:
                    index = int(char)
                    char = letters[index - 1]
                    result = result + char
                except:
                    print("valor invalido")
        print(result)

    def aplicacao(self):
        text = input("Digite seu texto!")
        Translate().decoding(text)

    def codifica(self, text):
        print("Codificando Frase")
        result = ''
        var = text.split(',')
        for char in var:
            var = char.strip()
            if var == '0':
                result = result + ' '
            else:
                try:
                    index = int(char)
                    char = letters[index - 1]
                    result = result + char
                except:
                    print("valor invalido")
        print(result)

    def aplicacao(self):
        text = input("Digite seu texto!")
        Translate().decoding(text)

Translate().aplicacao()
