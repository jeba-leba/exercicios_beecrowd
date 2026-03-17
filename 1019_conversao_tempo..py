# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
# e informe-o expresso no formato horas:minutos:segundos.

tempo = int(input())
minutos = tempo // 60
horas = minutos // 60

print(f"{horas}:{minutos % 60}:{tempo % 60}")