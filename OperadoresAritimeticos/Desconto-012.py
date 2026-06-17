#calculating the offer for a client
print('Nosso catálogo está com desconto de 5%!')
original = 129.90
offer = original - (original * 0.05)
def catalogo():
    print("""\n
    === Catálogo ===
    1 - Oversized Marrom
    2 - Oversized Preta
    3 - Oversized Branca
    4 - Oversized Verde
    5 - Oversized Azul
    """)

catalogo()
opcao = input('Esccolha uma opção (1-5): ')

match opcao:
    case "1":
        print('Você escolheu: Oversized Marrom')
        print('Valor Original: {}'.format(original))
        print(f'Valor com desconto {offer:.2f}')
    case "2":
        print('Você escolheu: Oversized Preta')
        print('Valor Original: {}'.format(original))
        print(f'Valor com desconto {offer:.2f}')
    case"3":
        print('Você escolheu: Oversized Branca')
        print('Valor Original: {}'.format(original))
        print(f'Valor com desconto {offer:.2f}')
    case"4":
        print('Você escolheu: Oversized Verde')
        print('Valor Original: {}'.format(original))
        print(f'Valor com desconto {offer:.2f}')
    case"5":
        print('Você escolheu: Oversized Azul')
        print('Valor Original: {}'.format(original))
        print(f'Valor com desconto {offer:.2f}')
    case _: #calue invalid
        print('Opção inválida! Escolha de 1 a 5.')