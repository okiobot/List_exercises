from Numeric_list import *

i = 1
tamanho = 0
def linha():
    print("="*90)

#Menu 
def menu():
    print('''
[1] - Mostra a lista inteira  
[2] - Adiciona mais um elemento 
[3] - Remove um elemento
[4] - Organizar alfabeticamente
[5] - Contar a quantidade de palavras 
[6] - Limpa a lista
[7] - Conta a quantidade de vezes que uma palavra aparece e sua posição (se tiver aparecido apenas uma vez)
[8] - Verifica a maior palavra
[9] - Verifica a menor palavra
[10] - Escolhe uma palavra aleatória
[11] - Imprime a lista e finaliza o código
''')
    linha()          

palavras = []
linha()
print("Digite '0' para parar de digitar palavras")
print("Se você deseja criar uma lista com números, digite '1': ")

#Código onde o usuário irá digitar as palavras
for t in range(999):
    digitado = input("Digite uma palavra: ")
    if digitado == "0":
        break  
    if digitado == "10":
        ListaN = input("Se você deseja utilizar uma lista numérica, digite '-1': ")
        if ListaN == "-1":
            #Se o usuário desejar, o código irá se adaptar para o código no outro arquivo, a lista numérica
            Lista_numerica()        
        else:
            pass
    if not digitado == "":
        palavras.append(digitado)
    else:    
        #Se o usuário não digitar nenhuma palavra, o código irá perguntá-lo se deseja digita-lo novamente
        f = input("Nenhuma palavra digitada, deseja inserir novamente? S/N: ")
        SN = f.upper()
        if SN == "N":
            break       
    
while True:
    linha()
            
    menu()

    #O usuário irá escolher as opções da lista  
    opcao = input("Escolha uma das seguintes opções: ")
    linha()   

    if opcao == "M":
        menu()

    #Mostra a lista completa
    if opcao == "1":
        print("A lista de palavras completa é esta: " + str(palavras))
    
    #Adiciona um elemento a lista
    if opcao == "2":
        adicionar = input("Digite a palavra a ser adicionada: ")
        palavras.append(adicionar)
        print(palavras)

    #Remove um elemento da lista
    if opcao == "3":
        print(palavras)
        d = input("Digite a palavra que deseja remover: ")
        if d not in palavras:
            #Se o usuário digitar uma palavra que não está na lista, o sistema irá perguntar se ele quer tentar novamente
            mistake = input("A palavra não está na lista, deseja tentar novamente? S/N: ")
            erro = mistake.upper()
            linha()
            if erro == "N":
                continue
            else:
                remover = input("Digite a palavra que deseja remover: ")
                if remover in palavras:
                    #Se o usuário digitar novamente uma palavra que não está na lista, o sistema ira enviá-lo de volta ao menu
                    palavras.remove(remover)
                    print("A nova lista: "+palavras)
                else:
                    print("Duas tentativas incorretas, voltando ao menu")
                    pass
        if d in palavras:
            palavras.remove(d)
            print("A nova lista: "+str(palavras))
    
    #Ordena alfabeticamente a lista
    if opcao == "4":
        palavras.sort()
        print(palavras)
    
    #Conta a quantidade de palavras na lista
    if opcao == "5":
        quantidade = len(palavras)
        print("Há "+str(quantidade)+" palavras na lista")
    
    #Limpa a lista
    if opcao == "6":
        apagar = input("Este comando irá apagar completamente a lista, deseja continuar? S/N: ")
        limpar = apagar.upper()
        if limpar == "S":
            palavras.clear()
        else:
            pass
    
    #Procura uma palavra específica na lista
    if opcao == "7":
        procura = input("Digite a palavra que você deseja procurar na lista: ")
        escolhida = palavras.count(procura)
        if escolhida == 1:
             #Se a palavra escolhida aparecer apenas uma vez, o código irá dizer que ele aparece uma vez e aponta o index dele
             print("A palavra aparece " +str(escolhida)+" vez e está na posição "+str(palavras.index(procura)))    
        else:
            #Se a palavra aparecer mais de uma vez ela irá mostrar quantas vezes ela se repete
            print("A palavra aparece " +str(escolhida)+" vez(es)")   
        
    #Verifica a maior palavra    
    if opcao == "8":
        maior = max(palavras, key=len)
        print("A maior palavra é: "+maior)
        
    #Verifica a menor palavra    
    if opcao == "9":
        menor = min(palavras, key=len)
        print("A menor palavra é: "+menor)
    
    #Escolhe uma palavra aleatório    
    if opcao == "10":
        aleatorio = random.choice(palavras)
        print("A palavra aleatória escolhida foi: "+str(aleatorio))

    #Quebra a código
    if opcao == "11":
        print(palavras)
        break
    