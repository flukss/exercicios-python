p = float(input('Digite o valor do produto: R$ '))
d = p*5/100
pf = p-d
print('Desconto de 5% gerado no produto é: R${:.2f}'.format(d))
print('Valor final: R${:.2f}'.format(pf))