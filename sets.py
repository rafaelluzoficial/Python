'''
|-----------------------------------|
| Conjuntos                         |
| Métodos: União, Intersecção       |
| Diferença, Diferença simétrica    |
| Remoção de duplicidade            |
| Não permite duplicidade de dados  |
|-----------------------------------|
'''

conjunto = {1, 2, 3, 4};
print(conjunto);

# adicionando elementos ao conjunto com add
conjunto.add(5);
print(conjunto);

# removendo elemntos do conjunto com discard
conjunto.discard(5);
print(conjunto);

conjunto1 = {1, 2, 3, 4, 5};
conjunto2 = {5, 6, 7, 8};
print('Conjunto 1 {}'.format(conjunto1));
print('Conjunto 2 {}'.format(conjunto2));

# método de união entre conjuntos
conjunto_uniao = conjunto1.union(conjunto2);
print('União {}'.format(conjunto_uniao));

# método de intersecção entre conjuntos
conjunto1 = {1, 2, 3, 4, 5};
conjunto2 = {5, 6, 7, 8};
conjunto_intersec = conjunto1.intersection(conjunto2);
print('Intersecção {}'.format(conjunto_intersec));

# método de diferença entre conjuntos
conjunto1 = {1, 2, 3, 4, 5};
conjunto2 = {5, 6, 7, 8};
conjunto_dif = conjunto1.difference(conjunto2);
print('Diferença {}'.format(conjunto_dif));

# diferença simétrica
conjunto_dif_symetric = conjunto1.symmetric_difference(conjunto2);
print('Diferença Simétrica {}'.format(conjunto_dif_symetric));

# pertinência = se um cojunto faz parte do outro com subset e superset
conjunto_a = {1, 2, 3};
conjunto_b = {1, 2, 3, 4, 5};
conjunto_subset = conjunto_a.issubset(conjunto_b);
conjunto_superset = conjunto_b.issuperset(conjunto_a);
print('A é subconjunto de B: {}'.format(conjunto_subset));
print('B é superconjunto de A: {}'.format(conjunto_superset));

# convertendo uma lista para conjunto para remover duplicidade
lista_animais = ['cachorro', 'gato', 'gato', 'elefante', 'elefante'];
print(lista_animais);
lista_animais = set(lista_animais);
print(lista_animais);
lista_animais = list(lista_animais);
print(lista_animais);