# Program Mencari Persamaan Kuadrat

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a == 0:
    print('\nBukan persamaan kuadrat karena a = 0')
    exit()

det = (b**2) - (4*a*c)
akar_det = det**(1/2)

if det < 0:
    print('Akar Imajiner')

elif det == 0:
    x1 = (-b + akar_det) / (2*a)
    print(f'\nx1 = {x1}')
    x2 = x1
    print(f'x2 = {x2}')

else:
    x1 = (-b + akar_det) / (2*a)
    print(f'\nx1 = {x1}')
    x2 = (-b - akar_det) / (2*a)
    print(f'x2 = {x2}')