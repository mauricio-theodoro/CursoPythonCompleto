def mutiplicar(num1: float, num2: float) -> float:
    return num1 * num2

resutado: float = mutiplicar(4.2345, 4.1213).__round__(2)

print(f'O resultado é {resutado}')

print(f'O resultado é {mutiplicar(9, 3):.2f}')

print(f'{(media := 8 / 2)} é a metade de {media * 2}')

geek: str = 'Harry Potter'

print(f"geek='{geek}'")

print(f'{geek.upper()[:4:-1] = }')
