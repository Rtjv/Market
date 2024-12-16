class Person:
    def __init__(self, name, cpf, age):
        self.__name = name
        self.__cpf = cpf
        self.__age = age


class Cliente(Person):
    def __init__(self, name, cpf, age, email, password):
        super().__init__(name, cpf, age)
        self.__email = email
        self.__password = password
        


class Funcionario(Person):
    def __init__(self, name, cpf, age, matricula, password):
        super().__init__(name, cpf, age)
        self.__matricula = matricula
        self.__password = password


    