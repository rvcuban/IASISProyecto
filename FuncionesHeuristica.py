import numpy as np


def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento buscado[{}, {}] vale {}".format(x, y, tablero[x, y]))
        break
    return x, y


class Tablero:
    """esta es la clase tablero que almacenara toda la infomracion del juego"""

    def __init__(self, monedas, posicionRobotX, posicionRobotY, table, salida,coordMonedas):
        if not monedas:
            return None
        self.monedas = monedas
        self.posicionRobotX = posicionRobotX
        self.posicionRobotY = posicionRobotY
        self.table = table

        # agregado
        self.monedasRecogidas = 0 # contador con monedas recogidas hasta el momento dentro del tablero
        self.salida = salida
        self.coordMonedas= coordMonedas #lista de las coordenadas de las monedas dentro de la matriz 

    def __str__(self) -> str:
        return f"Numero de monedas:{self.monedas} en el tablero\n {self.table}\n posicion del robot:{self.posicionRobotX,self.posicionRobotY}\n el numero de monedas recogidas actualmente es {self.monedasRecogidas}"


def obtMonedasTab(tablero):
    listaMonedas=[]
    dim = len(tablero)  # Es una matriz cuadrada N x N
    print(tablero[1,1])
    for i in range(0, dim):  # columna
        for j in range(0, dim):  # fila
            if (tablero[i,j]>=1) and (tablero[i,j]<7):
                posicion=i,j
                listaMonedas.append(posicion)
    return listaMonedas

def movValid(tablero: Tablero, x, y):
    if tablero.table[x, y] != 9:
        return True


def hayMoneda(tablero: Tablero, x, y):
    if tablero.table[x, y] < 7:
        valorMoneda = tablero.table[x, y]
        m = True
        return (m, valorMoneda)
    else:
        m = False
        return m


def move_up(tablero: Tablero):
    x = tablero.posicionRobotX
    y = tablero.posicionRobotY

    if movValid(tablero, x - 1, y):
        exisMoneda, valorMoneda = hayMoneda(tablero, x - 1, y)
        if (
            exisMoneda
        ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            tablero.monedasRecogidas = (
                tablero.monedasRecogidas + valorMoneda
            )  # modenas[1] almacena el valor

        tablero.posicionRobotX = tablero.posicionRobotX - 1
        tablero.posicionRobotY = tablero.posicionRobotY
        tablero.table[x - 1, y] = 8
        tablero.table[x, y] = 0
    else:
        print("movimineto invalido;el robot permanece quieto")


def move_down(tablero: Tablero):
    x = tablero.posicionRobotX
    y = tablero.posicionRobotY

    if movValid(tablero, x + 1, y):
        exisMoneda, valorMoneda = hayMoneda(tablero, x + 1, y)
        if (
            exisMoneda
        ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            tablero.monedasRecogidas = (
                tablero.monedasRecogidas + valorMoneda
            )  # modenas[1] almacena el valor

        tablero.posicionRobotX = tablero.posicionRobotX + 1
        tablero.posicionRobotY = tablero.posicionRobotY
        tablero.table[x + 1, y] = 8
        tablero.table[x, y] = 0
    else:
        print("movimineto invalido;el robot permanece quieto")


def move_left(tablero: Tablero):
    x = tablero.posicionRobotX
    y = tablero.posicionRobotY

    if movValid(tablero, x, y - 1):
        exisMoneda, valorMoneda = hayMoneda(tablero, x, y - 1)
        if (
            exisMoneda
        ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            tablero.monedasRecogidas = (
                tablero.monedasRecogidas + valorMoneda
            )  # modenas[1] almacena el valor

        tablero.posicionRobotX = tablero.posicionRobotX
        tablero.posicionRobotY = tablero.posicionRobotY - 1
        tablero.table[x, y - 1] = 8
        tablero.table[x, y] = 0
    else:
        print("movimineto invalido;el robot permanece quieto")


def move_right(tablero: Tablero):
    x = tablero.posicionRobotX
    y = tablero.posicionRobotY

    if movValid(tablero, x, y + 1):
        exisMoneda, valorMoneda = hayMoneda(tablero, x, y + 1)
        if (
            exisMoneda
        ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            tablero.monedasRecogidas = (
                tablero.monedasRecogidas + valorMoneda
            )  # modenas[1] almacena el valor

        tablero.posicionRobotX = tablero.posicionRobotX
        tablero.posicionRobotY = tablero.posicionRobotY + 1
        tablero.table[x, y + 1] = 8
        tablero.table[x, y] = 0
    else:
        print("movimineto invalido;el robot permanece quieto")


def moverArriba(tablero):
    posRobotX = tablero.posicionRobotX
    posRobotY = tablero.posicionRobotY
    if tablero.table[posRobotX][posRobotY - 1] == 9:
        return tablero

    if tablero.table[posRobotX][posRobotY - 1] == 7:
        tablero.table[posRobotX][posRobotY - 1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY - 1] == range(1, 6):
        tablero.table[posRobotX][posRobotY - 1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY - 1] == 7:
        tablero.table[posRobotX][posRobotY - 1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero
    if tablero.table[posRobotX][posRobotY - 1] == 0:
        tablero.table[posRobotX][posRobotY - 1] = 8
        tablero.table[posRobotX][posRobotY] = 0
        return tablero


def DistanciaManhatan(tablero:Tablero):
    print("EN CONSTRUCCION")
    

     #la distancia de manjatan nos dice que la distancia entre 2 putnos con coordenadas 
     #siendo p(x,y) y q(r,s) la distancia d se calcula (d(p,q))=raiz( (r-x)^2+(s-y)^2)
     #para nosotros sera la distancia del robot p a la moneda .quedando asi= d(r,m)=raiz(moneda[x]-robotX)^2+(mondeda[y]-robot`[y]^2)
    valor = valor+abs(tablero.posicionRobotX)