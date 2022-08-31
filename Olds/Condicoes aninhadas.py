#CURSO EM PYTHON

#Condições aninhadas

#nome = str(input("Qual é seu nome? "))
#if nome == "Jonathan" or nome == "Paloma":
#    print("Que nome bonito!")
#elif nome == "Wagner" or nome == "Alexandra" or nome == "Carlos":
#    print("Nome lero lero")
#elif nome in "Ana Raquel Maria Neuci":
#    print("Belo nome feminino")
#else:
    #print("Seu nome é bem normal. ")


#emprestimo = float(input("Digite o valor do emprestimo : "))
#ano = int(input("Digite o tempo que planeja pagar : "))
#salario = float(input("Digite seu sálario : "))
#meses = ano*12
#prestacao = emprestimo/meses
#terco = salario*0.30
#if prestacao <= terco:
 #   print(f"Seu emprestimo de {emprestimo} foi concedido sua parcela será de {prestacao:.2f}.")
#elif prestacao >= terco:
  #  print(f"Seu emprestimo de {prestacao:.2f} excerde 30% de sua renda {terco} sinto muito em informa\nmas seu emprestimo não pode ser realizado")
# end=""

#numero = int(input("Digite um número: "))
#print("""Escolha uma das bases para conversão:
#[ 1 ] Converte para BINÁRIO
#[ 2 ] Converte para OCTAL
#[ 3 ] Converte para HEXADECIMAL""")
#opcao = int(input("Sua opção: "))
#while True:


 #   if opcao == 1 or  opcao ==2 or opcao == 3:
 #       break
 #      print("Escolha uma opção disponivel")
 #       opcao = int(input("Sua opção: "))
#if opcao == 1:
 #  print(f"{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}") # o [2:] esta dizendo para mostrar o resultado a parti da 3º str lembrando que o python começa na str 0

#elif opcao == 2:
 #  print(f"{numero} convertido para OCTAL é igual a {oct(numero)[2:]}")

#elif opcao == 3:
  # print(f"{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}")

#else:
 #   print("Digite um argumento valido")

#pri = int(input("Primeiro número : "))
#seg = int(input("Segundo  número : "))
#if pri < seg:
#    print("O segundo número é maior!")
#elif pri > seg:
#    print("O Primeiro número é maior!")
#elif pri == seg:
#    print("O dois números são iguais!")

#from datetime import date
#data = date.today().year
#ano= int(input("Ano de nascimento: "))
#idade = int(2022-ano)
#print(f"Quem nasceu em \033[4;34m{ano}\033[m tem \033[4;34m{idade}\033[m anos em \033[4;34m{data}\033[m.")
#if idade == 18:
#    print("Você precisa se alistar \033[4;31mIMEDIATAMENTE!\033[m")
#elif idade != 18:
#    saldo = idade - 18
#    novo = 2022 -  saldo
#    print(f"Você deveria ter se alistado em \033[4;31m{novo}\033[m e seu alistamento foi há \033[;4;31m{saldo}\033[m anos")
#else:
#    print("Digite apenas números!")

#nota1 = float(input("Primeira nota: "))
#nota2 = float(input("Segunda nota : "))
#media = float((nota1+nota2)/2)
#print(f"Sua média e de {media}")
#if media >= 5.0 and media < 6.9: #ou if 7> media >=5: \\basicamente quer dizer se a media tiver entre 7 e 5 faça isso!
 #   print("Você está de recupeção ")
#elif media >= 7.0:
 #   print("Você está aprovado! ")
#elif media <= 4.9:
 #   print("Você esta reprovado!")
#else:
    #print("Verifique os argumentos digitados!")

import math
#peso = float(input("Qual seu peso? (kg) "))
#altura = float(input("Qual sua altura? (m) "))
#al=
#imc = peso/altura ** 2
#print(f"Você tem um IMC atual de \033[4;33m{imc:.1f}\033[m :")
#print(imc)
#if imc < 18.5:
#    print ("Abaixo do peso normal")
#elif imc >=18.5 and imc <= 25:
#    print("Peso ideal")
#elif 25 >= imc <=30:
#    print("Sobrepeso")
#elif 30 >= imc <=40:
#    print("Obesidade")
#else:
#    print("Obesidade mórbida")





#JOKENPO SIMULA UM JOKENPO COM O COMPUTADOR
import time
print("""Suas opções: 
[ 1 ] \033[1;4;30;97mPEDRA\033[m
[ 2 ] \033[4;1;30;97mPAPEL\033[m
[ 3 ] \033[4;1;30;97mTESOURA\033[m""")
jogada = int(input("Qual é sua jogada ? "))
if jogada == 1:
    jogada = "Pedra"
if jogada == 2:
    jogada = "Papel"
if jogada ==3:
    jogada = "Tesoura"
print("\033[33mJO\033[m")
time.sleep(0.7)
print("\033[33mKEN\033[m")
time.sleep(1)
print("\033[33mPO!!!\033[m")
print("\033[33m-=-\033[m" * 20)
import  random
#
#i = ("Pedra", "Papel", "Tesoura") #=== tuple
n =random.randint(1,3)  #se for usar a tuple tem que ser os números do 0 ao 3 que seriam 3 casa como na tuple.
#m =(i[n])  #Maneira mais facil de implenmentar uma tuple no  random // tambem uma maneira mais facil de fazer os 3 ifs abaixo
#print(m) #ou print(i[n])


if n == 1:
    n = "Pedra"
if n == 2:
    n = "Papel"
if n ==3:
    n = "Tesoura"

##################MANEIRA MAIS FACIL DE TER FEITO ESSA PARTE


print(f"\033[34;1mVocê jogou {jogada} e o computador jogou {n}\033[m")
if n == jogada:
    print("\033[;1;33mVocês empataram\033[m")
elif jogada == "Papel" and n == "Pedra" or jogada == "Tesoura" and n == "Papel" or jogada == "Pedra" and n == "Tesoura":
    print( "\033[1;32mParabéns você ganhou!!\033[m👏😁")
elif n == "Papel" and jogada == "Pedra" or n == "Tesoura" and jogada == "Papel" or n == "Pedra" and jogada == "Tesoura":
    print("\033[1;31mSinto muito você perdeu\033[m 😢👀")

print("\033[33m-=-\033[m" * 20)










