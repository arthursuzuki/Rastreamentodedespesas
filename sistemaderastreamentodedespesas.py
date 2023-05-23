import os
os.system('cls')

j = 's'
erro = []
recuperacao = []
deletado = []
saldot = []
valores = []
val = 0
while j != 'n':
    operacao = input("Qual operação deseja realizar? ").lower()
    if operacao == 'deposito':
        file = open('Arquivo.csv', 'a')
        nome = input("Qual seu o nome? ").title()
        categoria = input("Em qual categoria deseja depositar? ").lower()
        valor = input("Qual valor deseja depositar? ")
        valorponto = valor.replace(',', '.')
        file.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
        file.close()

    elif operacao == 'leitura':
        file = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome? ").title()
        for k in file:
            if nome in k:
                categoria = input("Em qual categoria deseja observar? ").lower()
                file.seek(0)
                for k2 in file:
                    if categoria in k2:
                        file.seek(0)
                        for linha in file:
                            if nome in linha:
                                if categoria in linha:
                                    print(linha.strip())
                if categoria == 'tudo':
                    file.seek(0)
                    for k3 in file:
                        if nome in k3:
                            print(k3.strip())
        file.close()

    elif operacao == 'deleção':
        file = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome? ").title()
        for p in file:
            if nome in p:
                categoria = input("Em qual categoria deseja deletar? ").lower()
                file.seek(0)
                for p2 in file:
                    if categoria in p2:
                        file.seek(0)
                        valor = input("Qual valor deseja deletar? ")
                        valorponto = valor.replace(',', '.')
                        for p3 in file:
                            if valorponto in p3:
                                file.seek(0)
                                for linha1 in file:
                                    if nome in linha1:
                                        if categoria in linha1:
                                            if valorponto in linha1:
                                                erro.append(linha1.strip())
        file.seek(0)
        for linha3 in file:
            recuperacao.append(linha3.strip())
        file.close()    
        file = open('Arquivo.csv', 'w')
        file.write('')
        file.close()
        recuperacao.remove(erro[0])
        file = open('Arquivo.csv', 'a')
        for c in range (len(recuperacao)):
            file.write(recuperacao[c] + '\n')
        recuperacao.clear()
        erro.clear()
        file.close()

    elif operacao == 'edição':
        file = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome? ").title()
        for o in file:
            if nome in o:
                categoria = input("Em qual categoria deseja editar? ").lower()
                file.seek(0)
                for o2 in file:
                    if categoria in o2:
                        file.seek(0)
                        valor = input("Qual valor deseja editar? ")
                        valorponto = valor.replace(',', '.')
                        for o3 in file:
                            if valorponto in o3:
                                file.seek(0)
                                for linha2 in file:
                                    if nome in linha2:
                                        if categoria in linha2:
                                            if valorponto in linha2:
                                                erro.append(linha2.strip())
        file.seek(0)
        for linha4 in file:
            recuperacao.append(linha4.strip())
        file.close()    
        file = open('Arquivo.csv', 'w')
        file.write('')
        file.close()
        recuperacao.remove(erro[0])
        file = open('Arquivo.csv', 'a')
        for c in range (len(recuperacao)):
            file.write(recuperacao[c] + '\n')
        recuperacao.clear()
        erro.clear()
        file.close()
        file = open("Arquivo.csv", 'a')
        while True:
            ed = input("Deseja editar o nome a categoria o valor ou cancelar? ").lower()
            if ed == 'nome':
                nome = input("Qual o novo nome? ").title()
                file.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                break
            elif ed == 'categoria':
                categoria = input("Qual a nova categoria? ").lower()
                file.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                break
            elif ed == 'valor':
                valor = input("Qual o novo valor? ")
                valorponto = valor.replace(',', '.')
                file.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                break
            elif ed == 'cancelar':
                file.write('Nome: ' + nome + ' ; ' + categoria + ' ; ' + valorponto + '\n')
                break
            else:
                continue
        file.close()
    elif operacao == 'saldo':
        file = open('Arquivo.csv', 'r')
        nome = input("Qual seu o nome? ").title()
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
        print(f'O seu saldo na categoria {categoria} é {val}')
        saldot.clear()
        valores.clear()
        val = 0
        file.close()
    elif operacao == 'saque':
        file = open('Arquivo.csv', 'a')
        nome = input("Qual seu o nome? ").title()
        categoria = input("De qual categoria deseja sacar? ").lower()
        valor = input("Qual valor deseja sacar? ")
        valorponto = valor.replace(',', '.')
        file.write('Nome: ' + nome + ' ; ' + categoria + ' ; -' + valorponto + '\n')
        file.close()    
    else:
        print('Opção inválida.')
        print('As opções possíveis são:')
        print('Deposito \nLeitura \nDeleção \nEdição \nSaldo \nSaque')

    j = input("Deseja continuar?[S/N] ").lower()
