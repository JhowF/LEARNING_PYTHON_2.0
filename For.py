# DIGITA 6 NUMEROS E SOMA SOMENTE OS NÚMEROS PARES
# m = 0
# count = 0

# for i in range(1, 7):

#     n1 = int(input(f"Digite 6 valores {i}/6  : "))

#     if n1 % 2 == 0:

#         m = m + n1 #Posso simplificar para  m+=n1
#         count = count + 1#Posso simplificar por count += 1
# print(f"Você escreveu {count} números pares e a soma desses números deu {m}", end=" ")1


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# TABUADA  COM O FOR
#m = 0
#n = int(input("Digite um número para saber sua taboada : "))
# for l in range (1,10):
# print(f"{n} X {l} = {n*l}")   #=",n * l)  #USAR O :2 QUE ESTA NO SEGUNDO {} PARA CORRIGIR ERRO DE ALINHAÇÃO É UMA BOA

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# MOSTRA 10 TERMOS DE UM PROGRAMA
# print("="*35)
# print("\033[1;34m10\033[m \033[1mTERMOS DE UMA PA\033[m")
# print("="*35)


# a= int(input("Primeiro termo: "))
# b = int(input("Razão: "))
# c = a + (10-1) * b #MANEIRA MAIS SIMPLES DE FAZER O CODIGÓ ABAIXO
# # c = int(b * 11)
# # if a < 1:
# #     c=int(b*10)
# for i in range (a,c,b ):
#     print(i,end= " ")
# print("Finish")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# CALCULA NÚMERO PRIMOS

#n = int(input("Digite um número: "))
#count = 0
#for i in range(1,n+1):
#    if n % i == 0:
#      print("\033[34m", end=" ") #VAI MUDAR AS CORES DO NÚMEROS DIVISIVEIS
#      count=count+1     
#    else:
#      print("\033[m", end=" ") #NÚMEROS QUE NÃO FOREM DIVISIVEIS ESTRÃO EM CORES NORMAIS
#    print(i, end=" ")  
#if count == 2:
#  print(f"\n\033[mO numero {n} foi divisível {count} vezes e por isso ele é um número Primo.")
#else:
#  print(f"\n\033[mO número {n} foi divisível {count} vezes. ")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# detector de palpindromo 

# frase= input("Digite uma frase: ").strip().upper()#escreve a frase desconsiderando os espaços antes e colocando em maiuscula
# palavras = frase.split()#split the phrase
# junto = "".join(palavras)#joint te phrase that before was splited
# inverso = junto[::-1]#peguei do inicio até o fim so que de trás pra frente.
# if inverso == junto:
#     print("Essa frase é um palindromo: ")
# else:
#     print("Não é um palindromo: ")
    

#uma outra maneira bem mais dificil de fazer o que o inverso está fazendo em apenas uma linha lá em cima
# inverso
# for letra in range(len(junto) -1, -1, -1): #comçei do ultimo número até o prmeiro voltando um número EXERCICIO 53 GUANABARA DÚVIDAS VER LA
#  inverso = inverso+junto[letra] #OU   inverso += junto[letra] #i join everything to make the phrase work 
# print(junto, inverso)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#ANALISA DATAS DE NASCIMENTO E DIZ QUEM É MAIOR DE IDADE

# from datetime import date
# data = date.today().year
# maior=0
# menor=0
# for pess in range(1,4):
#     nasc = int(input(f"Em que ano a {pess}º pessoa nasceu? "))
#     idade = data-nasc
#     if idade >= 18:
#         maior += 1
#     else:
#         menor += 1

# print(f"Ao todo tivermos {maior} maiores de idade\n e {menor} pessoa menor de idade")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# MAIOR E MENOR SEQUENCIA  DE PESO

# maior = 0
# menor = 0

# for p in range(1,6)  :
#     peso=float(input(f"Peso da {p}º pessoa: "))
#     if p ==1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f"O maior peso foi {maior} e o menor foi {menor}")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#PROGRAMA QUE LER O NOME, IDADE E SEXO DE 4 PESSOAS E NO FINAL MOSTRA:

#A MÉDIA DA IDADE 0DO GRUPO.             QUANTAS MULHERES TEM.

#QUAL O NOME DO HOMEN MAIS VELHO.       QUANTAS MULHERES TEM MENOS DE 20 ANOS. 




m = 0
countf = 0
velho = 0
nomevelho = ""
nova=0
for i in range (1,5):
    print(f"------ {i}º PESSOA ------")
    nome = input("Nome : ").strip()
    idade = int(input("Idade : "))
    sexo = input("Sexo [M/F] : ").upper()     
    m += idade
    n = m / i
    if i == 1 and sexo == "M": #OU  -- sexo in "Mm": --
        velho = idade
        nomevelho = nome 
    if sexo == "M" and idade > velho:
        velho = idade
        nomevelho = nome    
    if sexo == "F":
        countf += 1    
    if sexo == "F" and idade < 20:
        nova += 1                  
print(f"O homen mais velho tem {velho} e se chama {nomevelho}")
print(f"Existem {countf} mulheres  e {nova} tem menos de 20 anos.")
        
        
        
        
        
        
        
        
#print(n)
#print(countf)
#print(velho)
    

