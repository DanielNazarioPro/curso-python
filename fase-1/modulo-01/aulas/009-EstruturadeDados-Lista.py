# Estrutura de dados compostas - List

quadrados = [1, 4, 9, 16, 25]
print(quadrados)

# Como strings(e todos os tipos embutidos de sequencia), listas pode ser indexados e fatiados.

print(quadrados[0])
print(quadrados[-1])
print(quadrados[-3:])

# As listas tambem suportam operações como concatenação

print(quadrados + [36, 49, 64, 81, 100])

# Diferentemente de strings, que são imutáveis, listas são mutáveis, ou seja, é possível alterar elementos individuais de uma lista:

cubos = [1, 8, 27, 65, 125]  # algo errado aqui
print(4 ** 3)  # o cubo de 4 é 64, não 65!
print(cubos)
cubos[3] = 64  # substitui o valor errado
print(cubos)

# Você também pode adicionar novos itens no final da lista, usando o método list.append() (estudaremos mais a respeito dos métodos posteriormente):

cubos.append(216) # adiciona o cubo de 6
cubos.append(7 ** 3) # e o cubo de 7
print(cubos)

# A atribuição simples em Python nunca copia dados. Quando você atribui uma lista a uma variável, a variável se refere à lista existente. Quaisquer alterações que você fizer na lista por meio de uma variável serão vistas por todas as outras variáveis que se referem a ela:

rgb = ["Vermelho", "Verde", "Azul"]
print(rgb)
rgba = rgb

print(id(rgb) == id(rgba))

rgba.append("Alf")
print(rgb)
print(rgba)

rgba_correto = rgba[:]
rgba_correto[-1] = 'Alfa'
print(rgba_correto)

# Atribuição a fatias também é possível, e isso pode até alterar o tamanho da lista ou remover todos os itens dela:

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
# substitui alguns valores
letras[2:5] = ['C', 'D', 'E']
print(letras)

# agora remove-os
letras[2:5] = []
print(letras)

# limpa a lista substituindo todos os elementos por uma lista vazia

letras[:] = []
print(letras)

# É possível aninhar listas (criar listas contendo outras listas), por exemplo:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n] # type: ignore
print(x) # type: ignore
print(x[0]) # type: ignore
print(x[0][1]) # type: ignore
#              coluna x linha
# Uma matriz ['a','b','c'] <- x[0][1] coluna 0 e linha 1
#            [1, 2, 3]