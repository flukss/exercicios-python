def get_middle(s):
    tam = len(s)
    meio = int(tam / 2)
    meio_impar = round(meio)
    check = tam % 2
    if check == 1:
        print(s[meio_impar])
    else:
        print(f'{s[meio-1]}{s[meio]}')


get_middle('Python')