# Caluladora simples
# Peça dois numeros ao usuario e mostre o resultados das 4 operações básicas.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Executando a operação
if operacao == '+':
    print(f"Resultado: {somar(num1, num2)}")
elif operacao == '-':
    print(f"Resultado: {subtrair(num1, num2)}")
elif operacao == '*':
    print(f"Resultado: {multiplicar(num1, num2)}")
elif operacao == '/':
    print(f"Resultado: {dividir(num1, num2)}")
else:
    print("Operação inválida.")
