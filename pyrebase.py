import re


def validar_cpf(cpf):
    cpf = re.sub(r"[^0-9]", "", cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
   

def validar_email(email):
    padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(padrao_email, email) is not None


def validar_password(password):
    if len(password) < 8:
        return False
    padrao_password = r"^[0-9]{8,8}"
    return re.match(padrao_password, password) is not None

def validar_matricula(matricula):
    padrao_matricula = r"^\d{6,8}$"
    return re.match(padrao_matricula, matricula) is not None