
while True:
    
    try: #Diz pra ele tentar fazer o comando abaixo   ____ um mesmo try: pode ter varios tipos de except 

        n=int(input("Numero : "))

    
    except: #Caso de erro digite o que está dentro de except:   ---- except Exception as erro: 
        #Usando dessa maneira posso printar o erro espesificando o que desejo saber sobre o mesmo.
        #Ex:
        #print(f'O problema encontrado foi {erro.__class__.__name__,')
        print("Por favor digite um número e não o escreva.")
    
    else: #Opcional "Caso der certo digite isso!"
        print(f"Você digitou o número {n}")
        break
    finally: #Vai acontecer sempre dando certo ou errado!
        print("Volte sempre")
        
        
        
while True:
    
    try: 

        n=int(input("Numero : "))    
        m =  int(input("Numero : "))
        r = n / m
    except (ValueError, TypeError): #Posso gerar um except para cada tipo de erro que pode ter no meu codigo.
        print("Tivemos um problema com os tipos de dados que você digitou.")
    except ZeroDivisionError:
        print("N]ao é possivel dividir um número por zero!")
    else:
        print(f"O resultado é {r:.2f}")
    finally:
        print("Volte sempre! Muito obrigado!")
        