# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem: Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X

# %%
A, B, C = map(float, input().split())

valores = [A, B, C]
valores.sort(reverse=True)

A, B, C = valores

if A >= B + C:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")
else:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")

# %%
