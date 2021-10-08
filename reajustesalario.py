s = float(input('Seu salário atual: R$'))
a = (s*15)/100
sf = s+a
print('Seu reajuste salarial ficou em: R${:.2f}'.format(sf))
print('Acréscimo de R${:.2f}'.format(a))