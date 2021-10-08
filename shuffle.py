import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
ordem = random.shuffle([aluno1,aluno2, aluno3, aluno4])
print(f'A ordem de apresentação será: {ordem}')