"""
Saindo de loops com break

funciona da mesma forma que nas linguagens C e JAVA.

utilizamos o break para sair do loops de maneira projetada'forçada'


"""
# Exemplo 1
for numero in range(1, 11):
    if numero == 8:
        break
    else:
        print(numero)
print("Saiu do loop")

#Exemplo 2
while True:
    if (comando := input("Digite 'sair' para sair: ")) == 'sair':
        break

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break