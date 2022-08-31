
#SOMA VALORES E USA UM COMAND 999 PARA QUEBRAR E SOMAR OS VALORES EXCLUINDO O 999

# cou = count = 0
# while  True:
#     valor = int(input("Digite um valor : "))
#     if valor == 999:
#         break
#     count += valor
#     cou += 1
# print(f"A soma dos {cou} foi {count}")



#SHOW TABLES OF ANY NUMBER IN LOOP BREAKING WITH NEGATIVE NUMBER

# while True:
#     v = int(input("Quer ver a tabuada de qual valor ? "))
#     print("-"*30)
#     if v < 0:
#         break
#     for i in range (1,11):
#         print(f"{v:3}   X {i:3} = {v*i:3}")
# print("Programa encerrado com sucesso!")
    




#GAME IMPA OU PAR

# from random import randint

# count = 0
# while True:
#     print("-="*20)
#     print("vamos jogar par ou impar".upper())
#     value = int(input("Say any value : "))
#     pc = randint(1,10)
#     if value % 2 == 0:
#         value = "PAR"
#     else:
#         value = "IMPAR"
#     if pc % 2 == 0:
#         pc = "PAR"
#     else: 
#         pc = "IMPAR"
#     print(f"The computer play {pc} and you play {value}")
#     if pc == value :
#         print("'\033[1;97mYOU'RE RIGHT, more i doubt that you have the same luck again!\033[m")
#     else:
#         count += 1
#         break
#     count += 1 
# print("HAHAHA, GAME OVER FOR YOU, i hope you have better luck next time")
# print(f"You play {count} times.")





#ANÁLISE DE DADOS DO GRUPO

# dezoito=homens=mulheres=menos=0

# while True:
#     print("-"*20)
#     print("CADASTRE UMA PESSOA")
#     print('-'*20)

#     idade = int(input("Idade: "))
#     if idade >= 18:
#         dezoito +=1
#     s = " "
#     while s not in "MF":
#         s = input("Sexo [M/F]: ").upper().strip()
#     if s == "M":
#         homens += 1
#     if s == "F" and idade  < 20:
#         mulheres += 1
#     resp=" "
#     while resp not in "SN":
    
#         resp = input("Quer continuar? [S/N]").upper()
 
#     if resp == "S":
#         continue
#     elif resp == "N":
#         break

# print(f"Total de pessoas com mais de 18 anos: {dezoito}")
# print(f"Ao todo temos {homens} homens cadastrados")
# print(f"E temos {mulheres} mulheres com menos de 20 anos.")





#EXERCICIO COMPLICADISSIMO MAIS RESOLVIDO COM SPOILER


# v=vv=vvv=0
# menor = 0
# produtor = ""
# print("-"*25)
# print("   Loja super baratão".upper())
# while True:
#     pro=input("Nome do produto: ")
    
#     value = float(input("Valor do produto:"))
#     menor+=1
#     v += value
#     if value > 1000:
#         vv+=1
#     if menor == 1 or value < vvv:
#         vvv = value
#         produtor = pro
#     cont = " "
#     while cont not in "SN":
#         cont = input("quer continuar [S/N]: ").upper().strip()
#     if cont == "N":
#         break 

# print(f"toal {v}\n Mais que 1000 {vv}\n o produto {produtor}foi o mais barato {vvv}")



 
    

