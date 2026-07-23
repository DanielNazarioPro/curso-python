# Desafio - crie um programa que:
"""
1. Pede pelo seu nome e idade
2. Exibe uma mensagem de boas-vindas com o nome e idade fornecidos
3. Conta quantas letras seu nome possui e exibe essa informação
4. Calcula quantos anos você terá daqui a 5 anos e exibe essa informação
5. Uma mensagem de despedida com o nome fornecido.
"""

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
print(f"Bem-vindo {nome} você tem {idade} idade")

quantasLetras = len(nome)

print(f"Seu nome tem {quantasLetras} de letras")

quantosAnosDaquia5Anos = idade + 5

print(f"Voce terá {quantosAnosDaquia5Anos} daqui a 5 anos")

print(f"Foi bom te ver por aqui, {nome}.")
