#Lista de Exercicios - Métodos Funções em Python

#1 - Crie uma função que receba três números como argumentos e retorne o maior deles.

def maior_de_tres(a,b,c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c

resultado =  maior_de_tres(5, 12, 8)
print(f"o maior número é {resultado}")

#2 - Desenvolva uma função que calcule a soma dos N primeiros números inteiros positivos.

def soma_n_primeiros_inteiros(n):
  soma = 0
  for i in range(1, n + 1):
    soma += i
  return soma
resultado =  soma_n_primeiros_inteiros(5)
print(f"A soma dos primeiros 5 números inteiros é {resultado}")

#3 - - Escreva uma função recursiva para calcular o fatorial de um número.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(f"O fatorial de 5 é {resultado}")

#4 - Crie uma função que verifique se uma palavra ou frase é um palíndromo.

def e_palindromo(texto):
  texto =  texto.lower().replace(" ", "")
  return texto ==  texto[::-1]
resultado = e_palindromo("arara")
print(f"'arara' é palindromo? {resultado}" )

#5 - Implemente uma função que determine se um número é primo ou não.

def e_primo(numero):
  if numero <= 1:
    return False
  for i in range (2, int(numero** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

resultado = e_primo(17)
print(f"17 é primo ? {resultado}")

#6 - Desenvolva uma função que calcule a soma dos dígitos de um número inteiro.

def soma_digitos(numero):
  soma = 0 
  while numero > 0:
    soma += numero % 10
    numero //= 10
  return soma
resultado = soma_digitos(12345)
print(f"A soma dos digitos de 12345 é {resultado}")

#7 - Crie uma função recursiva para gera o N-ésimo termo da sequencia de Fibonacci

def fibonacci(n):
  if n <= 1:
    return n 
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

resultado  =  fibonacci(7)
print(f"O 7º termo da sequencia de Fibonacci é {resultado}")

#8 - Escreva uma função que conte o número de vogais em uma String

def contar_vogais(texto):
  
  contagem = 0 
  for letra in texto:
    if letra.lower() in 'aeiou':
      contagem += 1
  return contagem

resultado = contar_vogais("Python é uma linguagem de programação.")
print(f"O texto possui {resultado} vogais.")

#9 - Implemente uma calculadora simples que aceite dois números e uma operação (+, -, *, /) como entrada e retorne o resultado.

def calculadora(a, b, operacao):
  if operacao == '+':
    return a + b
  elif operacao == '-':
    return a - b
  elif operacao == '*':
    return a * b
  elif operacao == '/':
    return a / b
  else:
    return "Operação invalida"

resultado =  calculadora(10,5, '+')
print(f"Resultado da operação: {resultado}")
