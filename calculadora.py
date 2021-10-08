op = input('Escolha uma operação: \nAdição\nSubtração\nMultiplicação\nDivisão\n')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if op == 'Adição':
    print(n1+n2)
elif op == 'Subtração':
    print(n1-n2)
elif op == 'Multiplicação':
    print(n1*n2)
elif op == 'Divisão':
    print(n1/n2)
else:
    print('Operação não encontrada')