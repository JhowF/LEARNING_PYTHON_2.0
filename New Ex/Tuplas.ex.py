#ESCREVE UM NÚMERO POR EXTENSO


# while True:
#     numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco","Seis",
#                "Sete", "Oito", "Nove" ,"Dez", "Onze", "Doze", "treze" ,
#                "Quartoze", "Quinze", "Dezesseis", "Dezessete", "Dezoito",
#                "Dezenove", "Vinte")

#     numero = input("Por favor digite um número: ")
#     n = int(numero)
#     if 0 <= n <= 20 :
#        print(numeros [n])
#        break




#ANALISE DE DADOS INICIANTES

# from ntpath import join

# t1 = (int(input("Digite um número: ")),
#      int(input("Digite outro número: ")),
#      int(input("Digite um terceiro número: ")),
#      int(input("Digite um ultimo número: ")))
# # t2 = t1 [2]

# print(f"Você digitou os valor {t1}")

# print(f"O valor {t1 [2]} apareceu {t1.count(t1 [2])} vezes.")
# print(f"O valor 3 apareceu na {t1.index(3)+1}º posição. ")

# print(f"Os valores pares digitados foram ", end=" ")
# for n in t1:
#     if n % 2 == 0:
#          print(n, end=" ")




print("="*40)
print(f'{"LISTAGEM DE PREÇO":^40}') # ^ indica que os 40 espaços serão centralizados!
print("="*40)

lis = ("Lapis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Traansferidor", 4.20,
            "Compasso", 9.99,
            "Mochila",  120.32,
            "Canetas", 22.3,
            "Livro", 34.90)
for item in range(0, len(lis)):
    if item % 2 == 0: # Ele não está dividindo os valores em lis é sim a ordem deles! ex. lapis é 0 - 1.75 é 1 - borracha é 2 e assim sucessivamente!
        print(f'{lis[item]:.<25}', end="") #Indica que deve haver 25 . pro lado direito
    else:
        print(f"R${lis[item]: >7} ")      #<> nesse caso não indicam menos ou mais apenas indicam o lado que quero que o :.15 efetue os 15 . de espaços


