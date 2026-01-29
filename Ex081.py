lista, verifica, posicao, igual = [], [], [], []
qtd = cont = indice = 0
existe = False
continuar = ''
print('-' * 60)
print('Vamos fazer uma lista de números do maior para o menor')
print('Vamos mostrar se vc digitou o número 5 \033[1;32mSIM\033[m ou \033[1;31mNÃO\033[m')
print('-' * 60)
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    lista.sort(reverse = True)
    igual = lista[:] #copiar lista
    
    if not(verifica) or not(n in verifica): 
        verifica.append(n)
        qtd += 1
        #impede que números repedido sejam contados
        
    continuar = input('Quer continuar? S/N: ').upper()
    
    while continuar != 'S' and continuar != 'N':
        print('Dados errados!!! faça de novo') 
        continuar = input('Quer continuar? S/N: ').upper()
        #nao deixa o usuário digitar algo diferente de S ou N
        
    if continuar == 'N':
        break
    
if (5 in lista):
    existe = True
    cont = igual.count(5)
    for i in range(cont):
                indice = igual.index(5)
                posicao.append(indice + 1)
                igual[indice] = 0 #impede de contar o mesmo número 5
                                    
                                    
print()                         
print(f'Você digitou \033[1;33m{qtd}\033[m diferente(s)')
print(f'Sua lista de números do MAIOR para o MANOR: \033[1;33m{lista}\033[m')
if existe:
    print(f'Há o número 5 na sua lista nas posição(ões): \033[1;32m{posicao}\033[m')
else:
    print(f'\033[1;31mNÃO HÁ O NÚMERO 5 NA SUA LISTA\033[m')