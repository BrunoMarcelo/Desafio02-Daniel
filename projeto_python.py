#Propósito do código
print('='*26)
print(f"{'LISTA DE PRODUTOS':^26}")
print('='*26)
print(f"{'GERADOR DE NOTA FISCAL':^26}")
print('='*26)
print('')

#Solicita o nome do cliente e armazena na váriavel: nome
nome = str(input('Digite seu nome e sobrenome por favor: ')).upper()
idade = int(input('Digite sua idade: '))

#Solicita CPF e verifica se é válido (11 dígitos)
while True:
    cpf_cliente = str(input('Digite o CPF completo por favor: '))
    if len(cpf_cliente) < 11 or len(cpf_cliente) > 11:
        print('CPF INVÁLIDO')
    else:
        break

#Itens a venda e seus respectivos preços
print('')
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
print(f"{'21-SKOLL ':-<15} 3,50,00 R$")
print(f"{'22-BRAHMA ':-<15} 3,00 R$")
print(f"{'23-HEINEKEN ':-<15} 9,00 R$")
print(f"{'24-DEVASSA ':-<15} 5,00 R$")
print(f"{'25-ITAIPAVA ':-<15} 3,00 R$")
print('')

#Váriaveis de controle
cont = 0
soma = 0

#Listas que vão ser usadas no código e preenchidas
itens_escolhidos = []
precos = []

#Listas imutáveis que são usadas no código
lista_produtos = (
    'BANANA', 'MAÇA', 'LARANJA', 'ABACAXI', 'MELANCIA', 'MORANGO', 'UVA', 'PÊRA', 'MAMÃO', 'KIWI',
    'AMEIXA', 'PÊSSEGO', 'Cereja', 'LIMÃO', 'ABACATE', 'TOMATE', 'CENOURA', 'BATATA', 'BRÓCOLIS', 'PÃO', 'SKOLL', 'BRAHMA', 'HEINEKEN', 'DEVASSA', 'ITAIPAVA')
lista_preco = (1, 3, 2, 5.50, 10, 15.25, 6.50, 12.50, 4.50, 14.50, 11.50, 9.50, 4.50, 0.50,
               3.50, 2.50, 1.50, 2.75, 8.50, 1, 3.50, 3, 9, 5, 3)

lista_vips = ('BRUNO MARCELO', 'MATHEUS GALDINO', 'DANIEL CABRAL', 'RAFAEL CABRAL', 'ALEXANDRE MOURA',
              'HUGO MOURA', 'PAULA SIMONE', 'JOÃO VICTOR', 'ADRIANA NASCIMENTO', 'FERNANDA MONTEIRO')

#Início da lógica
#Começa por um while True para que o código seja executado até que o usuário digite a opção que leva ao Break
while True:
    num = int(input('Digite o número correspondente ao item que deseja OU digite 0 para encerrar: '))
    print('')

    #Caso cliente solicite encerrar o programa
    if num == 0:
        print('Se deseja finalizar o pedido e seguir para que seja concluído, digite 0 novamente por favor')
        num = input('Se deseja descartar as compras e encerrar, digite Sair: ').upper()

        #Se cliente escolher 0 novamente irá gerar a nota fiscal
        if num == '0':

            print('')
            print('SUA LISTA CONTÉM: ')

            #Comando for para que seja gerada a lista de itens escolhidos (carrinho de compras)
            for c in range(0, cont):
                print(f'{itens_escolhidos[c]:.<15} {precos[c]}R$')

            #Verifica se o nome digitado faz parte da lista de clientes vips
            if nome in lista_vips:
                print('')
                print(f'Cliente: {nome} CPF: {cpf_cliente} (Clube de descontos VIP)')
                print(f'Este é o valor total das suas compras: {soma}R$')
                print('')
                print('Por fazer parte do nosso clube de clientes VIP, iremos aplicar um desconto no valor total')
                print('')
                print(f'Este é o valor total das suas compras com o desconto aplicado: {soma * 0.9:.2f}R$')
                print('Sr(a) recebeu 10% de desconto nos itens a venda!')

            #Caso cliente não faça parte da lista de clientes vips
            else:
                print('')
                print(f'Cliente: {nome} CPF: {cpf_cliente}')
                print(f'Este é o valor total das suas compras: {soma}R$')
            break
        #Encerra o programa e descarta quaisquer itens que o usuário tenha selecionado
        if num == 'SAIR':
            print('Pedido encerrado por solicitação do usuário')
            break

    #Caso o número seja digitado incorretamente
    elif num < 1 or num > 25:
        print('O número digitado não é válido, por favor digite um número correspondente ao item que deseja: ')
        print('')
    #Verifica se o cliente é menor de idade e escolheu um produto +18
    elif idade <18 and num > 20:
        print('Produto não disponível, cliente menor de idade!')
        print('')

    #Caso o número digitado pertença a lista de itens a venda
    else:
        print(f'O item correspondente ao número digitado: {lista_produtos[num - 1]} \n E o seu valor: {lista_preco[num - 1]}R$')
        print('')

        #Adiciona o valor do produto a variável soma que gera o valor total das compras
        soma += lista_preco[num - 1]
        print(f'SUBTOTAL: {soma}R$')
        print('')

        #Adiciona os itens escolhidos ao "carrinho"
        itens_escolhidos.append(lista_produtos[num-1])
        precos.append(lista_preco[num - 1])

        #Contador utilizado para o comando for, que irá gerar o "carrinho"
        cont += 1