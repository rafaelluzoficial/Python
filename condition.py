val1 = int(input('Digite o primeiro valor: '));
val2 = int(input('Digite o segundo valor: '));
resto = 0;
# Operadores de comparação com estruturas condicionais

# Operadores maior > e menor <
if val1 > val2 :
    print('O maior valor é: {}'.format(val1))
elif val1 == val2:
    print('Os valores são iguais. Valor 1 {} | Valor 2 {}'.format(val1,val2))
else:
    print('O maior valor é: {}'.format(val2))

resto = val1 % val2;
print('O resto da divisão entre {} e {} é {}'.format(val1, val2, resto));

# Operadores And, Or, Mod
nota1 = int(input('Digite a nota do 1o Bimestre: '));
nota2 = int(input('Digite a nota do 2o Bimestre: '));
nota3 = int(input('Digite a nota do 3o Bimestre: '));
nota4 = int(input('Digite a nota do 4o Bimestre: '));
media = ((nota1 + nota2 + nota3 + nota4)/4);

if nota1 <= 10 or nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print('Foi informada alguma nota errada');
else:
    print('Média: {}'.format(media));