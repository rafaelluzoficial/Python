'''
|-----------------------------------------------------------------------|
| Tratamento de exceções                                                |
| Documentação em: https://docs.python.org/3/library/exceptions.html    |
|-----------------------------------------------------------------------|
'''
lista = [1, 10];

try:
    # forçando erros
    #divisao = 10 / 0;
    #numero = lista[3];
    x = a;
    numero = lista[0];

# IMPORTANTE: seguir a hierarquia deixando a exceção mais alta por último
# senão todos os erros irão cair nela
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')
except IndexError:
    print('Erro ao acessar item da lista')
except BaseException as ex: # BaseException é o pai de todas as exceções
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa quando não ocorrem exceções')
finally:
    print('Sempre executa dando erro ou não')


# PERSONALIZANDO EXCEÇÕES

# criando classe de exceção obrigatória
class Error(Exception):
    pass

# classe personalizada - pode ser qq nome
class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com um anota de 0 a 10: '))
        print(x)
        # forçando uma exceção com comando raise
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break # força saida do loop

    except ValueError:
        print('Valor inválido. Digite apenas números')
    except InputError as ex:
        print(ex)