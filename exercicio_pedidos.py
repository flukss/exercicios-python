ped = input('Código do pedido: ')
qnt = int(input('Quantidade: '))
chc = 1.20
bau = 1.30
bao = 1.50
hmb = 1.20
che = 1.70
suc = 2.20
ref = 1.00
if ped == '100':
    print(f'Solicitado {qnt} Cachorros-Quentes no valor de {qnt*chc}')
elif ped == '102':
    print(f'Solicitando {qnt} Bauru Simples no valor de {qnt*bau} ')
elif ped == '103':
    print(f'Solicitando {qnt} Bauro com ovo no valor de {qnt*bao}')
elif ped == '104':
    print(f'Solicitando {qnt} Cheeseburger no valor de {qnt*che}')
elif ped == '105':
    print(f'Solicitando {qnt} Sucos no valor de {qnt*suc}')
elif ped == '106':
    print(f'Solicitando {qnt} Refrigerantes no valor de {qnt*ref}')
else:
    print('Fora do menu.')