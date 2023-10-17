import csv
import random
import pandas as pd

# lendo o arquivo csv
tabela = open('alunos.csv')
type(tabela)

leitura = csv.reader(tabela)

# criando uma lista com a header da tabela
header_tabela = []
header_tabela = next(leitura)

# transformando cada linha da tabela em uma lista
usuarios = []

for usuario in tabela:
    usuario = usuario.strip()
    usuarios.append(usuario.split(","))


# mensagens aleatórias para adicionar a cada usuário
mensagens_aleatorias = ("seu esforço sera recompensado!", "ao continuar seus estudos, voce se garante um futuro melhor!", "continue se esforcando assim!", "nao desista, voce esta quase la!")

# adicionando mensagem aleatória na lista de usuários
for usuario in usuarios:
     random_mensagem = random.choice(mensagens_aleatorias)
     usuario.append(f"{usuario[1]}, {random_mensagem}")

# adicionando coluna "mensagem" na header da tabela
header_tabela.append("mensagem")

# alterando o arquivo csv da tabela
arquivo = 'alunos.csv'
with open(arquivo, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header_tabela)
    csvwriter.writerows(usuarios)

# printando os usuários
for i in range(len(usuarios)):
        print("\n")
        print("id: ", usuarios[i][0])
        print("nome: ", usuarios[i][1])
        print("idade: ", usuarios[i][2])
        print("curso: ", usuarios[i][3])
        print("semestre: ", usuarios[i][4])
        print("mensagem: ", usuarios[i][5])