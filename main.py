from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
from random import randint
import random
import time
if __name__ == "__main__":
    lista_robo = []
    lista_robo_lutador = []
    lista_robo_medico = []

    def add_lista(lista:list,elem)->None:
        lista.append(elem)
    
    def imprimir_lista(lista:list)->None:
        if lista == []:
            print("==============================================================================================\n\t\t\t\t\tLista Vazia\n==============================================================================================")
        else:
            print("==============================================================================================")
            for ind in range(len(lista)):
                print("| "+str(type(lista[ind]))+" | Code: "+str(ind)+" | "+str(lista[ind])+"\n")

    def curar_atacado(robo_atacado)->None:
        if lista_robo_medico != []:
            if robo_atacado.vida < 0.1:
                if randint(0,1) == 1:
                    medico_id = random.choice(range(len(lista_robo_medico)))
                    time.sleep(2)
                    print(f"\n=====| Status do robô antes da cura |=====\n {robo_atacado}")
                    lista_robo_medico[medico_id].curar(robo_atacado)
                    time.sleep(2)
                    print(f"\n=====| Status do robô após a cura |=====\n {robo_atacado}")
            else:
                time.sleep(2)
                print(f"{robo_atacado.nome} não foi curado! Pois há a probabilidade de 50% de um médico realizar a cura!!\n")
        else:
            time.sleep(2)
            print("Ainda não é possível realizar cura de robôs *-* Crie robô médico para desbloquear essa função ;)")

    def gerar_robo_menu()->None:
        print("=========| **Tipos de Robôs para Gerar** |=========\n1 - Robô\n2 - Robô Médico\n3 - Robô Lutador")
        opcao = int(input("Insira o tipo de robô para ser gerado: "))
        if opcao == 1:
           print("Criando Robô...")
           nome_robo = str(input("Insira o nome do robô: "))
           add_lista(lista_robo,Robo(nome_robo))
           
           print(f"Robô Criado ^-^... Hello World! by: {nome_robo}")
        elif opcao == 2:
            print("Criando Robô Médico...\n")
            nome_robo_med = str(input("Insira o nome do robô médico: "))
            add_lista(lista_robo_medico,RoboMedico(nome_robo_med))
            add_lista(lista_robo,RoboMedico(nome_robo_med))
        
            print(f"Robô Médico Criado ^-^... Hello World! by: {nome_robo_med}")
        elif opcao == 3:
            print("Criando Robô Lutador...\n")
            nome_robo_lutador = str(input("Insira o nome do robô lutador: "))
            add_lista(lista_robo_lutador,RoboLutador(nome_robo_lutador))
            add_lista(lista_robo,RoboLutador(nome_robo_lutador))
           
            print(f"Robô Lutador Criado ^-^... Hello World! by: {nome_robo_lutador}")
        else:
            print("Opção inválida :/ Tente Novamente!") 
    
    def casar_robo()->None:
        
        if len(lista_robo) >= 2:
            print("=========| **Casamento de Robôs** |=========\n")
            imprimir_lista(lista_robo)
            cod1_robo_casar = int(input("Insira o código do robô 1 para casar: "))
            cod2_robo_casar = int(input("Insira o código do robô 2 para casar: "))
            if ((cod1_robo_casar > len(lista_robo)) or (cod2_robo_casar > len(lista_robo))):
                raise IndexError("Valores de Code inválidos!")
            else:
                if(len(lista_robo) >= 2):
                    filho_robo = lista_robo[cod1_robo_casar] + lista_robo[cod2_robo_casar]
                    add_lista(lista_robo,filho_robo)
                    if str(type(filho_robo)) == "<class 'robo_lutador.RoboLutador'>":
                        add_lista(lista_robo_lutador,filho_robo)
                    elif str(type(filho_robo)) == "<class 'robo_medico.RoboMedico'>":
                        add_lista(lista_robo_medico,filho_robo)
        else:
            print("Poxa não é possível realizar o casamento de robôs :( Crie mais robôs e tente novamente!")
        
    def gerar_robo()->None:
        print("=========| **Geração de Robôs** |=========\n1 - Gerar um novo robô\n2 - Gerar um novo robô a partir de um casamento\n")
        opcao = int(input("Insira uma opção da maneira que deseja gerar um novo robô: "))
        if opcao == 1:
            gerar_robo_menu()
        elif opcao == 2:
            casar_robo()
        else:
            print("Opção inválida :/ Tente Novamente!")
    def luta_robos()->None:
        
        if lista_robo_lutador == []:
            print("Ainda não é pssível que os robôs lutem :/ Crie robôs lutadores!")
        else:
            print("=========| **Luta**  |=========")
            imprimir_lista(lista_robo_lutador)
            if len(lista_robo) > 1:
                robo_lutador = int(input("Insira o código do robô lutador: "))
                imprimir_lista(lista_robo)
                robo_atacado = int(input("Insira o código do robô que será atacado: "))
                
                res_bool = lista_robo_lutador[robo_lutador].atacar(lista_robo[robo_atacado])
                if res_bool == True:
                    curar_atacado(lista_robo[robo_atacado])
                else:
                    pass
            else:
                print("Crie mais robôs para lutar. Um robô não pode lutar contra ele mesmo!!\n")
    while(True):
        print("=============| Disputa de Robôs |===========\n|\t1 - Gerar um novo robô\t\t   |")
        print("|\t2 - Lutar \t\t\t   |\n|\t3 - Listar os robôs\t\t   |\n|\t4 - Encerrar a execução\t\t   |\n")
        opcao = int(input("Insira uma opção para executar a função que deseja: "))
        if opcao == 1:
            gerar_robo()
        elif opcao == 2:
            luta_robos()
        elif opcao == 3:
            lista_robo_lutador = []
            lista_robo_medico = []
            print("\t\tROBÔS")
            imprimir_lista(lista_robo)
            print("\t\tROBÔS LUTADORES")
            for ind in range(len(lista_robo)):
                if str(type(lista_robo[ind])) == "<class 'robo_lutador.RoboLutador'>":
                    add_lista(lista_robo_lutador,lista_robo[ind])
            imprimir_lista(lista_robo_lutador)
            print("\t\tROBÔS MÉDICOS")
            for ind in range(len(lista_robo)):
                if str(type(lista_robo[ind])) == "<class 'robo_medico.RoboMedico'>":
                    add_lista(lista_robo_medico,lista_robo[ind])
            imprimir_lista(lista_robo_medico)
        elif opcao == 4:
            break
        else:
            print("Opção inválida :/ Tente novamente!")