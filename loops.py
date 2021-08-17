'''
|---------------------------|
| Operadores: For, While    |
|---------------------------|
'''

# Forçar uma repetição até uma determinada condição ocorrer
nota1 = (int(input('Digite uma nota de 0 a 10: ')));
# Verificando condinção de entrada com while
while nota1 > 10:
    nota1 = int(input('Nota {} incorreta. Digite novamente: '.format(nota1)));

# função range estabelece um intervalo de valores
# cada novo valor é imbutido na variável i
for i in range(0, 101):
    print(i);

# Capturar número qualquer e verificar se é primo
num1 = int(input('Insira um número: '));
div = 0;

for i in range(1, num1+1):
    resto = num1 % i
    print(num1, resto);

    if resto == 0:
        div += 1;

if div == 2:
    print('O número {} é primo.'.format(num1));
else:
    print('O número {} NÃO é primo.'.format(num1));
