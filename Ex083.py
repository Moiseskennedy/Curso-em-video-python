print('Vamos verificar se o parênteses da expressão matematica que você escrever é valido! ')
print('-' * 40)
exp = input('Digite uma expressão: ')

aberto = exp.count('(')
fechado = exp.count(')')
if aberto == fechado:
    print('\033[1;32mExpressão valida!\033[m')
else:
    print('\033[1;31mExpressão inválida\033[m')