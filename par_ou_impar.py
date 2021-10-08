from random import randint
num = randint(1, 2)
lado = input('Par ou impar? ').capitalize()
num2 = int(input('Escolha um número: '))
r = (num + num2) % 2
print(f'Escolha da máquina: {num}')
if r == 0 and lado == 'Par':
    print('Você ganhou!')
elif r == 1 and lado == 'Impar':
    print('Você ganhou!')
else:
    print('Você perdeu')