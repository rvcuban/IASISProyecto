import numpy as np
import FuncionesHeuristica as heur
def cargarArchivo():       #falta lanzar error en caso de que el archivo no exista o no este en la carpeta 
    with open('LABECOIN1.txt','r') as f:
        monedas=next(f)
        datos = ''.join(f.readlines()).replace('\n',';')
    m = np.matrix(datos)

    return (m,monedas)
 

def main():
    print("LABECOIN")
    labecoin,monedas = cargarArchivo()  #tenemos el mata y el numero de modenas 
    #despues de cargar el archivo vamos a localizar la posicion de los elementos y crearel tablero
    print("ESTE ES EL MAPA QUE SE VA A RESOLVER")
    print(f"El numero de monedas es {monedas}")
    print(labecoin)
    posRobot=heur.localizarObjetivo(labecoin, 8) 
    salida =heur.localizarObjetivo(labecoin,7)
    coordMonedas= heur.obtMonedasTab(labecoin)
    # Source: https://stackoverflow.com/questions/47432043

    print("¿Con que algoritmo quieres resolver el puzzle?")
    opcion = input("1-Escalada simple. \n 2-Maxima pendiente \n")

    match opcion:
        case 1:
            escaladaSimple()
        case 2:
            print("Aqui falta Maxima pendiente")
    
    
    
    tablero = heur.Tablero(monedas, posRobot[0],posRobot[1], labecoin,salida)
    
    heur.move_up(tablero)
    heur.move_right(tablero)
    heur.move_up(tablero)
    heur.move_right(tablero)
    heur.move_right(tablero)
 
    print(tablero)
    print(coordMonedas)
  
main()
