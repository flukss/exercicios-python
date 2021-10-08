print('\033[1;36m-=\033[m'*12)
print('\033[1;7;30mAnalisador de triângulos\033[m')
print('\033[1;36m-=\033[m'*12)   #Cores no terminal
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n2+n1:
    print('Os segmentos acima PODEM FORMAR um triângulo!') 
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!') 
