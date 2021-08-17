'''
|-----------------------------------|
| Modulos: acessando arquivos       |
|-----------------------------------|
'''

# importando arquivos externos
import classes
# importando apenas a classe Televisao do arquivo classes.py
from classes import Televisao

# instanciando uma classe
calculadora = classes.Calculadora();
print(calculadora.soma(10, 5));
print(calculadora.subtracao(20, 30));

televisao = classes.Televisao();
print('Televisão está ligada: {}'.format(televisao.ligada));
televisao.power();
print('Televisão está ligada: {}'.format(televisao.ligada));
televisao.power();
print('Televisão está ligada: {}'.format(televisao.ligada));

print('Canal: {}'.format(televisao.canal));
televisao.aumenta_canal();
print('Canal: {}'.format(televisao.canal));
televisao.diminui_canal();
print('Canal: {}'.format(televisao.canal));