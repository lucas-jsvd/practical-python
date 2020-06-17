# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
numero_meses_pagamento = 0

print("Olá, seja bem-vindo ao programa de calculo de financiamento.")
mes_ini_pag_extra = int(input("Qual o mês inicial do pagamento extra ? "))
mes_final_pag_extra = int(input("Qual o mês final do pagamento extra ? "))
pagamento_extra = int(input("Qual o valor do pagamento extra mensal ? "))

while principal > 0:
    numero_meses_pagamento += 1
    if numero_meses_pagamento >= mes_ini_pag_extra and numero_meses_pagamento < mes_final_pag_extra:
        principal = principal * (1 + rate/12) - payment - pagamento_extra
        total_paid = total_paid + payment + pagamento_extra
    else:
        principal = principal * (1 + rate/12) - payment 
        total_paid = total_paid + payment
    print(f"{numero_meses_pagamento:10d} {total_paid:10.2f} {principal:10.2f}")

print(f"Total pago: {total_paid:10.2f}")
print(f"Total de meses: {numero_meses_pagamento:2d}")