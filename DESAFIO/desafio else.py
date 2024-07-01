# TODO: receber as notas

n1 = int(input('Entre com a nota da p1:'))
n2 = int(input('Entre com a nota da p2:'))

# TODO: caluclar média

media = (n1 + n2) / 2

# TODO resultado

if media == 10:
    print("Aprovado com mérito!")
elif media >=7:
    print('Aprovado!')
else:
    print('Reprovado!')