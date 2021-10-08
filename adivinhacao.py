from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5... Você consegue adivinhar?')
print('-=-' * 20)
usr = int(input('Escolha um número: '))
print('PROCESSANDO...')
sleep(3)
print(f'Número pensado foi {num}')
if usr == num:
    print('Você venceu!')
else:
    print('Você perdeu.')