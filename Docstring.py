# def contador (i,f,p):
#     """               #uso o comando ded 3 """""" duplas para colocar um documento de ajuda no parametro contador.
#     -> Faz contagem e mostra na tela.
#     :para i: Inicio da contagem 
#     :para f: Fim da contagem                        
#     :para p: passo da contagem 
#     Criado Jhow o brabo!
#     """
    
#     # for n in range(i,f,p):
#     #     print(n)
#     c = i
#     while c<= f:
#         print(f"{c}", end="..")   #Apenas outra maneira de fazer a função cima!
#         if p > 0:
#             c+=p    
#         else:
#             c+=1
#     print("fim")
    
    
# contador (1,10,0)

# # print(contador.__doc__)
# help(contador)




def mult(a, b=1, c=1): #Coloca um b=1 indica que caso nenhum valor seja atribuido a 
    #b ele terá o valor 1"posso colocar qualquer outro valor até mesmo 0, posso atribuir um =1 no a também a=1 caso deseje.
    s = a*b*c
    print(f"A multiplicação desses números vale {s}")
        
mult(3,3,3)
mult(2,75)





# def mult(a, b=1, c=1): 
#     s = a*b*c
#     return s  #Retorna os resultados para dentro do mult o qual pode ser armazenado dentro de uma variavel como feito abaixo.
    
    
# r1 = mult(3,3,3) #É necessario usar o return para armezar o resultado dentro de uma variável.
# r2 = mult(2,75)
# print(f"As multiplicações valem {r1} e {r2}")