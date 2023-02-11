import sys
import numpy as np

def move_up(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 7:       #7 por el identificador del robot 
                if x > 0:
                    board[x, y] = 0
                    board[x - 1, y] = 1
                    return
                else:
                    print("Movimiento invalido")

def move_down(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 7:
                if x < board.shape[0] - 1:
                    board[x, y] = 0
                    board[x + 1, y] = 1
                    return
                else:
                    print("Movimiento invalido")

def move_left(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 7:
                if y > 0:
                    board[x, y] = 0
                    board[x, y - 1] = 1
                    return
                else:
                    print("Movimiento invalido")

def move_right(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 1:
                if y < board.shape[1] - 1:
                    board[x, y] = 0
                    board[x, y + 1] = 1
                    return
                else:
                    print("Movimiento invalido")

tablero = np.zeros((10, 10))
tablero[0, 0] = 1

print(tablero)
print("Siguiente movimiento")
move_down(tablero)
print(tablero)
print("Siguiente movimiento")
move_right(tablero)
print(tablero)
print("Siguiente movimiento")
move_up(tablero)
print(tablero)
print("Siguiente movimiento")
move_left(tablero)