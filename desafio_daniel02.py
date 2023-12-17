print('='*26)
print(f'{'LISTA DE PRODUTOS':^26}')
print('='*26)
print(f'{'GERADOR DE NOTA FISCAL':^26}')
print('='*26)
print(f'{'ITENS A VENDA':^26}')
print(f'{'1-Banana ':-<15} 1,00 R$')
print(f'{'2-Maça ':-<15} 3,00 R$')
print(f'{'3-Laranja ':-<15} 2,00 R$')
print(f'{'4-Abacaxi ':-<15} 5,50 R$')
print(f'{'5-Melancia ':-<15} 10,00 R$')
print(f'{'6-Morango ':-<15} 15,25 R$')
print(f'{'7-Uva ':-<15} 6,50 R$')
print(f'{'8-Pêra ':-<15} 12,50 R$')
print(f'{'9-Mamão ':-<15} 4,50 R$')
print(f'{'10-Kiwi ':-<15} 14,50 R$')
print(f'{'11-Ameixa ':-<15} 11,50 R$')
print(f'{'12-Pêssego ':-<15} 9,50 R$')
print(f'{'13-Cereja ':-<15} 4,50 R$')
print(f'{'14-Limão ':-<15} 0,50 R$')
print(f'{'15-Abacate ':-<15} 3,50 R$')
print(f'{'16-Tomate ':-<15} 2,50 R$')
print(f'{'17-Cenoura ':-<15} 1,50 R$')
print(f'{'18-Batata ':-<15} 2,75 R$')
print(f'{'19-Brócolis ':-<15} 8,50 R$')
print(f'{'20-Pão ':-<15} 1,00 R$')
print('')

cont = 0
soma = 0
itens_escolhidos = []
precos = []

lista_produtos = (
    'Banana', 'Maça', 'Laranja', 'Abacaxi', 'Melancia', 'Morango', 'Uva', 'Pêra', 'Mamão', 'Kiwi', 'Pêssego', 'Ameixa',
    'Cereja', 'Limão', 'Abacate', 'Tomate', 'Cenoura', 'Batata', 'Brócolis', 'Pão')
lista_preco = ( 1, 3, 2, 5.5, 10, 15.25, 6.5, 12.5, 4.5, 14.5, 11.5, 9.5, 4.5, 0.5, 3.5, 2.5, 1.5, 2.75, 8.5, 1 )

while True:
    num = int(input('DIGITE O NÚMERO CORRESPONDENTE AO ITEM QUE DESEJA OU DIGITE 0 PARA SAIR: '))
    print('')
    if num == 0:
        break
    elif num < 1 or num > 20:
        print('O NÚMERO DIGITADO NÃO É VÁLIDO, POR FAVOR DIGITE UM NÚMERO CORRESPONDENTE AO PRODUTO QUE DESEJA: ')
        print('')
    else:

        print(f'O PRODUTO CORRESPONDENTE AO NÚMERO DIGITADO: {lista_produtos[num - 1]} E O SEU VALOR: {lista_preco[num - 1]}R$')
        print('')
        soma += lista_preco[num - 1]
        print(f'SUBTOTAL: {soma}R$')
        print('')
        itens_escolhidos.append(lista_produtos[num-1])
        precos.append(lista_preco[num - 1])
        cont += 1

print('SUA LISTA CONTÉM: ')
for c in range (0, cont):
    print(f'{itens_escolhidos[c]:.<15} {precos[c]}R$')


print(f'ESTE É O VALOR TOTAL DAS SUAS COMPRAS: {soma}R$')