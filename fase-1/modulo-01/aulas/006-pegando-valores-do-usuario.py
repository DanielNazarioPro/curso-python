input("Digite um valor: ") # type: ignore # função input() é utilizada para receber informações do usuário. O valor digitado será retornado como uma string.

x = input("Digite um valor: ") # type: ignore # função input() é utilizada para receber informações do usuário. O valor digitado será retornado como uma string.

print('O valor digitado foi: ' + x) # type: ignore # exibe o valor digitado pelo usuário na tela.

numeroInteiro = int(input("Digite um número inteiro: ")) # type: ignore # função input() é utilizada para receber informações do usuário. O valor digitado será convertido para inteiro usando a função int().

numeroDecimal = float(input("Digite um número decimal: ")) # type: ignore # função input() é utilizada para receber informações do usuário. O valor digitado será convertido para float usando a função float().

Complexo = complex(input("Digite um número complexo: ")) # type: ignore # função input() é utilizada para receber informações do usuário. O valor digitado será convertido para complexo usando a função complex().

x_num = int(x) # type: ignore # converte o valor digitado pelo usuário para inteiro usando a função int().
print('O valor digitado foi: ' + str(x_num)) # type: ignore # exibe o valor digitado pelo usuário na tela, convertendo o valor para string usando a função str().