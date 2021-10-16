class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self.__nome = nome
        self.__cpf = cpf
        self.__formacao = formacao



    @property
    def nome (self):
        return self.__nome
    
    @nome.setter
    def nome (self, nome):
        self.__nome = nome

    @property
    def cpf (self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, cpf):
        self.__cpf = cpf

    @property
    def formacao (self):
        return self.__formacao
    
    @formacao.setter
    def formacao (self, formacao):
        self.__formacao = formacao