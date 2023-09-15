numeros = list()
soma = 0
f = [2, 1, 0]
w = 0
for c in range(0, 9):
    if c < 3:
        numeros.append(int(input(f'Digite um número para ser adicionado na matriz [0, {c}]:')))
    elif 6 > c >= 3:
        numeros.append(int(input(f'Digite um número para ser adicionado na matriz [1, {f[-1]}]:')))
        f.pop()
    elif 6 <= c < 9:
        numeros.append(int(input(f'Digite um número para ser adicionado na matriz [2, {w}]:')))
        w += 1
print('-='*20)
for g, v in enumerate(numeros):
    if g == 2 or g == 5:
        print(f'[ {v} ]\n', end='')
    else:
        print(f'[ {v} ]', end=' ')
print('')
print('-='*20)
for num in numeros:
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os valores \033[1mpares\033[:m digitados foi de {soma}.')
print(f'A soma dos valores da \033[1mterceira coluna\033[:m equivalem a {numeros[2] + numeros[5] + numeros[8]}')
print(f'O maior valor da segunda linha foi o {max(numeros[3:6])}')