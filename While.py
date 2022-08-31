# import time
# print('Olá senhor poderia me confirmar seus dados: ')

# print('Usuario : ')
# U=input()
# while U != 'Jhow': #Enquanto U for != de Jhow ele continuara repetindo o codigo.'
#     print('Usuario não encontrado na nossa base de dados :')
#     print('Usuario :')
#     U=input()


# time.sleep(1)

# while True:
#     print('Senha :')
#     S=input()
#     #if S != '3455tuco':
#      #   print('Desculpe essa senha não se encontra registrada em nosso banco de dados')
#     if S =='3455tuco': #'Somente quando a senha for == 3455tuco que ele irá ativar a função break'
#         break

# time.sleep(1)


# while True:
#     print('Poderia agora me confirma sua idade: ')
#     Idade = input()
#     if Idade != '21/02/2001': #enquanto o if for != de "21/02/2001
#         # ele vai continuar repetindo o codigo, quando for == ele prossegir a vida.'
#         continue
#     break
# print('''Seja bem vindo senho Jonathan Rodrigo
     
# lhe desejo um excelente dia''')



                     #GUANABARA

# c = 1
# while c < 10:  #>  USANDO A FUNÇÃO FOR COM WHILE
#     print(c)
#     c +=1
     

# n = 1   
# while n != 0:
#     n = int(input("Digite um valor : "))

# r= "S"    
# n = 1   
# while r == "S":
#     n = int(input("Digite um valor : "))
#     r = str(input("Quer continuar? [S/N]")).upper()


# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input("Digite um valor: "))
#     if n %2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f"Você digitou {impar}números impares e {par} números par")
    
    

# while True:
#     dados = input("informe seu sexo : ").upper().strip()
#     if dados == "M" or dados == "F":
#         break
#     else:
#         continue
# print(f"Sexo {dados.upper()} registrado com sucesso")



#SEXO MASCULINO OU FEMININO

#1º MANEIRA    
# dado = input("informe seu sexo [M/F]: ").strip().upper() [0] vai constar somente a primeira letra
# while dado != "M" and dado != "F":
#     print("Dados inválidos; Por favor,", end= " ")
#     dado = input("Informe seu sexo: ").strip().upper() [0]
# print(f"Sexo {dado} registrado com sucesso!")

#2º MANEIRA
# sexo = input("informe seu sexo [M/F]: ").strip().upper() [0]
# while sexo not in "MmFf":
#     sexo = str(input("Dados invalidos, por favor informe seu sexo: ")).strip().upper() [0]
# print(f"Sexo {sexo} registrado com sucesso.")


#JOGO DE ADIVINHA 2.0
 
# from random import randint
# print("""\033[1;97mI'm your computer.... 
# I just thought of a number between 0 and 10, Do you know what numbers it is:\033[m.""")
# n = randint(0,10)
# resp = int(input("\033[1mCan you guess which one it was ? \nWhat's your guess :\033[m "))
# count = 0
# while n != resp:
#     if resp > n:
#         print("Less... Try again") 
#         resp = int(input("number : "))
#     elif resp < n:
#         print("More... Try again")
#         resp = int(input("number : "))
#     count += 1

# print(f"You got it right with {count+1} tries")



# #MENU DE OPÇÕES

# from time import sleep
# first = int(input("Firts value: "))
# second = int(input("Second value: "))
# op=0
# while op != 5:
#     print("-=="*30)
#     print(f"Valores {first} e {second}")
#     print("""
#         [ 1 ] Sum
#         [ 2 ] multiply
#         [ 3 ] Bigger 
#         [ 4 ] New value
#         [ 5 ] Exit progaming
#         """)
#     op = int(input("\033[1;97m]>>>> Qual é sua opção :\033[m"))
    

#     if op == 1:
#      print ("The sum of the two values is", first+second)
#     elif op == 2:
#         print("The multiply of the two values is", first*second)
#     elif op == 3:
#         if first > second:
#             print(first)
#         else:
#             print(second)
#     elif op == 4:
#         first = int(input("Firts value: "))
#         second = int(input("Second value: "))
#     elif op != 5:
#         print("Invalid option, try again!")
#     sleep(2)
               
# print("Programa finalizado com sucesso!")
    


#FATORAIAL DE UM NÚMERO

# import math
# num = int(input("Enter a number to find its factorial : "))
# f = math.factorial(num) 
# print(f)


# num = int(input("Enter a number to find its factorial : "))
# c = num
# f = 1
# print("Calculando {num}")
# while c > 0:
#     print(f"{c}", end="")
#     print(" X " if c > 1 else " = ", end= "")
#     f *= c
#     c -= 1
# print(f)
    

# num = int(input("Enter a number to find its factorial : "))
# c = num
# f = 1
# print("Calculando {num}")
# for n in range (1, c):
#     print(f"{c}", end="")
#     print(" X " if c > 1 else " = ", end= "")
#     f *= c
#     c -= 1
# print(f)




#GERADOR DE PA VAI DE "PRIMEIRO" PULANDO "SEGUNDO NÚMEROS" MOSTRANDO 10 RESULTADOS

# print("\033[1;97mGerador de PA\033[m")
# print("-="*20)
# primeiro = int(input("Primeiro termo: "))
# segundo = int(input("Razão da PA: "))
# termo = primeiro
# cont = 1
# while cont <= 10:
#     print( "->",termo, end=" ")
#     termo += segundo
#     cont += 1
    
# print("\033[1;97mGerador de PA\033[m")
# print("-="*20)
# primeiro = int(input("Primeiro termo: "))
# segundo = int(input("Razão da PA: "))
# termo = primeiro
# cont = 1
# total = 0
# mais = 10

# while mais != 0:
#     total = total + mais
#     while cont <= total:
#         print( "->",termo, end=" ")
#         termo += segundo 
#         cont += 1
#     print ("Pausa")
#     mais = int(input("Quantos termos você quer mostrar a mais? "))




    
    





    

    
