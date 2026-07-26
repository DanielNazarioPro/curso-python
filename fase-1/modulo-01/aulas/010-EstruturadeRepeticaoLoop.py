# Listas (list)
# Alterando, Adicionando e Removendo Elementos.
# Método append(), Método insert(), Método pop(), Método remove()
# Organizando Listas sort(), sorted(), len() - length

"""
user_ativos = ['joao', 'antonio', 'filipe', 'igor']

for user in user_ativos:
    print(user)

for user in user_ativos:
    print(user.upper())

listadeNumero = [1, 25, 5, 80, 110, -5]

for numero in listadeNumero:
    print(numero + 2)
    print('ola mundo')
    print(numero ** 2)

user_ativos = ['joao', 'antonio', 'filipe', 'igor']

mensagem_aos_usuarios = 'Bem vindo(a) {}!\nAté mais tarde {}!\n'

for x in user_ativos:
    print(mensagem_aos_usuarios.format(x, x))

# Função range() - range(inicio, fim, passo)

for n in range(1, 10):
    print(n)

for n in range(1, 10, 2):
    print(n)

lista = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]

for n in lista[:11]:
    print(n)

num = []

for x in range(1, 101):
    num.append(x) # type: ignore

print(num) # type: ignore"""

quadrado = [valor ** 2 for valor in range(1, 21)]

print(quadrado) # type: ignore