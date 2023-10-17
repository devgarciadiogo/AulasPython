#Revisão dos Exercicios de Python
#Lista de Exercícios Estrutura de Decisão

# 1 - Crie um programa que peça ao usuário para digitar um número e informe se é par ou ímpar.

def main():
  num = int(input("Digite um numero: "))

  if(num % 2 == 0):
    print(f"{num} é par.")
  else:
    print(f"{num} é ímpar.")
main()

# 2 - Crie um programa que peça ao usuário para digitar dois números e determine qual é o maior.

def main():
  n1 = int(input("Digite um número: "))
  n2 = int(input("Digite outro número: "))

  if(n1 > n2):
    print(f"{n1} é o maior número, e {n2} é o menor número")
  else:
    print(f"{n2} é o maior número, e {n1} é o menor número")
main()

# 3 - Crie um programa que pergunta ao usuário o preço de um produto e se ele tem um cupom de desconto. Considere o cupom de desconto com valor de R$ 10,00 reais.

def main():
  preco = float(input("Digite o preço do produto: "))
  cupom = input("Tem cupom de desconto? (S/N) ")

  if(cupom == "S"):
    preco -= 10
    print(f"O preço do produto com desconto é de {preco}")
  else:
    print(f"O preço do produto é de {preco}")
main()

# 4 - Crie uma calculadora que peça ao usuário para inserir dois números e uma das operações básicas (+, -, *, /) e, em seguida, execute a operação, informando para o usuário o resultado final.

def main():
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))
  operacao = input("Digite a operação (+, -, *, /): ")
  
  if(operacao == "+"):
    print(f"{n1} + {n2} = {n1 + n2}")
  elif(operacao == "-"):
    print(f"{n1} - {n2} = {n1 - n2}")
  elif(operacao == "*"):
    print(f"{n1} * {n2} = {n1 * n2}")
  elif(operacao == "/"):
    print(f"{n1} / {n2} = {n1 / n2}")
    
main()

# 5 - Crie um programa que peça ao usuário para digitar sua idade e classifique-a em "jovem", "adulto" ou "idoso". Considere (jovem <= 20, adulto > 20 e < 60, idoso >= 60)

def main():
  idade = int(input("Digite sua idade: "))

  if(idade <= 20):
    print("Você é jovem!")
  elif(idade > 20 and idade < 60):
    print("Você é adulto!")
  else:
    print("Você é idoso!")
main()

# 6 - Crie um programa que peça ao usuário para informar sua renda e sua pontuação de crédito. Com base nisso, decida se eles são elegíveis para um empréstimo. Considere que a pontuação elegível tem que ser 5 vezes o valor da renda informada.

def main():
  renda = float(input("Informe sua renda: "))
  pont_credito = float(input("Informe sua pontuação de crédito: "))

  if(pont_credito >= 5 * renda):
    print("Você pode solicitar um empréstimo!")
  else:
    print("Você não pode solicitar um empréstimo!")
main()

# 7 - Crie um jogo onde o programa gera um número aleatório e o jogador tenta adivinhar. O programa deve fornecer dicas se o palpite for alto ou baixo.

import random
def main():
  numero_aleatorio =  random.randint(1, 100)
  tentativas = 0

  print("Bem vindo ao jogo de advinhação!")
  print("Tente adivinha o número entre 1 e 100")

  while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
  
    if(palpite > numero_aleatorio):
      print("Seu palpite foi muito alto! Tente novamente.")
    elif(palpite < numero_aleatorio):
      print("Seu palpite foi muito baixo! Tente Novamente.")
    else:
      print("Parabéns! Você acertou!")
      break
main()


# 8 - Crie um jogo em que o jogador escolhe entre pedra, papel e tesoura, e o programa escolhe aleatoriamente. Determine o vencedor com base nas regras clássicas.

import random
def main():
  print("Bem vindo ao jogo de Pedra, Papel e Tesoura")
  
  opcoes = ["pedra", "papel", "tesoura"]

  print("Escolha uma opção: pedra, papel, ou tesoura")
  escolha_usuario = input("Sua escolha: ").lower()
  escolha_programa =  random.choice(opcoes)
  
  print(f"Você escolheu: {escolha_usuario}")
  print(f"O programa escolheu: {escolha_programa}")

  if escolha_usuario == escolha_programa:
    print("Empate! Ninguem venceu.")
  elif (escolha_usuario == "pedra" and escolha_programa == "tesoura") or \
       (escolha_usuario == "papel" and escolha_programa == "pedra") or \
       (escolha_usuario == "tesoura" and escolha_programa == "papel"):
    print("Você venceu! Parabéns")
  else:
    print("O programa venceu! Tente novamente.")
main()


  

