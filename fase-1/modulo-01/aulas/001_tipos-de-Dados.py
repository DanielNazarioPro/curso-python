# Tipos de dados integrados no Python

# Tipo de texto (string)

texto = "Olá, mundo!"
print(type(texto))  # Saída: <class 'str'>

# Tipo Numericos (int, float, complex)
numero_inteiro = 10
numero_decimal = 3.14
numero_complexo = 2 + 3j

print(type(numero_inteiro))  # Saída: <class 'int'>
print(type(numero_decimal))  # Saída: <class 'float'>
print(type(numero_complexo))  # Saída: <class 'complex'>

# Tipo Sequência (list, tuple, range)
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
intervalo = range(5)

print(type(lista))  # Saída: <class 'list'>
print(type(tupla))  # Saída: <class 'tuple'>
print(type(intervalo))  # Saída: <class 'range'>

# Tipo Mapeamento (dict)
dicionario = {"chave1": "valor1", "chave2": "valor2"}
print(type(dicionario))  # Saída: <class 'dict'>

# Tipo Conjunto (set, frozenset)
conjunto = {1, 2, 3, 4, 5}
conjunto_imutavel = frozenset([1, 2, 3, 4, 5])
print(type(conjunto))  # Saída: <class 'set'>
print(type(conjunto_imutavel))  # Saída: <class 'frozenset'>

# Tipo Booleano (bool)
verdadeiro = True
falso = False   
print(type(verdadeiro))  # Saída: <class 'bool'>
print(type(falso))  # Saída: <class 'bool'>

# Tipo Binário (bytes, bytearray, memoryview)
bytes_objeto = b"exemplo"
bytearray_objeto = bytearray(b"exemplo")
memoryview_objeto = memoryview(bytes_objeto)

print(type(bytes_objeto))  # Saída: <class 'bytes'>
print(type(bytearray_objeto))  # Saída: <class 'bytearray'>
print(type(memoryview_objeto))  # Saída: <class 'memoryview'>

# Tipo None (NoneType)
nulo = None
print(type(nulo))  # Saída: <class 'NoneType'>