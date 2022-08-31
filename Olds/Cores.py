#Existe varias maneiras de se colocar cor - aqui segue a mais simples
#vamos usar o codigo ANSI PARA CORES
#\033[m    #Comando usado para indicar que quero colocar uma "COR com o metodo ANSI"
#\033[stilo; text; cor de fundo;m    posso colocar em qualquer ordem
#\033[0;      33;  44m]

#Códigos para estilo
# 0=estilo nenhum -
# 1=negrito -
# 4=sublinhado
# 7=inverter as cores do fundo e da letra

#Códigos para texto
#30-black
#31-red
#32-green
#33-yellow
#34-blue
#35-purple
#36-light blue
#37-grey
#97-white


#Códigos para fundo
#40-Black
#41-red
#42-green
#43-yellow
#44-blue
#45-purple
#46-light blue
#47-grey
#107-White

print("\033[1;97;41mTeste\033[m")  #O zero é opicional no geral
print("\033[1;4;33;46mTeste\033[m") # O \033[m para dizer que quero que termine de usar a cor naquele momento.
print("\033[1;35;43mTeste\033[m")
print("\033[1;97;42mTeste\033[m")
print("\033[1;37;40mTeste\033[m")
print("\033[1;30;107mTeste\033[m")

print("\033[4;33;40mOlá mundo\033[m")
print("Meu nome é \033[4;31mJonathan\033[m")
print("\033[97mTesteando o branco\033[m")
                                          #DEPOIS DA UMA OLHADA NO MODULO COLORISE
A = 344789
B = 4543535
print(f"Os valores são \033[1;4;31m{A}\033[m e \033[4;31m{B}\033[m")
cores = {"Azul":"\033[34m", "zero":"\033[m", "red":"\033[1;31m", "light":"\033[36;4m"}
print("Os valores são {} {} {}  e {} {} {}".format(cores["Azul"], A ,cores["zero"],cores["red"] ,B,cores["zero"] ))