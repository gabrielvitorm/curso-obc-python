'''
Exercício 1
*Antecessor e Sucessor de um número:
-> Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
'''
print("###Resolução da primeira parte do exercício###\n")
print("Antecessor e sucessor de um número\n")
print("================================================")

'''
# Alternativa 1
num1 = int(input("Digite o número que você quer descobrir o antecessor e o sucessor:"))

num2 = num1 + 1
num3 = num1 - 1

print(f"O sucessor do número {num1} é o número {num2} e o antecessor é o número {num3}")
'''
# Alternativa 2

number = int(input("Digite o número que você quer descobrir o antecessor e o sucessor:"))

print(f"O atencesssor de {number} é igual a {number - 1} e o sucessor de {number} é igual a {number + 1}")

'''
*Média de 4 notas:
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

print("###Resolução da segunda parte do exercício###\n")
print("Média de 4 notas\n")
print("================================================")

print("Digite as suas notas abaixo para o calculo da média das notas:")

nota1 = float(input("Nota 1: \n"))
nota2 = float(input("Nota 2: \n"))
nota3 = float(input("Nota 3: \n"))
nota4 = float(input("Nota 4: \n"))

average = (nota1 + nota2 + nota3 + nota4)/4

print(f"\n A média das 4 notas é igual a {average}\n")