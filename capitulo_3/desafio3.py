quantidade = int(input('Quantos itens deseja em sua lista? \n'))
lista_mercado = []

for i in range(quantidade):

    item = input('Digite o item do mercado: ')

    lista_mercado.append(item)

print(lista_mercado)
