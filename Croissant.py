from Empresa import Empresa


class Croissant (Empresa):
    def __init__(self, nome, cnpj, medfuncionarios, medLucroMensal):
        super().__init__(nome, cnpj, medfuncionarios, medLucroMensal)