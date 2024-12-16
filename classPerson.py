class Person:
    def __init__(self, name, cpf, age):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
    def getCpf(self):
        return self.__cpf
    
class Cliente(Person):
    def __init__(self, name, cpf, age, email, password):
        super().__init__(name, cpf, age)
        self.__email = email
        self.__password = password
        
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def getName(self):
        return self.__name


class Funcionario(Person):
    def __init__(self, name, cpf, age, matricula, password):
        super().__init__(name, cpf, age)
        self.__matricula = matricula
        self.__password = password
    
    def getMatricula(self):
        return self.__matricula

    