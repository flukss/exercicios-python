def find_short(frase):
    lista_palavras = frase.split()
    menor_palavra = len(lista_palavras[0])
    for palavra in lista_palavras:
        if len(palavra) < menor_palavra:
            menor_palavra = len(palavra)
    print(menor_palavra)

find_short("bitcoin take over the world maybe who knows perhaps")