dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print(f'O valor de sua viagem será de R${preço:.2f}')