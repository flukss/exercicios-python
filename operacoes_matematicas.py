a = int(input('Diga um número: '))
b = int(input('Diga outro número: '))
s = a + b
m = a * b
d = a / b
di = a // b
e = a ** b
print('A soma é {}\nO produto é {}\nA divisão é {:.2}'.format(s, m, d), end =' ')
print('A divisão real é {}\nA potência é {}'.format(di, e))
