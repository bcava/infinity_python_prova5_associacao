class Prefeituras:
    def __init__(self, cidade, prefeito, empresas):
        self._cidade = cidade
        self._prefeito = prefeito
        self._empresas = empresas


    @property
    def cidade (self):
        return self._cidade
    
    @cidade.setter
    def cidade (self, cidade):
        self._cidade = cidade


    @property
    def prefeito (self):
        return self._prefeito
    
    @prefeito.setter
    def prefeito (self, prefeito):
        self._prefeito = prefeito


    @property
    def totalImpostos (self):
        return self._totalImpostos
    
    @totalImpostos.setter
    def totalImpostos (self, totalImpostos):
        self._totalImpostos = totalImpostos



    def total (self):
        totalTributos = 0
        for i in self._empresas:
            totalTributos += i.medLucroMensal *0.016
        return totalTributos
            