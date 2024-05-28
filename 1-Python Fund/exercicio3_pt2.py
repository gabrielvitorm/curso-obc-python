salario = float(input("Digite o salário do seu funcionário, para calcular o aumento dele: \n"))

if salario <= 1250:
    aumento = salario * 1.15
    print(f"O salário com aumento ficou R$ {aumento} \n")

else:
    aumento = salario * 1.1
    print(f"O salário com aumento ficou R$ {aumento:.2f} \n")