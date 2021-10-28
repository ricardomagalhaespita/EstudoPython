# # Tabela verdade do AND
# True and True  # Verdadeiro
# True and False  # Falso
# False and True  # Falso
# False and False  # Falso

# # Tabela verdade do OR
# True or True  # Verdadeiro
# True or False  # Verdadeiro
# False or True  # Verdadeiro
# False or False  # Falso

# # Tabela verdade do XOR 'OU Exclusivo'
# True != True  # Falso
# True != False  # Verdadeiro
# False != True  # Verdadeiro
# False != False  # Falso

# # Operador de Negação (unário)
# not True
# not False
# not 0
# not 1
# not not -1
# not not True

# # Cuidado!
# True & False
# False | True
# True ^ False

# AND Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 10
3 & 2

# OR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)

# Ou

saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)
