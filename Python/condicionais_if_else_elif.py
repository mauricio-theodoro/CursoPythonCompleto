"""
Estruturas condicionais
if, else, elif
"""

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Menor de idade")
elif 17 < idade < 50:
    print("Adulto")
elif 49 < idade < 80:
    print("Senhor")
else:
    print("Idoso")