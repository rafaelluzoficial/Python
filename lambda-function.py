'''
|-----------------------------------|
| Função Lambda: função anônima     |
| Funções simples que resolvemos    |
| com uma única linha               |
|-----------------------------------|
'''

lista_animais = ['cachorro', 'gato', 'elefante'];

# função lambda para contagem de letras
contador_letras = lambda lista: [len(x) for x in lista]
soma = lambda a, b: a + b;

# funções lambda contidas em um dicionário
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

if __name__ == '__main__':
    print(contador_letras(lista_animais));
    print(soma(2, 5));

    # capturando função lambda de dentro de um dicionário
    soma = calculadora['soma'];
    print(soma(10,5));