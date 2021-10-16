
class Empresa:
    def __init__(self, nome, cnpj, medFuncionarios, medLucroMensal):
        self._nome = nome
        self._cnpj = cnpj
        self._medFuncionarios = medFuncionarios 
        self._medLucroMensal = medLucroMensal


    @property
    def nome (self):
        return self._nome
    
    @nome.setter
    def nome (self, nome):
        self._nome = nome

    @property
    def cnpj (self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj (self, cnpj):
        self._cnpj = cnpj  

    @property
    def medFuncionarios (self):
        return self._medFuncionarios
    
    @medFuncionarios.setter
    def medFuncionarios (self, medFuncionarios):
        self._medFuncionarios = medFuncionarios 


    @property
    def medLucroMensal (self):
        return self._medLucroMensal
    
    @medLucroMensal.setter
    def medLucroMensal (self, medLucroMensal):
        self._medLucroMensal = medLucroMensal 
    



