'''import math
num = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo de {} tem o seno de {:.2f}\n O angulo de {} tem o cosseno de {:.2f}\n O ângulo de {} tem a tangente de {:.2f}'.format(num, sen, num, cos, num, tan))'''

'''import math
num = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o seno de {:.2f}.\nO ângulo de {} tem o cosseno de {:.2f}.\nO ângulo de {} tem a tangente de {:.2f}'.format(num, math.sin(math.radians(num)), num, math.cos(math.radians(num)), num, math.tan(math.radians(num))))'''

from math import radians, sin, cos, tan
num = float(input('Digite um ângulo: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, sin(radians(num))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, cos(radians(num))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(num, tan(radians(num))))