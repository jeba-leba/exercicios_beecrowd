# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
print(f"{valor}")

for f in notas:
    qtde = valor // f 
    if qtde >= 0:
        print(f"{qtde} nota(s) de R$ {f},00")
    valor = valor % f

