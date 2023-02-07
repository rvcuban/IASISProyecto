import numpy as np
def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento a[{}, {}] vale {}".format(x, y, tablero[x,y]))
        break
    return x,y
class tablero:
    def __init__(self, monedas, posicionRobotX, posicionRobotY,table):
        self.monedas=monedas
        self.posicionRobotX= posicionRobotX
        self.posicionRobotY= posicionRobotY
        self.table = table
    



def move_up(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 1:
                if x > 0:
                    board[x, y] = 0
                    board[x - 1, y] = 1
                    return
                else:
                    print("Movimiento invalido")

    
def moverArriba(tablero):
    posRobotX = tablero.posicionRobotX
    posRobotY = tablero.posicionRobotY
    if tablero.table[posRobotX][posRobotY-1] == 9:
        return tablero
    
    if tablero.table[posRobotX][posRobotY-1] == 7:
        tablero.table[posRobotX][posRobotY-1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY-1] == range(1,6):
        tablero.table[posRobotX][posRobotY-1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY-1] == 7:
        tablero.table[posRobotX][posRobotY-1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY-1] == 0:
        tablero.table[posRobotX][posRobotY-1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    
