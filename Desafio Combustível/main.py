'''Escreva um algoritmo em Python que leia o número de litros vendidos e o tipo de combustível codificado da seguinte forma:

1 - Álcool,

2 – Gasolina

3 – Gasolina Aditivada

4 - Diesel

Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90, o preço do litro do diesel é R$ 4,20 e o preço do litro da gasolina aditivada é R$ 3,97. Os cálculos finais são definidos de acordo com a tabela abaixo:

Álcool – Até 20 litros, desconto de 3% por litro.

Álcool – Acima de 20 litros, desconto de 5% por litro.

Gasolina – Até 7 litros, desconto de 4% por litro.

Gasolina – Acima de 15 litros, desconto de 6% por litro.

Diesel – Até 12 litros, desconto de 2% por litro.

Diesel – Acima de 12 litros, desconto de 0% por litro.

Gasolina Aditivada – Até 26 litros, desconto de 0,5% por litro.

Gasolina Aditivada – Acima de 38 litros, desconto de 1,7% por litro
'''
def main():
  while True:
    try:
      tipo_combustivel = int(input("Qual combustível deseja (álcool = 1 / gasolina normal = 2 / gasolina aditivada = 3 / diesel = 4)?"))

      if tipo_combustivel >= 1 and tipo_combustivel <= 4:
        litro = float(input("Quantos litros?"))

        preco = 0
        # Álcool
        if tipo_combustivel == 1:
          if litro <= 20:
            preco = (2.90 * litro) - (2.90 * litro * 0.03)
          else:
            preco = (2.90 * litro) - (2.90 * litro * 0.05)
        # Gasolina Normal
        elif tipo_combustivel == 2:
          if litro <= 7:
            preco = (3.30 * litro) - (3.30 * litro * 0.04)
          else:
            preco = (3.30 * litro) - (3.30 * litro * 0.06)
        # Gasolina Aditivada
        elif tipo_combustivel == 3:
          if litro <= 12:
            preco = (4.20 * litro) - (4.20 * litro * 0.02)
          else:
            preco = (4.20 * litro)
        # Diesel
        elif tipo_combustivel == 4:
          if litro <= 26:
            preco = (3.97 * litro) - (3.97 * litro * (0.05 / 100))
          else:
            preco = (3.97 * litro) - (3.97 * litro * (1.7 / 100))

        print(f"Total a pagar: R$ {preco:.2f}")
        break
      else:
        print("Opção inválida")
        continue
    except ValueError:
      print("Por favor, insira um valor válido.")

main()
