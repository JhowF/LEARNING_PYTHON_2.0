#LISTAS ULTILIZAM [] E TUPLAS ()
# #LISTAS SÃO MULTÁVEIS

# lista = []

# lista.append("Tuco")

# print(lista)

# lista.append("Frezaa")
# lista.append("Goku")
# lista [2] = "Ovo"

# print(lista)

# lista.insert(0, "Alterado/incluso")  #primiero indico a posição na lista  é depois o que inserir na lista

# print(lista)

# del lista [-1] #Usei para excluir o último número!
# lista.pop(0) #usei para excluir o primeiro número!   caso eu indique uma posição ele vai excluir o ultimo.!

# if "Tuco" in lista:
#     lista.remove("Tuco") #Uso para excluir um elemento pelo seu nome é não posição!
# print(lista)



# valores = [8, 2, 5, 6,  7, 0, 1, 2, 3, 6, 8,]
# valores.sort() #Vai organizar os números em ordem númerica.
# print(valores [0:7])


# nomes = ["j", "b", "a", "t", "c", "a", "z", "x", "g"]
# nomes.sort() #Tembém organiza letras!
# print(nomes )


# valores = [8, 2, 5, 6,  7, 0, 1, 2, 3, 6, 8,]
# valores.sort(reverse=True) #Vai organizar os números só que na ordem reversa!
# print(valores [0:7])



# valores = []
# for cont in range(0,5) :
#     valores.append(int(input("Digite um valor: ")))
    
    
#     #A função enumerate() retorna uma tupla de dois elementos a cada iteração:
#     # um número sequencial e um item da sequência correspondente.
    
# for c, v in enumerate(valores) : #Diz na posição "c" encontri o valor "v" 
#     print(c, v)
    
    
# ver = valores [:] #caso eu não use [:] não estarei criando uma copia da lista em sí
# #, vou está apenas ligando os valores da lista a os valores de ver e se eu alterar algo em ver também será alterado em lista!






#                                   LISTA 2 
# dados = ["pedro", 25]
# pessoas = []
# pessoas.append(dados[:])
# print(pessoas [0])


# lista = [["jonathan", 21], ["Paloma", 18], ["Bruna", 27]]
# # print (lista [2])
# # print (lista [2][0])

# for p in lista:
#     print(f"{p[0]} tem {p[1]} anos de idade")




menor = maior = 0
galera = list()
dado = list()

for c in range (0,3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera.append(dado [:])
    dado.clear()

for p in galera:
    if p[1] >=21:
        print(f"{p[0]} é maior de idade")
        maior +=1
        
    else:
        print(f"{p[0]} é menor de idade.")
        menor +=1

print(f"Temos {menor} pesssoas menores de idade é {maior} maiores de idade!")












