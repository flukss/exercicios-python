def descending_order(num):
    linha = str(num)
    lista = []
    for n in linha:
        lista.append(n)
    lista.sort(reverse=True)
    ordenada = ''.join(lista)
    print(ordenada)