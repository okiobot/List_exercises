import random

def Lista_numerica(): 
    
    def linha():
        print("="*90)

    def menu():
        print('''
[0] - Mostra a lista inteira
[1] - Adiciona mais um elemento
[2] - Remove um elemento
[3] - Organizar de forma crescente
[4] - Organizar de forma decrescente
[5] - Contar a quantidade de números
[6] - Limpa a lista
[7] - Conta a quantidade de vezes que um número aparece e sua posição (se tiver aparecido apenas uma vez)
[8] - Mostra o maior valor da lista
[9] - Mostra o menor valor da lista
[10] - Soma todos os valores da lista
[11] - Calcula a média dos valores da lista
[12] - Escolhe um número aleatório da lista
[13] - Imprime a lista e finaliza o código
''')
        linha()          

    numeros = []
    linha()
    print("Digite '-1' para parar de digitar ")

    #Números que o usuário irá digitar
    for t in range(999):
        digitado = input("Digite um número: ")
        if digitado == "":
            r = input("Você não digitou nenhum número, deseja adicionar? S/N")
            erroN = r.upper()
            if erroN == "N":
                break
            else:
                continue
        num = int(digitado)
        if num == -1:
            break
        numeros.append(num)
        
    while True:
        linha()
                
        menu()

        opcao = input("Escolha uma das seguintes opções: ")
        linha()   
        
        if opcao == "M":
            menu()

        if opcao == "0":
            print("A lista de números completa é esta: " + str(numeros))
        
        #Adiciona um número à lista
        if opcao == "1":
            adicionar = int(input("Digite o número a ser adicionado: "))
            numeros.append(adicionar)
            print(numeros)
        
        #Remove um número da lista
        if opcao == "2":
            print(numeros)
            d = int(input("Digite o número que deseja remover: "))
            if d not in numeros:
                #Se o usuário digitar um número que não está na lista, o sistema deixará ele tentar novamente
                mistake = input("O número não está na lista, deseja tentar novamente? S/N: ")
                erro = mistake.upper()
                linha()
                if erro == "N":
                    continue
                else:
                    #Se o usuário digitar um número que não está na lista duas vezes, ele será redirecionado para o menu
                    remover = input("Digite o número que deseja remover: ")
                    if remover in numeros:
                        numeros.remove(remover)
                        print("A nova lista: "+numeros)
                    else:
                        print("Duas tentativas incorretas, voltando ao menu")
                        pass
            if d in numeros:
                numeros.remove(d)
                print("A nova lista: "+str(numeros))
        
        #Arruma a lista de forma crescente
        if opcao == "3":
            numeros.sort()
            print("A lista em ordem cresente: "+str(numeros))
        
        #Arruma a lista de forma decrescente
        if opcao == "4":
            numeros.sort()
            numeros.reverse()
            print("A lista em ordem decrescente: "+str(numeros))
        
        #Conta a quantidade de elementos na lista
        if opcao == "5":
            quantidade = len(numeros)
            print("Há "+str(quantidade)+" números na lista")
        
        #Limpa a lista
        if opcao == "6":
            apagar = input("Este comando irá apagar completamente a lista, deseja continuar?")
            limpar = apagar.upper()
            if limpar == "S":
                numeros.clear()
            else:
                pass
        
        #Procura um elemento especificado pelo usuário
        if opcao == "7":
            procura = int(input("Digite o número que você deseja procurar na lista: "))
            escolhida = numeros.count(procura)
            if procura not in numeros:
                print("O número não está na lista")          
            if escolhida == 1:
                print("O número aparece " +str(escolhida)+" vez e está na posição "+str(numeros.index(procura)))    
            if escolhida > 1:
                print("O número aparece " +str(escolhida)+" vezes")   
          
        #Procura o maior número  
        if opcao == "8":
            maior = max(numeros)
            print("O maior número é : " +str(maior))
        
        #Procura o menor número
        if opcao == "9":
            menor = min(numeros)
            print("O menor número é: "+str(menor))
        
        #Soma todos os elementos na lista
        if opcao == "10":
            total = sum(numeros)
            print("A soma dos números é: "+str(total))
        
        #Calcula a média dos números 
        if opcao == "11":
            media = sum(numeros)/len(numeros)
            print("A média dos números é: "+str(media))
        
        #Escolhe um número aleatório
        if opcao == "12":
            numeroR = random.choice(numeros)
            print("O número aleatório escolhido é: "+str(numeroR))
        
        #Mostra a lista e finaliza o código
        if opcao == "13":
            print(numeros)
            exit()
