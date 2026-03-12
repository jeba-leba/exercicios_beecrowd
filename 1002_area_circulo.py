# A fórmula para calcular a área de uma circunferência é: area = π . raio2. 
# Considerando para este problema que π = 3.14159:
# Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

n = float(3.14159)
raio =float(input())
area =float(n * (raio ** 2))
resultado = round(area, 4)

print(f"A={resultado:.4f}")

