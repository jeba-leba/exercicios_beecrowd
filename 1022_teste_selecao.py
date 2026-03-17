# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D,
# ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

A, B, C, D = input().split()

if (int(B) > int(C)) and (int(D) > int(A)) and ((int(C) + int(D)) > (int(A) + int(B))) and (int(C) > 0) and (int(D) > 0) and (int(A) % 2 == 0):
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")