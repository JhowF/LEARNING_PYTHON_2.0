#import random
#GERAR UM NUMERO ALEATORIO // SORTEIO
#while True:
#    print(f"Escola um numero aleatorio dentre os números 1 e 2: ")
#    escolha = int(input("Número : "))
#    n = random.randint(1, 2)
#    print("-=-" * 20)  # vai aparecer 20 traços desse fica até bonito
#    print(f"O número sorteado foi {n}")
#    if escolha == n:
#        break
#print("uau" * 20) #vai aparecer 20 traços desse fica até bonito
#print("Parabéns você acertou! ")



#MULTA POR EXCESSO DED VELOCIDADE
#velocidade = float(input("Qual a é a velocidade atual do carro ? "))
#multa = (velocidade-80) * 7
#if velocidade <= 80:
#    print("Tenha um bom dia dirija com segurança.")
#else:
#    print(f"Limite de 80km/h excercido você deve pagar uma multa de {multa}R$ reais.")


#MOSTRA SE UM NÚMERO É IMPA OU PAR
#numero = int(input("Digite um número : "))
#resultado = numero % 2
#if resultado == 0:
#    print(f"O número {numero} é um número Par")
#else:
#    print(f"O numero {numero} é um número Ímpar")



#CALCULA O PREÇO DE UMA VIAGEM DE ACORDO COM SUA DISTANCIA
#distancia = float(input("Qual e a distancia da sua viagem ? "))
#if distancia <= 200:
#    print(f"Você pagará R${(distancia)*0.50:.2f} por sua viagem de {distancia} KM/H ")
#elif distancia >= 201:
#    print(f"Você pagará R${(distancia)*0.45:.2f} por sua viagem de {distancia} KM/H ")

#if distancia <= 200:  APENAS OUTRA MANEIRA DE FAZER O MESMO EXCERCICIO
#    preco = distancia * 0.50
#elif distancia >= 201:
#    preco = distancia * 0.45
#print(f"Você pagará R${preco} por sua viagem de {distancia} KM/H ")



#CALCULA SE O ANO É BISSEXTO
#from datetime import  date #USADO NESSE CASO PARA IMPORTAR A DATA ATUAL PARA O PROGRAMA
#ano = int(input("Digite um ano ou digite zero para o ano atual: "))
#PARA UM ANO SER BISSEXTO ELE DEVE SER DIVISIVEL POR 4 NÃO DIVISIVEL POR 100 OU DIVISIVEL POR 400: É NECESSARIO PELO MENOS DUAS DESSAS REGRAS PARA SER CONSIDERADO
#if ano == 0:
#    ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #LEMBRANDO QUE % CALCULA O RESTO DA DIVISÃO E NÃO HA DIVISÃO!
#    print(f"O ano {ano} é BISSEXTO ")
#else:
#    print(f"O ano {ano} não é BISSEXTO ")



#CALCULA MENOR E MAIOR VALOR
#a = int(input("1º Valor: "))
#b = int(input("2º Valor: "))
#c = int(input("3º Valor: "))
#verificando quem é menor
#menor = a
#if b<a and b<c:
#    menor = b
#if c<a and c<b:
#    menor = c
#verificando quem é maior
#maior = a
#if b>a and b>c:
#    maior = b
#if c>a and c>b:
#    maior = c
#print(f"Maior número = {maior}")
#print(f"Menor número = {menor}")




