# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais

nome = input()
salario_fixo = float(input())
vendas_valor = float(input())
bonus = vendas_valor * 0.15

total_salario = salario_fixo + bonus

print(f"TOTAL = R$ {total_salario:.2f}")