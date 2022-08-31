# print("What's your name?")
# answer = input().upper()
# print("Heloo, "+ answer)
# while answer != "JONATHAN":
#    print("Desculpe tente novamente")
#    print("What's your name?")
#    answer = input().upper()
#    if answer == "JONATHAN":
#        break
# print(f"bem vindo sr. {answer}")

# uco = 0 # Loop que vai repetir 3 vezes o que está dentro do print
# while uco < 1: #número dentro indica o tanto de repetições
#    print("Hello, Word")
#    uco = uco+1 #É necessário
# Paloma = 0
# while Paloma < 1: #número dentro indica o tanto de repetições
#    print ("Te amo bb S2")
#    Paloma = Paloma+1 #É necessário

# for tuco in [0, 5 ]: #imprimi a quantidade de casa dentro do couchetes sendo nesse caso 2.
#    print("Olá humano")


# for tuco in range (1, 10): #imprime do número iniciado até o numero final informado.
# print('Uzumaki naruto')
# import builtins

#for tuco in range (1, 10, 2): #O terceiro número informado indica que irei chegar até o número 10 pulando NESSE CASO de 2 em 2 casas.
 #n = print(tuco, "Uzumaki naruto")

# import builtins

# from PIL import Image, ImageFilter #Programa usado para abrir imagens
# im = Image.open(r"C:\Users\jonat\Pictures\147-1470576_one-piece-wallpaper-4k.jpg") # É extremamente necessario informar o lacol onde está a imagem com exatidão
# im.show()
# af = im.filter(ImageFilter.BoxBlur(10))
# af.save("Onepiecenew.jpg")
# iv = Image.open(r"Onepiecenew.jpg")
# iv.show()

#word = set ([1, 2, 3, 4, 3, 5, 6, 6, 6, 2, 8]); Vai imprimir somente os número sem repetição de números iguais
#ou {1, 2, 3, 4, 3, 5, 6, 6, 6, 2, 8} da o mesmo resultado que o acima porém mais simples de ser feito
#print(word)




#import docx2txt
#Doc = docx2txt.process("dictionary.docx")  -  Usado para abrir documento WORD
#print(Doc.split())


#s = input("Do you agree? ").upper()
     #Posso colocar o .upper() no final da input ou ao na variavel dentro da função if
#if s.upper() in ["Y", "YES"]: #Isso basicamente e fazer uma lista dentro da função IF "muito util"
#    print("Agreed.")
#elif s in ["N", "NO", "NOP"]:
#    print("Not agreed.")

#def main ():
#    for m in range(3):
#        meow()

#def meow():
#    print("meow")
#main()

#for i in range (4):
    #print("?", end="") - uma maneira de fazer ????? alinhados N final do end posso colocar uma str para aparecer no final de cada frase

#print("?"*5) - Outra maneira de fazer a função acima

#for i in range(5): #quantidade de linhas
#    for j in range(3): #quantidade de # em cada linha
#        print("#", end="")
#    print()




#def main (): #graçãs a essa função posso execultar o print(u()) uma linha antes da sua criação

#    print(u())

#def u ():  #Toda vez que fizer print(u()) ele vai execultar todos os programas abaixos contidos dentro da função def u ():
#    while True:
#        h = input("Diga me qual o seu problema? ")
#        if h.upper() == "NÃO SEI":
#            print("okay vamos tentar de novo")
#            continue
#        break
#    print("Bom não pense muito sobre isso!")
#main()


#i = 1
#while True:
    #print(i)
    #i *= 2 #irá multiplicar pelo valor informado
#    i +=  1 #Não o porque mas isso faz com que os números gerados sejam uma sequencia e não o numero 1 repitidas vezes.

#scores = [72, 73, 33]
#print("Avarage: ", (sum(scores) / len(scores)))
#print(f"Avarage: {(sum(scores) / len(scores))}") = Outra maneira de somar str com int ou float
#print("Avarage: "+ str(sum(scores) / len(scores)))  = Outra maneira de somar str com int ou float
#sum = Soma os valor
#len = Mostra a quantidade de itens dentro de uma lista

#scores = [] Valores a serem preenchidos conforme abaixo
#for i in range (2):
    #scores.append(int(input("Score: "))) # irá pergunta o score na quantidade de vezes dentro do range ()
#avarege = sum(scores) / len(scores)
#print(avarege,  end="") end="" serve para dizer que não começar a frase seguinte na linha de baixo.
#print(" Se ei coloco o end do jeito acima essa frase aparece ao seu lado não na linha de baixo")

#import sys
#if P[0] == 'J':
#numbers = [4,6,8,77,2,5,9]
#if 7 in numbers :
 #   print ("found")
#else:
    #print("not found")

#people = {       #mostra o número do nome abaixo digitado, basicamente é uma agenda
#    "Paloma": "+55-8336-2061",
#    "Jonathan": "+55-8432-2801",
#    "paloma": "+55-8727-4828"
#}
#name = str(input("name: ")) #solicita o nome
#if name in people: #diz 'se o nome estiver na lista people'
#    print(f"Number: {people[name]}") #diz " se o nome estiver na lista mostre o numero de acordo com o numero solicitado'


#import csv    #Quando execulto ese programa os dados digitados vão para uma planilha no excel l.csv a qual coloquei o nome nele
#file = open("l.csv", "a") #abre a planilha no excel
#with file = open("l.csv", "a") = Caso use dessa maneira não a necessidade de usar o acima e nem de usar o file.close pois ele fechará o aruivo automaticamente.
#name = str(input("Name: ")) #pergunta o nome
#number = str(input("Number: ")) #pergunta o numero
#writer = csv.writer(file) #escrever no arquivo
#writer.writerow([name, number]) #colocar o digitado em nome e numero no arquivo
#file.close() # fecha o arquivo

# import pyttsx3 #Diz o que esta escrito na frase engine.say

# engine = pyttsx3.init()
# name = input("Qual seu nome ? ") #apenas uma imput anexada ao engine.say
# engine.say(f" {name}, Olha como fala com o meu mestre jonathan lindo e gostoso ") # o que sera dito
# engine.runAndWait() # para exceultar o codigo









