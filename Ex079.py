lista = []
while True:
    n = int(input('Adicione um numero: '))
    
    if (n in lista) == False:
        lista.append(n)
        print('\nNumero adicionado!')
        
        continuar = input('Deseja continuar? S/N:  ').upper()
        
        if continuar == 'N':
            break
            
        elif continuar != 'S':
            print('\033[1;31mERROR! Dados invalidos... tente novamente.\033[m')
            continuar = input('Deseja continar? S/N: ').upper()
            if continuar == 'N':
                break
            
    else:
        print('\n \033[1;31mNumero ja adicionado!\033[m')
    
    
lista.sort()
print(f'\nSua lista:  {lista}')