import numpy as np
def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento a[{}, {}] vale {}".format(x, y, tablero[x,y]))