from classPerson import User
import re
#importa o modulo RE
users = []
employees = []

def id_validation(id):
    id = re.sub(r"[^0-9]", "", id)
    if len(id) != 11 or not id.isdigit():
        return False
#checa se o id entra em um padrão de formataçao
   
def email_validation(email):
    email_standard = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_standard, email) is not None
#checa se o email entra em um padrão de formataçao

def password_validation(password):
    if len(password) < 8:
        return False
    password_standard = r"^[0-9]{8,8}"
    return re.match(password_standard, password) is not None
#checa se o id entra em um padrão de formataçao

def registration_id_validation(registration_id):
    registration_id_standard = r"^\d{6,8}$"
    return re.match(registration_id_standard, registration_id) is not None
#checa se a matricula entra em um padrão de formataçao