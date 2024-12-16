import re

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