# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor
# número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. 
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print(f"NOTAS:")

for f in notas:
    qtde = valor // f
    if qtde >= 0.00:
        print(f"{qtde:.0f} nota(s) de R$ {f}.00")
    valor = valor % f

print(f"MOEDAS:")
for m in moedas:
    qtde = valor // m
    if qtde >= 0.00:
        print(f"{qtde:.0f} moeda(s) de R$ {m:.2f}")
    valor = valor % m