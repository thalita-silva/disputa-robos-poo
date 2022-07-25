from random import uniform
from robo import Robo
import time
class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str) -> None:
       super().__init__(nome)
       self.poder_dano = round(uniform(RoboLutador.dano_maximo,1.0),3)

    def __repr__(self) -> str:
        return super().__repr__() + f'| Poder de dano = {self.poder_dano}'
   
    def atacar(self,robo_atacado)->bool:
        if self.nome != robo_atacado.nome:
            robo_atacado.vida *= (1 - self.poder_dano)
            if str(type(robo_atacado)) == "<class 'robo_lutador.RoboLutador'>":
                print(f"O {self.nome} atacou outro robô lutador O.O prepare-se para o contra-ataque!!")
                time.sleep(2)
                self.vida *= (1 - robo_atacado.poder_dano)
                print(f"{robo_atacado.nome} contra-atacou seu oponente...")
                time.sleep(2)
                print(f"Status Robô Lutador após contra-ataque: {self}\nStatus Robô Atacado após a luta: {robo_atacado}")
            else:
                time.sleep(2)
                print(f"\nStatus Robô Atacado após a luta: {robo_atacado}")
            return True
        else:
            print("Um robô não pode lutar contra ele mesmo!! Inicie outra luta entre robôs diferentes!")
            return False
            
        

