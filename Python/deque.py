"""
Módulo Collection - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

#Importando
from collections import deque

#Criando deques

deq = deque('Harry')

print(deq)

#Adicionando elementos no deque

deq.append('P')

print(deq)

deq.appendleft('M') # Adiciona no começo

print(deq)

# Remover elementos

print(deq.pop())

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)