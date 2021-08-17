'''
|-----------------------------------|
| Classes                           |
|-----------------------------------|
'''
# definindo classes
class Calculadora:
    # iniciando variáveis da classe
    def __init__(self):
        pass # se não colocar, dá pau!

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b;

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b;

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False;
        else:
            self.ligada = True;

    def aumenta_canal(self):
        self.canal +=1;

    def diminui_canal(self):
        self.canal -=1;

# quando for o main que chama, executa o código abaixo, senão não faz nada
if __name__ == '__main__':

    # instanciando uma classe
    calculadora = Calculadora();
    print(calculadora.soma(10, 5));
    print(calculadora.subtracao(20, 30));

    televisao = Televisao();
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