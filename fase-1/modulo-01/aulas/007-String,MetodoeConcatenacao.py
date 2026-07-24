# Strings
"""
1-  método title()
2-  método upper() / lower()
3- Concatenação de strings. (+)
4- White space em strings: \n(-> faz uma quebra de linha)  e \t (-> faz uma tabulação)
5- Removendo espaços em Python: rstrip(), lstrip() e strip()
6- Quando usar as aspas simples e aspas duplas.
"""

nome = 'daniel nazario'
print(nome.title())
print(nome.upper())
print(nome.lower())

primeiroNome = 'daniel'
segundoNome = 'nazario'
nomeCompleto = primeiroNome +' '+ segundoNome
print('Olá ' +nomeCompleto+ '!')

print('nome: \nfelipe')
print('Linguagem de programação: \tPython\tJava\tJavascript')
nome = ' daniel '
obs = '1'
# metodo rstrip() (-> apaga os campos em branco do lado direito)
print(nome.strip() + obs)
print(obs + nome.strip())
# metodo lstrip() (-> apaga os campos em branco do lado esquerdo)
print(nome.lstrip() + obs)
print(obs + nome.lstrip() + obs)
# metodo stripe() (-> apaga todos os campos em branco.)
print(nome.strip() + obs)
print(obs + nome.strip() + obs)


frase = "Eu vou para John's bar"
frase1 = 'Maria disse: "passei na prova!"'
print(frase)
print(frase1)
