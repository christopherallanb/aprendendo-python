
"" """                _      _              _                        _          _                                _       
                (_)    | |            | |                      | |        | |                              (_)      
 _ __  _ __ ___  _  ___| |_ ___     __| | ___    ___ ___  _ __ | |_ __ _  | |__   __ _ _ __   ___ __ _ _ __ _  __ _ 
| '_ \| '__/ _ \| |/ _ \ __/ _ \   / _` |/ _ \  / __/ _ \| '_ \| __/ _` | | '_ \ / _` | '_ \ / __/ _` | '__| |/ _` |
| |_) | | | (_) | |  __/ |_ (_) | | (_| |  __/ | (__ (_) | | | | |_ (_| | | |_) | (_| | | | | (__ (_| | |  | | (_| |
| .__/|_|  \___/| |\___|\__\___/   \__,_|\___|  \___\___/|_| |_|\__\__,_| |_.__/ \__,_|_| |_|\___\__,_|_|  |_|\__,_|
| |            _/ |                                                                                                 
|_|           |__/                                                                                                  
"""""

#nunca mais faça isso, não vale a pena




DEFAULT_USER = "cristopher"
DEFAULT_PASSWORD = "1212"
DEFAULT_CPF = "11130931455"
DEFAULT_IDADE = 18
DEFAULT_BALANCE_CRISTOPHER = 1000.0
DEFAULT_BALANCE_NEW_USER = 0.0

def menu():
    print("Menu de Opções:")
    print("1 - Login")
    print("2 - Registrar Usuário")
    print("3 - Sair")

def login(nickname, password):
    return nickname == DEFAULT_USER and password == DEFAULT_PASSWORD

def cadastrar_usuario(nickname, cpf, idade, password):
    print(f"Usuário {nickname} cadastrado com CPF {cpf} e idade {idade}.")
    return DEFAULT_BALANCE_NEW_USER

def verificar_usuario_existente(nome_usuario):
    return nome_usuario == DEFAULT_USER

def cadastrar_usuario_default():
    if not verificar_usuario_existente(DEFAULT_USER):
        print(f"Usuário padrão {DEFAULT_USER} criado com saldo inicial de R$ {DEFAULT_BALANCE_CRISTOPHER}.")

cadastrar_usuario_default()

print("\nBem-vindo ao nosso sistema, informe o que deseja abaixo:")
user_balance = DEFAULT_BALANCE_CRISTOPHER

while True:
    menu()
    try:
        escolha = int(input("--> "))
        if escolha == 1:
            nome_login = input('Digite seu nickname: ')
            senha_login = input('Digite sua senha: ')
            if login(nome_login, senha_login):
                print("Login realizado com sucesso!")
                
                while True:
                    print("Bem-vindo ao banco!")
                    print("1 = Saque\n2 = Depósito\n3 = Consultar saldo\n4 = Sair")

                    usuario = input("O que gostaria de fazer?: ")
                    
                    if usuario.isdigit() and int(usuario) in [1, 2, 3, 4]:
                        usuario = int(usuario)

                        if usuario == 4:
                            print("Até logo!")
                            break

                        if usuario == 1:
                            valor_saque = float(input("Qual o valor do saque? "))
                            if valor_saque > user_balance:
                                print("Você não tem saldo suficiente para realizar este saque.")
                            else:
                                user_balance -= valor_saque
                                print("Saque realizado com sucesso. Seu saldo atual é de R$", user_balance)

                        elif usuario == 2:
                            valor_deposito = float(input("Qual o valor do depósito? "))
                            user_balance += valor_deposito
                            print("Depósito realizado com sucesso. Seu saldo atual é de R$", user_balance)

                        elif usuario == 3:
                            print("Seu saldo atual é de R$", user_balance)

            else:
                print("Login falhou. Verifique seu nickname e senha.")

        elif escolha == 2:
            while True:
                nome = input('Informe seu nickname: ')
                if nome == DEFAULT_USER:
                    print("Este nickname já está em uso. Tente outro.")
                    continue
                
                cpf = input("Informe seu CPF (11 dígitos sem pontuação): ")
                if cpf.isdigit() and len(cpf) == 11 and cpf != DEFAULT_CPF:
                    formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                    idade = int(input("Idade: "))
                    if idade < 18:
                        print("A idade deve ser 18 anos ou mais. Tente novamente.")
                        continue
                    
                    senha = input('Informe sua senha (4 a 12 caracteres): ')
                    if 4 <= len(senha) <= 12:
                        user_balance = cadastrar_usuario(nome, formatted_cpf, idade, senha)
                        print("Usuário cadastrado com sucesso!")
                        break
                    else:
                        print("A senha deve ter entre 4 e 12 caracteres. Tente novamente.")
                else:
                    print("Este CPF já está cadastrado (pertence ao usuário padrão) ou é inválido. Tente outro.")
                    
            print("Bem-vindo ao banco!")
            while True:
                print("1 = Saque\n2 = Depósito\n3 = Consultar saldo\n4 = Sair")
                usuario = input("O que gostaria de fazer?: ")
                
                if usuario.isdigit() and int(usuario) in [1, 2, 3, 4]:
                    usuario = int(usuario)

                    if usuario == 4:
                        print("Até logo!")
                        break

                    if usuario == 1:
                        valor_saque = float(input("Qual o valor do saque? "))
                        if valor_saque > user_balance:
                            print("Você não tem saldo suficiente para realizar este saque.")
                        else:
                            user_balance -= valor_saque
                            print("Saque realizado com sucesso. Seu saldo atual é de R$", user_balance)

                    elif usuario == 2:
                        valor_deposito = float(input("Qual o valor do depósito? "))
                        user_balance += valor_deposito
                        print("Depósito realizado com sucesso. Seu saldo atual é de R$", user_balance)

                    elif usuario == 3:
                        print("Seu saldo atual é de R$", user_balance)

        elif escolha == 3:
            print("Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Por favor, insira um número válido.")



                    
                                      ##          
                                      ############
                                    ##############
                                  ##############  
                            ##################    
                      ####################        
      ##            ####################          
                  ######################          
    ##            ######################          
    ##            ######################          
  ##            ##################      ##        
  ##          ##################        ##        
  ##          ################                    
  ##        ##################                    
  ####    ####################                    
    ################################              
                                                  