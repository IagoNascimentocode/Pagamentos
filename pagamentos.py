print('{} LOJA {}'.format(10*'=',10*'='))
preço = float(input('Valor do produtor R$'))
print('''FORMAS DE PAGEMTO
[ 1 ] À VISTA EM DINHEIRO
[ 2 ] À VISTA NO CARTÃO/DEBITO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opçao = int(input('Qual a opção? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra vai ser parcelada em 2x e cada parcela vai custas {}'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 /100)
    totalparc = int(input('quantas parcelas?'))
    parcela = total / totalparc
    print('sua compra vai ser parcelada em {}x e cada parcela vai custar {} com juros'.format(totalparc,parcela))
else:
    total = preço
    print('Sua opção está incorreta.\ntente de novo.')
print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço,total))

