import numpy as np


def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento buscado[{}, {}] vale {}".format(x, y, tablero[x, y]))
        break
    return x, y


class Tablero:
    """esta es la clase tablero que almacenara toda la infomracion del juego"""

    def __init__(self, monedas, posicionRobotX, posicionRobotY, table):
        if not monedas:
            return None
        self.monedas = monedas
        self.posicionRobotX = posicionRobotX
        self.posicionRobotY = posicionRobotY
        self.table = table

        # agregado
        self.monedasRecogidas = 0

    def __str__(self) -> str:
        return f"Numero de monedas:{self.monedas} en el tablero\n {self.table}\n posicion del robot:{self.posicionRobotX,self.posicionRobotY}\n el numero de monedas recogidas actualmente es {self.monedasRecogidas}"


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
