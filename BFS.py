import FuncionesHeuristica as fh

def BFS (inicial:fh.Tablero):
    listaAbiertos= []
    while (not fh.hemosTerminado(inicial)):
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY):
            listaAbiertos.append(fh.move_up(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY):
            listaAbiertos.append(fh.move_down(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.move_left(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.move_right(inicial))
             
 #diagonales, y javi tiene que cambiar las variables del movValid
        if fh.movValid(inicial, inicial.posicionRobotX +1, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.diag_downLeft(inicial))     
        if fh.movValid(inicial, inicial.posicionRobotX + 1, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.diag_downRight(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX -1, inicial.posicionRobotY - 1):
            listaAbiertos.append(fh.diag_upLeft(inicial))
        if fh.movValid(inicial, inicial.posicionRobotX - 1, inicial.posicionRobotY + 1):
            listaAbiertos.append(fh.diag_upRight(inicial))      
        
        mejorNodo = listaAbiertos[0]
        #Recorremos la lista de abiertos para conseguir el nodo con mejor heuristica
        
        for nodo in listaAbiertos:
            if mejorNodo.h < nodo.h:
                mejorNodo = nodo

        listaAbiertos.remove(mejorNodo) 
        if (mejorNodo.h > inicial.h):
            inicial = mejorNodo
        else:
            print("BFS no ha podido encontrar una solución")
            print(inicial.movimientosRealizados)
            return

    print(f"{inicial.table} es la solución encontrada por BFS")
    





    

        
            
        


        

