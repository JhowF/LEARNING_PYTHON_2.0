
#MOSTRA MENOR E MAIOR VALOR DIGITADO DENTRO DE UMA LISTA !

# valor = []
# mai = 0
# men = 0
# for i in range (0,5):
#     valor.append(int(input(f"Digite um valor {i+1}: ")))
#     if i == 0:  #Diz que o primeiro i é o maior e o menor número pois aind não há outro número!
#         mai=men= valor [i] 
#     else:
#         if valor[i] > mai:
#             mai = valor [i]
#         if valor[i] < men:
#             men = valor[i]

# print("-="*30)
# print(f"Você digitou os valores {valor}.")

# for l,v in enumerate(valor):

#     if v == mai: #Para mostrar a posição do maior número !
        
#         print(f"{l+1}", end=" ")
        
#     elif v == men:#Para mostrar a posição do menor número !
#         print(f"{l+1}", end=" ")
        
# print()        
# print (f"{men} e {mai}")


 
 
 #----------------------------- -------------------------- ------------------------------ -------------------------- 
 

#ADICIONA OS VALORES DIGITADO A LISTA É OS COLOCA EM ORDEM

# lista = []
# maior  = 0
# while True:
#     lista.append(int(input("Digite um valor: ")))
#     print("Valor adicionado com sucesso!")
#     cont = input("Deseja continuar? [S/N]").upper().strip()
#     if cont [0] == "N":
#         break
    
# lista.sort()
# lista_nova = set(lista)

# print("-"*30)
    
# print(f"Você digitou os valores {lista_nova} e o maior valor da lista é {max(lista_nova)}")           







 #----------------------------- -------------------------- ------------------------------ -------------------------- 
 

#ADICIONA OS VALORES DA LISTA EM ORDEM CORRETA DE MANEIRA LOGICA SEM USAR O COMANDO "SORT ()"

# lista = []

# for c in range(0,5):
#     n = input(f"Digite um valor {c+1} : ") #Sé eu colocar o .append aqui o número irá sempre para o final.
            
#     if c == 0 or n > lista[-1]: #Se ele for o primeiro comando ou se o valor de n for maior que o último número da lista
#         lista.append(n)
#         print(f"Adicionado ao final da lista...")
#     else:
#         pos = 0
#         while pos < len(lista): #Ele vai da posição 0 até a ultima posição!
            
#             if n <= lista[pos]: #Várificar se cada valor é maior ou igual ao valor da lista
#                 #na posição [pos] que quer dizer que vair ir em todas as posições.
            
#                 lista.insert(pos, n) #Insira o número na posição em que o pos está
#                 print(f"Adicionado na posição {pos} da lista.")
#                 break
#             pos +=1

# print("-"*30)

# print(f"Os valores digitados em ordem foram {lista}")
            
            
            
 #----------------------------- -------------------------- ------------------------------ -------------------------- 
 
 
 #VERIFICA A QUANTIDADE DE NÚMEROS NUMA LISTA E SE UM VALOR EM ESPECIFICO 
 # ESTA DENTRO ALÉM DE COLOCAR EM ORDEM DECRESCENTE
 
# lista = []
# while True:
#     try:
#         valor = int(input("Digite um valor : "))       
#         lista.append(valor)
#     except:
#         print("Por favor digite um valor valido que não envolva letras")
#     else:
#         conti = input("Quer continuar [S/N : ").upper()
#         if conti == "N":
#             break
        
# print(f"Você digitou {len(lista)} elementos")
# lista.sort(reverse=True)
# print(f"Os valor em ordém decrecente são {lista}")

# if 5 in lista:
#     print("O valor 5 foi encontrado na lista.")
# else:
#     print("O valor 5 não foi encontrado na lista.")
        

            


#----------------------------- -------------------------- ------------------------------ --------------------------

#DIVIDINDO VALORES EM VARIAS LISTAS




    
    