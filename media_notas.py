nome = input('Digite seu nome: ')
a = float(input('Nota da primeira prova: '))
b = float(input('Nota da segunda prova: '))
c = (a+b)/2
print('{}, a média entre as notas de suas provas é {:.1f}'.format(nome, c))