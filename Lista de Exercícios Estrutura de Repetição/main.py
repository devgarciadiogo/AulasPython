#Lista de Exercícios - Estrutura de Repetição

# 1- Escreva um programa que receba um número inteiro positivo “inicial” e um número real positivo “final”. exiba os números do “inicial” até “final” em ordem crescente. Utilize o “for”.

def main():
  inicial =  int(input("Digite o numero inicial (inteiro positivo):"))
  final =  int(input("Digite o número final (inteiro positivo): " ))

  print("Numeros em ordem crescente: ")
  for numero in range (inicial, final + 1):
    print(numero)
main()

# 2- Escreva um programa que receba um número inteiro negativo “inicial” e um número positivo real “final”. exiba os números do “inicial” até “final” em ordem decrescente. Utilize o “while”.


def main():
  inicial = int(input("Digite o numero inicial (inteiro negativo): "))
  final =  float(input("Digite o numero final (real positivo): "))

  if inicial >= 0 or final <= 0:
    print("Por favor, insira um número intei")
  else:
    print("Numeros em ordem decrescente: ")
    while inicial >= final:
      print(inicial)
      inicial -= 1
main()

# 3- Crie um programa que solicite ao usuário um número inteiro positivo e exiba a soma de todos os números inteiros de 1 até o número fornecido. Utilize o “for”


def main():
  numero = int(input("Digite um número inteiro positivo: "))
  soma = 0 

  if numero <= 0:
    print("Por favor, insira um número inteiro positivo")
  else:
    for i in range(1, numero + 1):
      soma += i
  print(f"A soma de todos os números inteiros de 1 até {numero} é: {soma}")
main()


# 4- Escreva um programa que solicite um número inteiro não negativo e calcule o fatorial. Utilize o “while”.

def main():
  numero = int(input("Digite um número inteiro não negativo: "))

  if numero < 0:
    print("Por favor, insira um número inteiro não negativo.")
  else:
    fatorial = 1
    
    i = 1
    while i <= numero:
      fatorial *= i
      i += 1
  print(f"o fatorial de {numero} é {fatorial}")
main()

# 5- Peça ao usuário para digitar uma série de números. Quando o usuário digitar "0", exiba a média dos números digitados. Utilize “for/while/enumerate/len/list

def main():
  soma =  0
  contador = 0

  while True:
    numero = float(input("Digite um número(ou 0 para calcular a média): "))

    if numero == 0:
      break

    soma += numero
    contador += 1

  if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é: {media:.2f}")
  else:
    print("Nenhum número válido foi digitado")
main()

# 6- Crie um programa que receba o peso inicial de uma pessoa e a quantidade de anos de projeção que se deseja calcular. A cada ano percorrido o usuario deve informar se houve aumento ou perca de peso. Considere as constantes GANHO_PESO igual a 2.5kg e PERCA_PESO igual a 0.5kg. Utilize “while”.

def main():
  GANHO_PESO = 2.5
  PERCA_PESO = 0.5

  peso_inicial = float(input("Digite o peso inicial (kg): "))
  anos_projecao = int(input("Digite a quantidade de anos de projeção: "))

  ano_atual = 1

  while ano_atual <= anos_projecao:
    decisao = input(f"Ano {ano_atual}: Houve aumento (A) ou perca (P) de peso?") 

    if decisao == "A":
      peso_inicial += GANHO_PESO
    elif decisao == "P":
      peso_inicial -= PERCA_PESO
    else:
      print("Entrada invalida. Por favor, digite 'A' para aumento ou 'P' para perda")
      continue
    
    print(f"Peso após o ano {ano_atual}: {peso_inicial} kg")
    ano_atual += 1

  print("Projeção concluida.")

main()

# 8- Crie um programa que receba dois números inteiros positivos, sendo o primeiro o valor base e o segundo o valor exponencial. Calcule a potenciação SEM utilizar o operador ** e SEM utilizar a função pow().

def main():
  base = int(input("Digite o valor base(inteiro positivo): "))
  expoente = int(input("Digite o valor exponencial(inteiro positivo"))

  if base < 0 or expoente < 0:
    print("Por favor, insira valores inteiros positivos para a base e o expoente")
  else:
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    print(f"{base} elevado a {expoente} é igual a {resultado}")
main
