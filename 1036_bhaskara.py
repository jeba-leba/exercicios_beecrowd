# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
# mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

A, B, C = input().split()
delta = (float(B) ** 2) - (4 * float(A) * float(C))
if (delta < 0) or (float(A) == 0):
    print(f"Impossivel calcular")
else:
    R1 = (-float(B) + (delta ** 0.5)) / (2 * float(A))
    R2 = (-float(B) - (delta ** 0.5)) / (2 * float(A))
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
