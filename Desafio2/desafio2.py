l1 = int(input('Digite o lado 1: '))
l2 = int(input('Digite o lado 2: '))
l3 = int(input('Digite o lado 3: '))

if {l1} == {l2} == {l3}:
    print('Equilatero!')
elif {l1} == {l2} != {l3} or {l1} != {l2} == {l3}:
    print('Isoceles!')
elif {l1} != {l2} != {l3}:
    print('Escaleno!')