import os
import requests
os.system('cls')

j =("s")
erro = []
recuperacao = []
deletado = []
saldot = []
valores = []
val = 0
bdd=open("logins.csv","a+")
bdd.close()

def dolar():
    try:
        entrada=(input("Digite o valor em dolar: "))
        transf=(entrada.replace(',', '.'))
        valor=float(transf)
        api=requests.get(f"https://api.exchangerate-api.com/v4/latest/BRL")
        data=api.json()
        if "rates" in data:
            if "USD" in data["rates"]:
                taxa=data["rates"]["USD"]
                valorreal= str(round(valor/taxa))
                os.system("cls")
                print(f"Para a sua segurança, salvamos o valor em real")
                print(f"USD {valor} em reais é: R${valorreal}")
                return valorreal
    except ConnectionError or TimeoutError or ConnectionRefusedError:
        print("Servidor indisponivel, adicione os valores em Real ou tente mais tarde")
        return ("servidor")
    

def euro():
    entrada=(input("Digite o valor em euro: "))
    transf=(entrada.replace(',', '.'))
    valor=float(transf)
    api=requests.get(f"https://api.exchangerate-api.com/v4/latest/BRL")
    data=api.json()
    if "rates" in data:
        if "EUR" in data["rates"]:
            taxa=data["rates"]["EUR"]
            valorreal= str(round(valor/taxa))
            os.system("cls")
            print(f"Para a sua segurança, salvamos o valor em real")
            print(f"EUR {valor} em reais é: R${valorreal}")
            return valorreal

def senha(nome):
    bdd = open("logins.csv", "r+")
    cnt = 0
    linhas = bdd.readlines()
    bdd.seek(0)
    linha = ("")
    loop=True
    for i, linha_atual in enumerate(linhas):
        cmps=linha_atual.strip().split(';')
        if nome == cmps[0]:
            while loop == True:
                senhaatt=cmps[1]
                digitado=input("Digite a senha: ")
                cnt+=1
                if digitado == senhaatt:
                    os.system("cls")
                    print("Senha correta.")
                    bdd.close()
                    return
                if cnt == 3:
                    print("Limite de tentativas atingido, reinicie o sistema para continuar.")
                    bdd.close()
                    exit()
                else:
                    print(f"Senha incorreta. Você tem mais {3 - cnt} tentativas.")
                    continue
    else:
        codigo=input("Digite uma senha para o seu perfil: ")
        linha=(nome+";"+codigo+"\n")
        bdd.writelines(linhas)  
        bdd.write(linha)

    bdd.close()


