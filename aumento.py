sal = float(input('Qual o salário do funcionário? '))
if sal <= 1250:
    aum = (sal*15/100) + sal
else:
    aum = (sal*10/100) + sal
print(f'Quam ganhava {sal} passa a ganhar {aum:.2f}')