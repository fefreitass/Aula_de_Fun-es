# import time

# Horario = time.localtime()
# def saudacao(nome):
#     if Horario.tm_hour < 12:
#         return(f"Bom dia,{nome}")
#     if Horario.tm_hour > 12 and Horario < 18:
#         return(f"Boa tarde,{nome}")
#     if Horario.tm_hour > 18:
#         return(f"Boa noite,{nome}")
# print(saudacao("Felipe"))
        
lista = [1,2,3,4,5,6]

def maior_elemento(lista):
    maior = 0
    
    if len(lista) == 0:
            return "erro"
        
    for i in lista:
        if type(i) != int:
            return  "erro"
        if maior < i:
            maior = i
    
    return maior
    
    

print(maior_elemento(lista))