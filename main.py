
from classPerson import Person
from classPerson import Cliente
from classPerson import Funcionario

from login import validar_cpf
from login import validar_email
from login import validar_matricula
from login import validar_password
from login import clientes
from login import funcionarios


while True:
        
    print("=============== Login ===============")
    print("     Digite 1 para se Cadastrar      ")
    print("     Digite 2 para Logar             ")
    print("     Digite 3 para Sair              ")
    print("     Digite 4 se for funcionario     ")

    try:
        opcao = int(input("Digite a ação om base na tabela acima:"))
    except ValueError:
        print("Digite um numero valido!")

        continue



    if opcao == 1:
        name = input("Digite seu nome:")
        cpf = input("Digite seu cpf:")
        if not validar_cpf(cpf):
            print("Erro, CPF invalido")
            continue

        age = input("Digite sua idade:")
        email = input("Digite seu email para cadastrar:")
        if not validar_email(email):
            print("Email invalido")
            break


        password = input("Digite a senha para este conta:")

        for c in clientes:
            if c.getCpf() == cpf:
                print("Cpf já cadastrado")
                break
            if c.getEmail() == email:
                print("Email ja cadastrado")
                break
        
        newClient = Cliente(name, cpf, age, email, password)
        clientes.append(newClient)
    
       

    elif opcao == 2:
        email = input("Digite seu email:")
        password = input("Digite sua senha:")

        if clientes:
            cliente_encontrado = None
            for c in clientes:
                if c.getEmail() == email and c.getPassword() == password:
                    cliente_encontrado = c
                    break
            if cliente_encontrado:
                print(f"{cliente_encontrado.getName()}, seja bem vindo")
            else:
                print("Email ou senha incorretos")
        else:
            print("Nenhum cliente cadastrado")

    elif opcao == 3:
        print("Sessão encerrada!")
        break
    elif opcao == 4:
        matricula = input("Digite sua matricula:")
        if not validar_matricula(matricula):
            print("Matricula invalida")
            continue


        password = input("Digite sua senha:")
        if not validar_password(password):
            print("Senha invalida")
            continue

        if funcionarios:
            funcionario_encontrado = None
            for f in funcionarios:
                if f.getMatricula == matricula and f.getPassword == password:
                    funcionario_encontrado = f
                    break
            if funcionario_encontrado:
                print(f"Bem vindo {funcionario_encontrado.getName} ")
            else:
                print("Matricula ou senha incorretas")
        else:
            print("Nenhum funcionario cadastrado.")


        