while True:
    j=="n"
    print("Bem vindo ao Sistema de rastreamento de despesas")
    operacao = input("Qual operação deseja realizar? ").lower()
    os.system("cls")

    if operacao == 'deposito':
        arq = open('Arquivo.csv', 'a')
        nome = input("Qual seu o nome completo? ").title()
        senha(nome)
        correto ="não"
        while correto == 'não':
            categoria = input("Em qual categoria deseja depositar? ").lower()
            certo=True
            while certo == True:
                brlusdeur = input("Deseja utilizar qual moeda? Opções: Euro, Dólar ou Real (Caso você esteja offline só será possível fazer em Real.) ").lower()
                if brlusdeur == "dolar":
                    valor = dolar()
                    certo = False
                elif brlusdeur == "euro":
                    valor = euro()
                    certo = False
                elif brlusdeur == "real":
                    valor = (input("Digite o valor em Real: ")).replace(",",".")
                    certo = False
                else:
                    print("Digite uma moeda válida")
            valorponto = valor.replace(',', '.')
            print('Dados à adicionar: \nNome: ' + nome + ', Categoria: ' + categoria + ', Valor: R$' + valorponto + '\n')
            correto=input("Está tudo certo? ").lower()
            if correto == ("não"):
                os.system("cls")
                print("Digite as informações corretas: ")    
            else:                
                arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                arq.close()
                print("Operação finalizada")
                j = input("Deseja finalizar o sistema? ").lower()
                os.system("cls")


    elif operacao == 'leitura':
        arq = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome completo? ").title()
        senha(nome)
        for k in arq:
            if nome in k:
                categoria = input("Em qual categoria deseja observar? ").lower()
                arq.seek(0)
                for k2 in arq:
                    if categoria in k2:
                        arq.seek(0)
                        for linha in arq:
                            if nome in linha:
                                if categoria in linha:
                                    print(linha.strip())
                if categoria == 'tudo':
                    arq.seek(0)
                    for k3 in arq:
                        if nome in k3:
                            print(k3.strip())
        arq.close()
        j = input("Deseja finalizar o sistema? ").lower()
        os.system("cls")
        

    elif operacao == 'deleção':
        arq = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome completo? ").title()
        senha(nome)
        for p in arq:
            if nome in p:
                categoria = input("Em qual categoria deseja deletar? ").lower()
                arq.seek(0)
                for p2 in arq:
                    if categoria in p2:
                        arq.seek(0)
                        valor = input("Qual valor deseja deletar? ")
                        valorponto = valor.replace(',', '.')
                        for p3 in arq:
                            if valorponto in p3:
                                arq.seek(0)
                                for linha1 in arq:
                                    if nome in linha1:
                                        if categoria in linha1:
                                            if valorponto in linha1:
                                                erro.append(linha1.strip())
        arq.seek(0)
        for linha3 in arq:
            recuperacao.append(linha3.strip())
        arq.close()    
        arq = open('Arquivo.csv', 'w')
        arq.write('')
        arq.close()
        try:
            recuperacao.remove(erro[0])
            arq = open('Arquivo.csv', 'a')
            for c in range (len(recuperacao)):
                arq.write(recuperacao[c] + '\n')
            recuperacao.clear()
            erro.clear()
            arq.close()
            j = input("Deseja finalizar o sistema? ").lower()
            os.system("cls")
        except IndexError:
            print("Não há nada no arquivo.")
        

    elif operacao == 'edição':
        try:
            arq = open('Arquivo.csv', 'r')
            nome = input("Qual seu o nome completo? ").title()
            senha(nome)
            for o in arq:
                if nome in o:
                    categoria = input("Em qual categoria deseja editar? ").lower()
                    arq.seek(0)
                    for o2 in arq:
                        if categoria in o2:
                            arq.seek(0)
                            valor = input("Qual valor deseja editar? ")
                            valorponto = valor.replace(',', '.')
                            for o3 in arq:
                                if valorponto in o3:
                                    arq.seek(0)
                                    for linha2 in arq:
                                        if nome in linha2:
                                            if categoria in linha2:
                                                if valorponto in linha2:
                                                    erro.append(linha2.strip())
            arq.seek(0)
            for linha4 in arq:
                recuperacao.append(linha4.strip())
            arq.close()    
            arq = open('Arquivo.csv', 'w')
            arq.write('')
            arq.close()
            try:
                recuperacao.remove(erro[0])
                arq = open('Arquivo.csv', 'a')
                for c in range (len(recuperacao)):
                    arq.write(recuperacao[c] + '\n')
                recuperacao.clear()
                erro.clear()
                arq.close()
                arq = open("Arquivo.csv", 'a')
                while True:
                    ed = input("Deseja editar o nome a categoria o valor ou cancelar? ").lower()
                    if ed == 'nome':
                        nome = input("Qual o novo nome? ").title()
                        arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                        break
                    elif ed == 'categoria':
                        categoria = input("Qual a nova categoria? ").lower()
                        arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                        break
                    elif ed == 'valor':
                        valor = input("Qual o novo valor? ")
                        valorponto = valor.replace(',', '.')
                        arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                        break
                    elif ed == 'cancelar':
                        arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                        break
                        
                arq.close()
            except IndexError:
                os.system("cls")
                print("Não há nada no arquivo.")
        except NameError:
            print(end="")
        j = input("Deseja finalizar o sistema? ").lower()
        os.system("cls")
    elif operacao == 'saldo':
            file = open('Arquivo.csv', 'r')
            nome = input("Qual seu o nome? ").title()
            senha(nome)
            for s in file:
                if nome in s:
                    categoria = input("Em qual categoria deseja observar o saldo? ").lower()
                    file.seek(0)
                    for s2 in file:
                        if categoria in s2:
                            file.seek(0)
                            for linha5 in file:
                                if nome in linha5:
                                    if categoria in linha5:
                                        saldot.append(linha5.strip().split('; '))
                        if categoria == 'tudo':
                            file.seek(0)
                            for s5 in file:
                                if nome in s5:
                                    saldot.append(s5.strip().split('; '))
            for s3 in range(len(saldot)):
                valores.append(saldot[s3][2])
            for s4 in range(len(valores)):
                val += float(valores[s4])
            try:
                print(f'O seu saldo na categoria {categoria} é {val}')
                saldot.clear()
                valores.clear()
                val = 0
                file.close()
                j = input("Deseja finalizar o sistema? ").lower()
                os.system("cls") 
            except NameError:
                os.system("cls")
                print("Não há nada no arquivo.")

                    
        
    elif operacao == 'saque':
        arq = open('Arquivo.csv', 'a')
        nome = input("Qual seu o nome completo? ").title()
        senha(nome)
        categoria = input("De qual categoria deseja sacar? ").lower()
        valor = input("Qual valor deseja sacar? ")
        valorponto = valor.replace(',', '.')
        arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; -' + valorponto + '\n')
        arq.close()
        j = input("Deseja finalizar o sistema? ").lower()
        os.system("cls")
    else:
        print('Opção inválida.')
        print('As opções possíveis são:')
        print('Deposito \nLeitura \nDeleção \nEdição \nSaldo \nSaque')
    if j=="s":
        exit()
    elif j=="sim":
        exit()
    else:
        continue

