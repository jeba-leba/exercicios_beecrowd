# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
# A seguir, calcule e mostre o valor da conta a pagar.
# 1 Cachorro Quente R$4.00
# 2 X-Salada R$4.50
# 3 X-Bacon R$5.00
# 4 Torrada simples R$2.00
# 5 Refrigerante R$1.50

#%% 
codigo, qtde = map(int, input().split())

precos = {
            1: 4.00,
            2: 4.50,
            3: 5.00,
            4: 2.00,
            5: 1.50
}

total = precos.get(codigo, 0) * qtde

print(f"Total: R$ {total:.2f}")