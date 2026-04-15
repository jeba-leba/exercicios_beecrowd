# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
# uma linha em branco e em seguida, os valores na sequência como foram lidos.

# %%
a, b, c = map(int, input().split())

resultado = [a, b, c]
resultado.sort()

ordem_1 = resultado[0]
ordem_2 = resultado[1]
ordem_3 = resultado[2]

print(f"{ordem_1}\n{ordem_2}\n{ordem_3}\n\n{a}\n{b}\n{c}")

