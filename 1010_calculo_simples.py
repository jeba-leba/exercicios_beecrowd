# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e 
# o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

cod1, qtd1, preco1 = input().split()
cod2, qtd2, preco2 = input().split()

qtd1 = int(qtd1)
preco1 = float(preco1)

qtd2 = int(qtd2)
preco2 = float(preco2)

total = qtd1 * preco1 + qtd2 * preco2

print(f"VALOR A PAGAR: R$ {total:.2f}")
