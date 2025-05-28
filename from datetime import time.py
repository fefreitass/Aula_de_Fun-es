import time

# Exercicio_1

# Horario = time.localtime()
# def saudacao(nome):
#     if Horario.tm_hour < 12:
#         return(f"Bom dia,{nome}")
#     if Horario.tm_hour > 12 and Horario.tm_hour < 18:
#         return(f"Boa tarde,{nome}")
#     if Horario.tm_hour > 18:
#         return(f"Boa noite,{nome}")
# print(saudacao("Felipe"))
        
# Exercicio_2
        
# lista = [1,2,3,4,5,6]

# def maior_elemento(lista):
#     maior = 0
    
#     if len(lista) == 0:
#             return "erro"
        
#     for i in lista:
#         if type(i) != int:
#             return  "erro"
#         if maior < i:
#             maior = i
    
#     return maior
    
    

# print(maior_elemento(lista))


# Desafio_Final

def menu():
    print('''
          [1] Calcular IMC
          [2] Verificar maior número
          [3] Sair
          ''')
    opcao  = input("")
    return opcao
    

def calcular_imc():
    print()
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("\nAbaixo do peso")
    elif imc > 18.5 and imc < 24.9:
        print("\nPeso normal")
    elif imc > 25 and imc < 29.9:
        print("\nSobrepeso")
    elif imc > 30 and imc < 34.9:
        print("\nObesidade grau 1")
    elif imc > 35 and imc < 39.9:
        print("\nObesidade grau 2")
    else:
        print("\nObesidade grau 3")
        
def verificar_maior():
    print()
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    if primeiro_valor > segundo_valor:
        print(f"O valor maior é: {primeiro_valor} e o menor é: {segundo_valor}")
    else:
        print(f"O valor maior é: {segundo_valor} e o menor é: {primeiro_valor}")
        
def sair(): 
    print()
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    print("Programa Finalizado !")
        
        
escolha = ""
while escolha != "3":
    time.sleep(1)
    escolha = menu()
    
    if escolha == "1":
        calcular_imc()
    elif escolha == "2":
        verificar_maior()
    elif escolha == "3":
        sair()
    else:
        print("Digite um valor valido: ")
