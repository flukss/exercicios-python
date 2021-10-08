from random import choice
from time import sleep
pc = ['Pedra', 'Papel', 'Tesoura']
usu = input('Escolha entre pedra, papel e tesoura: ').capitalize()
pc = choice(pc)
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Po...')
sleep(1)
if pc == 'Pedra' and usu == 'Tesoura':
    print('Você perdeu.')
elif pc == 'Papel' and usu == 'Pedra':
    print('Você perdeu.')
elif pc == 'Pedra' and usu == 'Tesoura':
    print('Você perdeu.')
elif pc == 'Tesoura' and usu == 'Pedra':
    print('Você ganhou.')
elif pc == 'Papel' and usu == 'Tesoura':
    print('Você ganhou.')
elif pc == 'Pedra' and usu == 'Papel':
    print('Você ganhou.')
else:
    print('Empate.')
print(f'Escolha do computador {pc}\nEscolha do usuário {usu}')