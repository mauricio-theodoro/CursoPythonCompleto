"""
Geradores

 - Geradores (Generators) são Iterators (Iteradores);

 OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

 Outras informações:
 - Generators podem ser criados com funções geradoras;
 - Funções geradoras utilizam a palavra reservada yield;
 - Generators podem ser criados com Expressões Geradoras;

 Diferença entre funções e Generator Functions (Funções Geradoras)

----------------------------------------------------------------------------------
| Funções                                 | Generator Functions                  |
----------------------------------------------------------------------------------
| Utilizam return                        | Utilizam yield                        |
----------------------------------------------------------------------------------
| Retorna uma vez                       | Podem utilizar yield mútiplas vezes    |
----------------------------------------------------------------------------------
| Quando executada, retorna um valor   | Quando executada, retorna um generator  |
----------------------------------------------------------------------------------
gen = conta_ate(5) # <- gera um generator

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


gen = conta_ate(10) # <- gera um generator

for num in gen:
    print(num)


gen = conta_ate(15)

print(next(gen),'\n') # 1

for num in gen:
    print(num)
"""

# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Um Generator Function não é um Generator. Ela gera um generator!

gen = list(conta_ate(10))

print(gen)


