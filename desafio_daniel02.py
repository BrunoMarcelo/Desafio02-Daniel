print('='*26)
print(f"{'LISTA DE PRODUTOS':^26}")
print('='*26)
print(f"{'GERADOR DE NOTA FISCAL':^26}")
print('='*26)
print(f"{'ITENS A VENDA':^26}")
print(f"{'1-Banana ':-<15} 1,00 R$")
print(f"{'2-MAÇA ':-<15} 3,00 R$")
print(f"{'3-LARANJA ':-<15} 2,00 R$")
print(f"{'4-ABACAXI ':-<15} 5,50 R$")
print(f"{'5-MELANCIA ':-<15} 10,00 R$")
print(f"{'6-MORANGO ':-<15} 15,25 R$")
print(f"{'7-UVA ':-<15} 6,50 R$")
print(f"{'8-PÊRA ':-<15} 12,50 R$")
print(f"{'9-MAMÃO ':-<15} 4,50 R$")
print(f"{'10-KIWI ':-<15} 14,50 R$")
print(f"{'11-AMEIXA ':-<15} 11,50 R$")
print(f"{'12-PÊSSEGO ':-<15} 9,50 R$")
print(f"{'13-CEREJA ':-<15} 4,50 R$")
print(f"{'14-LIMÃO ':-<15} 0,50 R$")
print(f"{'15-ABACATE ':-<15} 3,50 R$")
print(f"{'16-TOMATE ':-<15} 2,50 R$")
print(f"{'17-CENOURA ':-<15} 1,50 R$")
print(f"{'18-Batata ':-<15} 2,75 R$")
print(f"{'19-BRÓCOLIS ':-<15} 8,50 R$")
print(f"{'20-PÃO ':-<15} 1,00 R$")
print('')

cont = 0
soma = 0
itens_escolhidos = []
precos = []

lista_produtos = (
    'BANANA', 'MAÇA', 'LARANJA', 'ABACAXI', 'MELANCIA', 'MORANGO', 'UVA', 'PÊRA', 'MAMÃO', 'KIWI', 'AMEIXA', 'PÊSSEGO',
    'Cereja', 'LIMÃO', 'ABACATE', 'TOMATE', 'CENOURA', 'BATATA', 'BRÓCOLIS', 'PÃO')
lista_preco = ( 1, 3, 2, 5.5, 10, 15.25, 6.5, 12.5, 4.5, 14.5, 11.5, 9.5, 4.5, 0.5, 3.5, 2.5, 1.5, 2.75, 8.5, 1 )

while True:
    num = int(input('Digite o número correspondente ao item que deseja OU digite 0 para encerrar: '))
    print('')
    if num == 0:
        print('Se deseja finalizar o pedido e seguir para que seja concluído, digite 0 novamente por favor: ')
        num = input('Se deseja descartar as compras e encerrar, digite Sair: ').upper()
        if num == '0':
            print('')
            print('SUA LISTA CONTÉM: ')
            for c in range(0, cont):
                print(f'{itens_escolhidos[c]:.<15} {precos[c]}R$')
            print(f'ESTE É O VALOR TOTAL DAS SUAS COMPRAS: {soma}R$')
            break
        if num == 'SAIR':
            print('Pedido encerrado por solicitação do usuário')
            break
    elif num < 1 or num > 20:
        print('O número digitado não é válido, por favor digite um número correspondente ao item que deseja: ')
        print('')
    else:
        print(f'O item correspondente ao número digitado: {lista_produtos[num - 1]} \n E o seu valor: {lista_preco[num - 1]}R$')
        print('')
        soma += lista_preco[num - 1]
        print(f'SUBTOTAL: {soma}R$')
        print('')
        itens_escolhidos.append(lista_produtos[num-1])
        precos.append(lista_preco[num - 1])
        cont += 1