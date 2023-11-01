# Lista de Exercicios de Strings em Python

#1 - Dada a string s = "PythonProgramming", extraia a palavra "Python".

nome = "PythonProgramming"
print(nome[0:6])

#2 - Dada a string s = "PythonProgramming", inverta a string usando slicing.

nome = "PythonProgramming"
print(nome[::-1])

#3 - Dada a string s = "ABCDE", escreva um programa que imprima todos os caracteres em posições ímpares.

nome = "ABCDE"
print(nome[1::2])

#4 - Dada a string s = "abcdefgh", use slicing para obter a sub-string "cdef".

nome = "abcdefgh"
print(nome[2:6])

#5 - Escreva um programa que aceite uma string do usuário e imprima os primeiros 3 caracteres e os últimos 3 caracteres da string, concatenados juntos.

nome = (input("Digite uma string: "))
resultado = nome[:3] + nome[-3:]
print(resultado)

#6 - Dada a string texto = "Python é uma linguagem, Python é popular, Python é versátil.", substitua todas as ocorrências de "Python" por "Java".

texto = "Python é uma linguagem, Python é popular, Python é versátil."
texto_modificado = nome.replace("Python", "Java")
print(texto_modificado)

#7 - Receba uma string do usuário que pode conter várias ocorrências da palavra "errado". Corrija todas elas para "correto".

nome = (input("Digite uma frase com a palavra errado: "))
nome1 = nome.replace("errado","correto")
print(nome1)

#8 - Dada a string url = "https://www.exemplo.com.br", substitua "https" por "http" e "www." por "api.".

url = "url = https://www.exemplo.com.br"
url_personalizada = nome.replace("https","htpp").replace("www","api")
print(url_personalizada)

#9 - Transforme uma data no formato DD/MM/AAAA para AAAA-MM-DD. Por exemplo, "03/10/2023" deve se tornar "2023-10-03".

data = "05/11/2003"
data_transformada = data[6:] + "-" + data[3:5] + "-" + data[:2]
print(data_transformada)

#10 - Dada uma string que pode conter várias ocorrências de "Sr." ou "Sra.", substitua-as por "Senhor" e "Senhora", respectivamente.

texto = "Sr. Diogo é casado com a Sra. Alice"
texto_modificado = texto.replace("Sr.", "Senhor").replace("Sra.", "Senhora")
print(texto_modificado)

#11- Peça ao usuário que digite uma palavra e imprima a palavra em maiúsculas e depois em minúsculas

nome = input("Digite uma palavra: ")
print(nome.upper())
print(nome.lower())

#12 - Dada a string texto = "Python É FANTÁSTICO!", converta o texto para minúsculas e depois substitua "é" por "é realmente"

texto = "Python é FANTÁSTICO"
texto_modificado = texto.lower().replace("é", "é realmente")
print(texto_modificado)

#13 - Peça ao usuário que digite seu nome completo. Mostre o nome em maiúsculas e verifique se o nome "silva" está presente (independentemente de estar em maiúsculas ou minúsculas).

nome = input("Digite seu nome completo: ")
print(nome.upper())
contem_silva = "silva" in nome.lower()
print("Contem Silva ?", contem_silva)

#14 - Peça ao usuário que insira uma senha. A senha correta é "PythonRocks". Verifique se a senha está correta, independentemente de estar em maiúsculas ou minúsculas.

senha = input("Digite uma senha: ")
if senha.lower() == "pythonrocks":
    print("Acesso permitido!")
else:
    print("Acesso negado!")

#15 - Dada a lista de palavras palavras = ["maÇÃ", "BANAna", "Uva", "MorANGo"], crie uma nova lista onde todas as palavras estejam em minúsculas.

frutas = ["maÇÃ", "BANAna", "Uva", "MorANGo"]
frutas_min = [fruta.lower() for fruta  in frutas]
print(frutas_min)