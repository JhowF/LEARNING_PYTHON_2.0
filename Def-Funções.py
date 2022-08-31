def soma (a, b):
    
    print(f"a = {a:3} :  b = {b:3}")
    print("-"*20)
    print(a+b)
    print("-"*20)
    
    
soma (4,5)
soma(b=15,a=9)

# -----------------------------
def som (* num): #Esse * serve para indicar que eu não sei quantos parametros vou receber para somar!
    print(sum(num)) #"sum" é a função de soma!
   
som(1,1,1,2,2 )   
   
# -----------------------------

def dobra ( jhk):
    pos = 0
    while pos < len(jhk):
        jhk[pos]*=2
        pos+=1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)



                   #PARTE  2
                   
#QUANDO EU ABRO E FECHO PARENTESES ()  É UMA FUNÇÃO/METODO   EX.: STRIP()  

#USANDO O HELP()




