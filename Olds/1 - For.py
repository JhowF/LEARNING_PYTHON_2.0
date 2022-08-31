#lAÇO DE VARIAVEL DE CONTROLE - TAMBÉM CONHECIDO COM ESTRUTURA DE REPETIÇÃO "for"


#for  c in range(1,10): #ranger = intervalo em ingles \ ele conta 1 número a meno então (1,10) e na verdade (1,9)
    #print("oi") #or ´print("oi\n"*10)
    #SE EU PRINTAR c ELE VAI CONTAR DE 1 A 9


#for c in range(0, 9, 2): #O -1 SERVE PARA INDICAR QUE ELE CONTAR TIRANDO 1 UNIDADE DO PROXIMO NÚMERO
    #print(c)

#lista = [1, 2, 3, 4, 5] --  VAI DEIXAR OS NUMERPS AQUI EM ORDEM DECRESCENTE
#for l in reversed(lista) :
    #print(l)
# from time import sleep

#n = int(input("Begin "))
#f = int(input("End"))
#p = int(input("Setp"))

#for c in range (n, f+1, p): #começa no n vai até o f pulando de p em p números

#    print (c)
#m = 0 #Preciso acrescentar esse valor aqui para ele some todos os valor digitados em n
#for c in range (0,3):
#    n = int(input("Dite um valor: "))
#    m = m + n #ou m +=n


#print(m)
#print(n*5) #nesse caso esse mostra o resultando levando em conta o ultimo valor dito ao n


#FAZ CONTAGEM REGRESSIVA E QUANDO ACABA TOCA UMA MUSICA
#import pygame
#import time
#for c in range (10, -1, -1):#O SEGUNDO MENO E PARA QUE CONTE DE 10 A 0 E NÃO DE 10 A 1    // lembrando que conta sempre 1 número a meno
#    time.sleep(9)
#    print(c)
#pygame.init()
#pygame.mixer.music.load("Cold.mp3")
#pygame.mixer.music.play()
#input()
#pygame.event.wait()



#FAZ UM FOR DE TODOS OS NÚMEROS PARAS ENTRE 0 E 50

#for a in range(0,52,2): #DESSA MANEIRA E MELHOR QUE A DEBAIXO POIS EXIGE MENOS ITERAÇÕES DO PROCESSADOR
 #   print(a, end="  ")
#for a in range(1,51): #OUTRA MANEIRA DE FAZER O EXEMPLO ACIMA
    #if a % 2 == 0:
        #print(a, end="  ")






#USADO PARA SOMAR NÚMEROS ENTRE 1 A 500 SOMANDO MOSTRANDO A QUANTIDADE  NÚMEROS DENTRO DELES

m = 0 #usado para somar números

cont = 0 #vai ser usado para contar os números dentro do for

for l in range (1,501, 2): #para achar todos os números impares dentro de 1 á 500

    if l % 3 == 0: #usado para achar os multiplos de 3

       m = m + l  #usado para somar os números dentro do for numero por número

       cont = cont+1 #usado para contar a quantidade de números

print(cont) #quantidade de valor impares multiplos de 3 dentro do for

print(m,end=" ")#soma dos números impares







