#Revisão dos Exercicios de Python
# 1- Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor.

def main():
  n1 = int(input("Digite um número: "))
  n2 = int(input("Digite outro número: "))

  if(n1 > n2):
      print(f"{n1} é o maior número, e {n2} é o menor número")
  else:
      print(f"{n2} é o maior número, e {n1} é o menor número")
main()


# 2 - Faça um programa que obtenha o ano de nascimento de uma pessoa e informe qual a idade dessa pessoa.

def main():
  ano_nascimento = int(input("Insira o seu ano de nascimento: "))
  ano_atual = int(input("Insira o ano atual: "))
  
  print(f"Sua idade é {ano_atual - ano_nascimento} anos")
main()


# 3 - Faça um programa que receba 3 notas, e calcule a média final de uma pessoa.

def main():
  nota1 = float(input("Insira a primeira nota: "))
  nota2 = float(input("Insira a segunda nota: "))
  nota3 = float(input("Insira a terceira nota: "))

  media = (nota1 + nota2 + nota3)/3
  print(f"O resultado da média é {media}")
main()
