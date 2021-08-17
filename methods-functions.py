'''
|-----------------------------------|
| Métodos e funções                 |
|-----------------------------------|
'''

# definindo funções (retornam algum valor)
def soma(a, b):
    return a + b;

print(soma(3,4));
print(soma(5,10));

# definindo classes
class Calculadora:
    # iniciando variáveis da classe
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b;

    def subtracao(self):
        return self.valor_a - self.valor_b;

# instanciando uma classe
calculadora = Calculadora(10, 2);
print(calculadora.soma());
print(calculadora.subtracao());