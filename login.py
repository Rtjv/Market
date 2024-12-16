import pyrebase
from classPerson import Cliente
import re



# Configurações do Firebase (copie os dados do Firebase Console)
firebase_config = {
    "apiKey": "SUA_API_KEY",
    "authDomain": "SEU_PROJETO.firebaseapp.com",
    "databaseURL": "https://SEU_PROJETO.firebaseio.com",
    "projectId": "SEU_PROJETO",
    "storageBucket": "SEU_PROJETO.appspot.com",
    "messagingSenderId": "SEU_SENDER_ID",
    "appId": "SUA_APP_ID"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


def validar_cpf(cpf):
    cpf = re.sub(r"[^0-9]", "", cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    def calcular_digito(cpf, peso_inicial):
        soma= sum(int(cpf[i])* (peso_inicial - i) for i in range(peso_inicial - 1))
        resto = soma % 11
        return "0" if resto <2 else str(11 - resto)
    
    primeiro_digito = calcular_digito(cpf, 10)
    segundo_digito = (cpf, 11)

    return cpf[-2:] == primeiro_digito + segundo_digito

def validar_email(email):
    padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao_email, email) is not None


def validar_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

def validar_matricula(matricula):
    padrao_matricula = r"^\d{6,8}$"
    return re.match(padrao_matricula, matricula) is not None

from classPerson import Person
from classPerson import Cliente
from classPerson import Funcionario

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

        clientes = db.child("clientes").get()
        if clientes.val():
            for c in clientes.each():
                if c.val()["cpf"] == cpf:
                    print("Cpf já cadastrado")
                    break
                if c.val()["email"] == email:
                    print("Email ja cadastrado")
                    break
            else:
                db.child("clientes").push(cliente_data)
                print("Cliente cadastrado com sucesso")
        else:
            db.child("clientes").push(cliente_data)
            print("Cliente cadastrado com sucesso")
       

    elif opcao == 2:
        email = input("Digite seu email:")
        password = input("Digite sua senha:")

        clientes = db.child("clientes").get()
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

        funcionarios = db.child("funcionarios").get()
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


        
