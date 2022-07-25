from random import random
from robo import Robo

class RoboMedico(Robo):
  
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.poder_de_cura = round(random(),3)
     
    def __repr__(self) -> str:
        return super().__repr__() + f" | Poder de cura = {self.poder_de_cura}"
    
    def curar(self,robo_paciente:"Robo"):
        if self.vida >= robo_paciente.vida:
            if robo_paciente.precisa_de_medico() == True:
                robo_paciente.vida += self.poder_de_cura 
                if robo_paciente.vida > 1.0:
                    robo_paciente.vida = 1.0
        else:
            print(f"O {self.nome} tem vida de {self.vida} que não é suficiente para curar o {robo_paciente.nome} com vida de {robo_paciente.vida}\n")
