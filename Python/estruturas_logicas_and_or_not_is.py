"""
Estruturas Lógicas: and (e), or (ou), not (não), is(é)

Operadores unários:
    - not,
Operadores binários:
    - and, or, is

Para o "and", ambos os valor sprecisam ser True
Para o "or", um ou outro valor precisa ser True
Para o "not", o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True

if ativo or logado:
    print(" Bem vindo Usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

    if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")
else:
    print("Bem vindo usuário.")
"""
ativo = True
logado = False

if ativo:
    print("Bem vindo usuário.")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")

# o ativo é falso?
print(ativo is False)