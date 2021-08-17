'''
|-----------------------------------|
| Manipulando data e hora           |
|-----------------------------------|
'''

# biblioteca datetime para trabalhar com data/hora
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    # variavel do tipo datetime
    data_atual = date.today()
    print(data_atual);

    # formatando data convertendo para string
    print(data_atual.strftime('%d/%m/%y'));
    # ano completo
    print(data_atual.strftime('%d/%m/%Y'));
    print(data_atual.strftime('%A/%B/%Y'));

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.hour)
    tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom')
    print(tupla[data_atual.weekday()]) # weekday retorna o indice do dia da semana: segunda = 0, terça = 1...
    data_criada = datetime(2018,6,20,15,30,20)
    print(data_criada.strftime('%c'))

    #convertendo strig com data para datetime
    str_data = '10/01/2019'
    str_data_conv = datetime.strptime(str_data, '%d/%m/%Y')
    print(str_data_conv)

    #subtração e soma de datas com biblioteca timedelta
    nova_data = str_data_conv - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_date();
    trabalhando_com_time();
    trabalhando_com_datetime();