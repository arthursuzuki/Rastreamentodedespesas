import os
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

def senha(nome):
    bdd = open("logins.csv", "r+")
    cnt = 0
    linhas = bdd.readlines()
    bdd.seek(0)
    linha = ""
    loop=True
    for i, linha_atual in enumerate(linhas):
        campos=linha_atual.strip().split(';')
        if nome == campos[0]:
            while loop == True:
                senha_atual=campos[1]
                senha_digitada=input("Digite a senha: ")
                cnt+=1
                if senha_digitada == senha_atual:
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

def operacao(j):
    while j != 'n':
        print("Bem vindo ao Sistema de rastreamento de despesas")
        print('Escolha uma das seguintes operações: ')
        print('Deposito \nLeitura \nDeleção \nEdição \nSaldo \nSaque')
        operacao = input("Qual operação deseja realizar? ").lower()
        os.system("cls")
        if operacao == 'deposito':
            arq = open('Arquivo.csv', 'a')
            nome = input("Qual seu o nome? ").title()
            senha(nome)
            categoria = input("Em qual categoria deseja depositar? ").lower()
            valor = input("Qual valor deseja depositar? ")
            valorponto = valor.replace(',', '.')
            arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
            arq.close()
            j = input("Deseja continuar?[S/N] ").lower()
            os.system("cls")
            continue

        elif operacao == 'leitura':
            arq = open('Arquivo.csv', 'r')
            nome = input("Qual seu o nome? ").title()
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
            j = input("Deseja continuar?[S/N] ").lower()
            os.system("cls")
            continue

        elif operacao == 'deleção':
            arq = open('Arquivo.csv', 'r')
            nome = input("Qual seu o nome? ").title()
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
            recuperacao.remove(erro[0])
            arq = open('Arquivo.csv', 'a')
            for c in range (len(recuperacao)):
                arq.write(recuperacao[c] + '\n')
            recuperacao.clear()
            erro.clear()
            arq.close()
            j = input("Deseja continuar?[S/N] ").lower()
            os.system("cls")
            continue

        elif operacao == 'edição':
            try:
                arq = open('Arquivo.csv', 'r')
                nome = input("Qual seu o nome? ").title()
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
                    else:
                        continue
                arq.close()
            except NameError:
                print(end="")
            j = input("Deseja continuar?[S/N] ").lower()
            os.system("cls")
            continue
        elif operacao == 'saldo':
            try:
                arq = open('Arquivo.csv', 'r')
                nome = input("Qual seu o nome? ").title()
                senha(nome)
                for s in arq:
                    if nome in s:
                        categoria = input("Em qual categoria deseja observar o saldo? ").lower()
                        arq.seek(0)
                        for s2 in arq:
                            if categoria in s2:
                                arq.seek(0)
                                for linha5 in arq:
                                    if nome in linha5:
                                        if categoria in linha5:
                                            saldot.append(linha5.strip().split('; '))
                            if categoria == 'tudo':
                                arq.seek(0)
                                for s5 in arq:
                                    if nome in s5:
                                        saldot.append(s5.strip().split('; '))
                for s3 in range(len(saldot)):
                    valores.append(saldot[s3][2])
                for s4 in range(len(valores)):
                    val += float(valores[s4])
                print(f'O seu saldo na categoria {categoria} é {val}')
                saldot.clear()
                valores.clear()
                val = 0
                arq.close()
                j = input("Deseja continuar?[S/N] ").lower()
                os.system("cls")
                continue
            except NameError:
                print(end="")
                j = input("Deseja continuar?[S/N] ").lower()
                os.system("cls")
                continue
            
        elif operacao == 'saque':
            arq = open('Arquivo.csv', 'a')
            nome = input("Qual seu o nome? ").title()
            senha(nome)
            categoria = input("De qual categoria deseja sacar? ").lower()
            valor = input("Qual valor deseja sacar? ")
            valorponto = valor.replace(',', '.')
            arq.write('Nome: ' + nome + ' ; ' + categoria + ' ; -' + valorponto + '\n')
            arq.close()
            j = input("Deseja continuar?[S/N] ").lower()
            os.system("cls")
            continue  
        else:
            print('Opção inválida.')
            print('As opções possíveis são:')
            print('Deposito \nLeitura \nDeleção \nEdição \nSaldo \nSaque')
            
operacao(j)