# texto em python

print("Python")
print('Meu nome é Daniel')

print(type("Python")) # str
print(type("500")) # str
print(type(500)) # int

print(int('5')) # type: ignore # converte string para inteiro'
print(float('5.5')) # type: ignore # converte string para float'
print(str(5)) # type: ignore # converte inteiro para string'
print(str(5.5)) # type: ignore # converte float para string'

print(bool(1)) # type: ignore # converte inteiro para booleano'

print("50" + "10") # type: ignore # concatenação de strings

print(int("50") + int("10")) # type: ignore # soma de números representados por strings

print ("olá " + "   Daniel") # type: ignore # concatenação de strings

print ("python " * 3) # type: ignore # repete a string 3 vezes