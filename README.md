# Rastreamentodedespesas
Manual do Sistema de Rastreamento de Despesas


Entendendo o Sistema
	O Sistema de Rastreamento de despesas tem como objetivo ajudar o usuário a rastrear e melhor controlar suas finanças. É necessário instalar o Python na sua máquina além de instalar o PIP requests, e após isso, utilizando o CMD ou o VSCode, será possível realizar às seguintes operações:
Deposito
Leitura
Deleção
Edição
Saldo
Saque
Explicaremos como funciona cada uma dessas funções posteriormente no manual.

2. Começando no sistema
	Agora que já sabemos qual o objetivo do sistema, vamos começar a utilizá-lo. Após iniciar o arquivo, digite qual das operações você deseja realizar, por questões de segurança e identificação, toda vez que o usuário iniciar uma das operações, será perguntado o nome e a senha do usuário. Caso seja a primeira vez que o usuário esteja usando o sistema, será pedido para que ele crie uma senha (Não esqueça essa senha, pois ela é única e não pode ser modificada posteriormente!). Após a identificação do usuário, a sua escolha de operação será executada.
3. Explicando de cada operação

Deposito
Faça Login
Escolha a categoria que você deseja adicionar (ex: Cinema, comida, energia);
Digite a moeda que você deseja utilizar, caso você esteja offline só será possível usar o Real
Caso seja em dólar ou euro, o valor será salvo em real.
Digite o valor que você deseja adicionar()
A sua operação foi concluída

Leitura
Faça Login
Digite a categoria a qual você quer ler
Em seguida você irá ler todos(se for o caso de ter mais um valor dentro da categoria) os valores dentro da categoria 
A sua operação foi concluída
Deleção
Faça Login
Digite a categoria que você deseja encerrar (Para a sua segurança, você só pode deletar uma transação por vez).
Digite o valor da transação específica que você deseja encerrar. ( Caso você tenha esquecido, encerre o programa e consulte na função de leitura.).
A operação foi concluída
Edição
Faça Login
Digite a categoria que você deseja editar
Digite o valor que você quer editar
Digite os novos valores
A sua operação foi concluída
Saldo
Faça Login
Digite seu nome
Digite a categoria ou digite “tudo” para olhar os valores
Veja o saldo
A sua operação foi concluída
Saque
Faça Login
Digite a categoria que você deseja sacar dinheiro
A operação foi concluída
