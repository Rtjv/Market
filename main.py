
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
            continue


        password = input("Digite a senha para este conta:")
        
        cliente_data = {
            "name": name,
            "cpf": cpf,
            "age": age,
            "email": email,
            "password": password
        }

        funcionario_data = {
            "name":name,
            "cpf":cpf,
            "age":age,
            "matricula":matricula,
            "password":password

        }

        if clientes.val():
            for c in clientes.each():
                if c.val()["cpf"] == cpf:
                    print("Cpf já cadastrado")
                    break
                if c.val()["email"] == email:
                    print("Email ja cadastrado")
                    break
            else:
                print("Cliente cadastrado com sucesso")
        else:
            print("Cliente cadastrado com sucesso")
       

    elif opcao == 2:
        email = input("Digite seu email:")
        password = input("Digite sua senha:")

        if clientes.val():
            cliente_encontrado = None
            for c in clientes.each():
                if c.val()["email"] == email and c.val()["password"] == password:
                    cliente_encontrado = c.val()
                    break
            if cliente_encontrado:
                print(f"{cliente_encontrado['name']}, seja bem vindo")
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

        if funcionarios.val():
            funcionario_encontrado = None
            for f in funcionarios.each():
                if f.val()["matricula"] == matricula and f.val()["password"] == password:
                    funcionario_encontrado = f.val()
                    break
            if funcionario_encontrado:
                print(f"Bem vindo {funcionario_encontrado['name']} ")
            else:
                print("Matricula ou senha incorretas")
        else:
            print("Nenhum funcionario cadastrado.")


        
