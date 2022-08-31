#DICIONÁRIOS
#para indentificar um dicionário usamos {}

dados = {"nome":"Jonathan", "Idade":21}
dado = {"nome":"Paloma", "Idade":18}

# print(dados ["nome"])

dados ["sexo"]= ("Masculino")#criar u novo dado dentro do dicionario
dado ["sexo"]= ("Feminino")
# # print(dados)

# #del dados ["sexo"] #Vai excluir o elemento sexo do meu dicionario.

# # print(dados)
# for n in dados.values(): #Serve para mostrar os valores atribuidos!
#     print(f"{n:^2}",end=", ")
#     if n == "Masculino":
#         print(end="\n")
        
    
# for m in dados.keys(): #Server para mostra as atribuições do dicionario no caso aqui será, nome, idade e sexo!
#     print(f"{m:^2}",end=" ")
#     if m == "sexo":
#         print(end="\n")
        
        
# for l,v in dados.items():#Serve para mostrar o dicionario completo
#     print(f"{l:^2} : {v:^2}")
    
    
lista = [dados.values(), dado.values()]

dada = dados.values(),dado.values()
print(dada [1])

# for v, c in enumerate(lista):
#     print(f"{v} : {c}") 


# print(f"{lista [1]}\n {lista [0]}")


#Para dicionário usamos o .copy() enves do [:]