
import numpy as np
import FuncionesHeuristica as heur
def cargarArchivo():
    with open('LABECOIN1.txt','r') as f:
        datos = ''.join(f.readlines()).replace('\n',';')
    m = np.matrix(datos)

    return m

def main():
    print("LABECOIN")
    tablero = cargarArchivo()


    # Source: https://stackoverflow.com/questions/47432043

    print("¿Con que algoritmo quieres resolver el puzzle?")
    opcion = input("1-Escalada simple. \n 2-Maxima pendiente \n")

    match opcion:
        case 1:
            escaladaSimple()
        case 2:
            print("Aqui falta Maxima pendiente")
    
    print(heur.localizarObjetivo(tablero, 7))

    
main()
