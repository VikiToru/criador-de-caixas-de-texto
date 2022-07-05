from math import ceil

while True:
    print('-=-'*11)
    print('''As opções de caixas de texto são:
    [ 0 ] -=-=-
    [ 1 ] +=-=+
    [ 2 ] /--\  \--/''')
    opcao = int(input('Digite uma delas: '))
    
    if opcao == 0 or opcao == 1 or opcao == 2:
        texto = str(input('Digite um texto: '))
        texto_tamanho = len(texto)
        
        if opcao == 0 or opcao == 1:
            if opcao == 0:
                borda_caracteres = '-=-'
            else:
                borda_caracteres = '+=-=+'

            borda_comprimento = len(borda_caracteres)
            borda = borda_caracteres * ceil(texto_tamanho / borda_comprimento)
            
            print(borda + '\n' + texto + '\n' + borda)
        else:
            borda_meio = '-' * (texto_tamanho - 2)
            borda_cima = '/' + borda_meio + '\\'
            borda_baixo = '\\' + borda_meio + '/'

            print(borda_cima + '\n' + texto + '\n' + borda_baixo)
            
        while True:
            resposta_continuar = str(input('Deseja continuar a rodar o programa? [S/N] ')).strip().lower()[0]
            if resposta_continuar in 'sn':
                break
        
        if resposta_continuar == 'n':
            break
    else:
        print('Não entendi. Tente novamente.')
    
print('Programa fechado!')