'''
|-----------------------------------|
| Manipulando arquivos              |
|-----------------------------------|
'''
import shutil # usando nos métodos de mover e copiar arquivos

def escrever_arquivo(texto):
    # cirando arquivo ou abrindo arquivo existente
    # parâmetro w = write -> atualiza arquivo inteiro
    # parâmetro a = insere nova linha
    # parâmetro r = read -> lê arquivo

    arquivo = open('teste.txt', 'w')
    # escrevendo em um arquivo
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arq, texto):
    arquivo = open(nome_arq, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arq):
    arquivo = open(nome_arq, 'r')

    # conteúdo do arquivo vem como uma string
    alunos_notas = arquivo.read()
    #print(alunos_notas)

    # quebra conteúdo do arquivo em uma lista
    alunos_notas = alunos_notas.split('\n')
    #print(alunos_notas)

    # lista que conterá as médias dos alunos
    lista_media = []

    for i in alunos_notas:
        # separa nome dos alunos de suas notas em uma lista
        lista_notas = i.split(',')
        #print(lista_notas)

        # coloca o nome do aluno em uma variável
        aluno = lista_notas[0]

        # retira o nome do aluno da lista - 1o elemento
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)

        media = lambda notas: sum([int(x) for x in notas]) / len(notas)
        # adiciona a média do aluno na lista de médias como dicionário
        lista_media.append({aluno:media(lista_notas)})
        # retorna a lista contendo um dicionário de alunos e suas médias
    return lista_media

def copia_arquivo(nome_arq):
    shutil.copy(nome_arq, '~Workspace/')

def move_arquivo(nome_arq):
    shutil.move(nome_arq, '~Workspace/')

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha\n');
    #atualizar_arquivo('teste.txt', 'Rafael,10,20,30\n');
    #atualizar_arquivo('teste.txt', 'Gabriel,40,50,60\n');
    #atualizar_arquivo('teste.txt', 'Duda,70,80,90\n');
    #ler_arquivo('teste.txt');
    #copia_arquivo();
    #move_arquivo();

    lista_media = media_notas('teste.txt');
    print(lista_media);