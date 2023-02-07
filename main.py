
import numpy as np
import FuncionesHeuristica as heur
def cargarArchivo():
    with open('LABECOIN1.txt','r') as f:
        datos = ''.join(f.readlines()).replace('\n',';')
    m = np.matrix(datos)

    return m

def main():
    print("LABECOIN")
    labecoin = cargarArchivo()


    # Source: https://stackoverflow.com/questions/47432043

    print("¿Con que algoritmo quieres resolver el puzzle?")
    opcion = input("1-Escalada simple. \n 2-Maxima pendiente \n")

    match opcion:
        case 1:
            escaladaSimple()
        case 2:
            print("Aqui falta Maxima pendiente")
    
    posRobot=heur.localizarObjetivo(labecoin, 7)
    tablero = heur.tablero(0, posRobot[0],posRobot[1], labecoin)
    
    heur.moverArriba(tablero)
    print(tablero)
main()
