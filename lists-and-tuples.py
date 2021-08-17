'''
|---------------------------|
| Lista: valores mutáveis   |
|---------------------------|
'''
# criando listas

lista_inteiros = [5, 3, 1, 7];
lista_animais = ['cachorro', 'gato', 'elefante'];

# acessando valores por meio de indices
print(lista_animais[2]);

# percorrendo lista com for
for i in lista_animais:
    print(i);

# somando valores de uma lista com for
soma = 0;

for i in lista_inteiros:
    soma += i;
print(soma);

# somando valores de uma lista com sum
print(sum(lista_inteiros));

# buscando maior e menor valor com max e min
print(max(lista_inteiros));
print(min(lista_inteiros));

# validando se existe um valor na lista
if 'gato' in lista_animais:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

# Incluindo valores em uma lista com append
if 'lobo' in lista_animais:
    print('Existe um lobo na lista')
else:
    lista_animais.append('lobo')
    print('Lobo foi incluído na lista')
    print(lista_animais)

# retirando um elemento da lista pelo valor
    lista_animais.remove('lobo')
    print('Lobo foi retirado na lista')
    print(lista_animais)

# retirando o último elemento da lista com pop
    lista_animais.pop();
    print(lista_animais);

# multiplicando uma lista
nova_lista_animal = lista_animais * 3;
print(nova_lista_animal);

# ordenando uma lista com sort
lista_animais.sort();
lista_inteiros.sort();
print(lista_animais);
print(lista_inteiros);

# invertendo lista com reverse
lista_animais.reverse();
lista_inteiros.reverse();
print(lista_animais);
print(lista_inteiros);

'''
|---------------------------|
| Tuplas: valores imutáveis |
|---------------------------|
'''
tupla = (1, 10, 12, 14)
print(tupla);

# convertendo lista em tupla
tupla_animal = tuple(lista_animais);
print(tupla_animal);

# convertendo tuplas em listas
lista_tupla = list(tupla);
print(lista_tupla);