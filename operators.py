val1 = 1;
val2 = 2;
soma = val1 + val2;
subtracao = val1 - val2;
multiplicacao = val1 * val2;
divisao = val1 / val2;

'''
|-----------------------|
| Operador: Format      |
|-----------------------|
'''
# Operador format concatena qualquer tipo de dados
print('Soma: {} | Subtração: {}\n'.format(soma, subtracao));

# É possível referenciar as variáveis por meio de aliases
print('Soma: {alias1} | Subtração: {alias2}\n'.format(alias1=soma, alias2=subtracao));

# É possível atribuir a string de saída à uma variável
saida = 'Soma: {alias1} | Subtração: {alias2}\n'.format(alias1=soma, alias2=subtracao);
print(saida);

'''
|-----------------------|
| Operador: Input       |
|-----------------------|
'''
# Operador input aguarda usuário digitar um valor
val3 = input('Digite o valor desejado: ');
print('O valor digitado foi: {} '.format(val3));