vel = float(input('Qual velocidade do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Multado! Você excedeu o limite de velocidade e receberá uma multa no valor de R${multa:.2f}')
    print('Tenha um bom dia! Dirija com segurança!')