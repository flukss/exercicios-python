nota = float(input('Nota do aluno: '))
falta = int(input('Quantidade de faltas: '))
if nota >= 9 and falta <= 20:
    print('Conceito A')
elif nota >= 9 and falta >= 20:
    print('Conceito B')
elif nota >= 8.9 and falta <= 20:
    print('Conceito B')
elif nota >= 8.9 and falta >= 20:
    print('Conceito C')
elif nota >= 7.4 and falta <= 20:
    print('Conceito C')
elif nota >= 7.4 and falta >= 20:
    print('Conceito D')
elif nota >= 4.9 and falta <= 20:
    print('Conceito D')
elif nota >= 4.9 and falta >= 20:
    print('Conceito E')
else:
    print('Conceito E')
