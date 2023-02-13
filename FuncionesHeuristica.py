import numpy as np
import math
import copy
def localizarObjetivo(tablero, num):
    for x, y in zip(*np.where(tablero == num)):
        print("El elemento buscado[{}, {}] vale {}".format(x, y, tablero[x, y]))
        break
    return x, y


class Tablero:
    """esta es la clase tablero que almacenara toda la infomracion del juego"""

   
    def __init__(self, monedasNecesarias = None, posicionRobotX = None, posicionRobotY = None, table = None, salida = None
                ,coordMonedas = None, h = 0, movimientosRealizados: list = None):
        if not monedasNecesarias:
            return None
        self.monedasNecesarias = monedasNecesarias
        self.posicionRobotX = posicionRobotX
        self.posicionRobotY = posicionRobotY
        self.table = table
        self.h = h
        self.movimientosRealizados = movimientosRealizados



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
    return tablero.table[x, y] != 9


def hayMoneda(tablero: Tablero, x, y):
    if tablero.table[x, y] < 7:
        valorMoneda = tablero.table[x, y]
        m = True
        return (m, valorMoneda)
    else:
        m = False
        return m


def move_up(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x - 1, y)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX - 1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY
    nuevoEstado.table[x - 1, y] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("A")
    return nuevoEstado

def move_down(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x + 1, y)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX + 1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY
    nuevoEstado.table[x + 1, y] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("B")
    return nuevoEstado

def move_left(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x , y- 1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX 
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY - 1
    nuevoEstado.table[x , y - 1] = 8
    nuevoEstado.table[x, y ] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("I")
    return nuevoEstado

def move_right(tablero: Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x , y+1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX 
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("D")
    return nuevoEstado
        

def  diag_upRight(tablero:Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x-1, y+1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX -1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x-1 , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("AD")
    return nuevoEstado


def  diag_upLeft(tablero:Tablero):
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x-1, y-1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX -1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY -1
    nuevoEstado.table[x-1 , y -1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("AI")
    return nuevoEstado


def  diag_downRight(tablero:Tablero): 
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x+1, y+1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX +1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY + 1
    nuevoEstado.table[x+1 , y +1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("BD")
    return nuevoEstado  

def  diag_downLeft(tablero:Tablero):   
    nuevoEstado = copy.deepcopy(tablero)
    
    x = nuevoEstado.posicionRobotX
    y = nuevoEstado.posicionRobotY


   
    exisMoneda, valorMoneda = hayMoneda(nuevoEstado, x+1, y-1)
    if (exisMoneda ):  # monedas de 0 almacena true o false para saber si hay moneda en la casilla que nos movemos
            nuevoEstado.monedasRecogidas = ( nuevoEstado.monedasRecogidas + valorMoneda )  # modenas[1] almacena el valor

    nuevoEstado.posicionRobotX =nuevoEstado.posicionRobotX +1
    nuevoEstado.posicionRobotY =nuevoEstado.posicionRobotY -1 
    nuevoEstado.table[x+1 , y -1] = 8
    nuevoEstado.table[x, y] = 0
    nuevoEstado.h = DistanciaManhatan(nuevoEstado)
    nuevoEstado.movimientosRealizados.append("BI")
    return nuevoEstado



def DistanciaManhatan(tablero:Tablero):
     #la distancia de manjatan nos dice que la distancia entre 2 putnos con coordenadas 
     #siendo p(x,y) y q(r,s) la distancia d se calcula (d(p,q))=raiz( (r-x)^2+(s-y)^2)
     #para nosotros sera la distancia del robot p a la moneda .quedando asi= d(r,m)=raiz(moneda[x]-robotX)^2+(mondeda[y]-robot`[y]^2)
     
    heuristica = 0
     
    posRobot = [tablero.posicionRobotX , tablero.posicionRobotY]
    for moneda in tablero.coordMonedas:
        valorX = moneda[0] - posRobot[0]
        valorY = moneda[1] - posRobot[1]
        heuristica = heuristica + abs(math.pow(valorX, 2) + math.pow(valorY, 2))
    return heuristica


def hemosTerminado (tablero: Tablero):
    if (tablero.posicionRobotX == tablero.salida[0] and tablero.posicionRobotY == tablero.salida[1]):
        return True
    else:
        return False
