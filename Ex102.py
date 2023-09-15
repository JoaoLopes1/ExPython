from math import factorial
def fatorial(num, show=''):
    if show in 'NNAONÃO':
        return print(f'O fatorial do número {num} é {factorial(num)}.')
    elif show in 'SSIM':
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c}', end=' ')
            else:
                print(f'{c} x', end=' ')
        print()
        return print(f'O fatorial do número {num} é {factorial(num)}.')


fact = int(input('Número:'))
while True:
    show = str(input('Mostrar conta [S/N]:')).strip().upper()
    if show in 'NNAONÃOSSIM':
        break
fatorial(fact, show)