from random import random

class Robo:
    nivel_critico = 0.60
    
    def __init__(self,nome:str) -> None:
        self.__nome = nome
        self.__vida = round(random(),3)
      
    @property 
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome:str):
        self.__nome = nome
        
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida:float):
        self.__vida = vida

    def __repr__(self) -> str:
        return f"Robô: {self.nome} | Vida = {round(self.vida,3)}"    
   
    def __add__(self, robo_gerador:"Robo")->"Robo":
        nome_bebe = self.nome.split('-',maxsplit=1)[0] + '-' + robo_gerador.nome.split('-',maxsplit=1)[0]
        return type(self)(nome_bebe)
        
    def precisa_de_medico(self):
        if self.__vida < Robo.nivel_critico:
            return True
        else:
            return False

