


def cargarArchivo():
    fichero = input("Inserte la ruta del fichero a resolver")
    fp=open(fichero, 'r')
    lines = fp.readlines().remove()
    tablero = []
    for linea in lines:
        tablero.append(linea.split(","))

    #datos =''.join(f.readlines()).replace('\n',';')
    #tablero = 
    fp.close()

   








#Source: https://stackoverflow.com/questions/510049





def main():
    print("LABECOIN")
    cargarArchivo()


    # Source: https://stackoverflow.com/questions/47432043

    print("¿Con que algoritmo quieres resolver el puzzle?")
    opcion = input("1-Escalada simple. \n 2-Maxima pendiente \n")

    match opcion:
        case 1:
            escaladaSimple()
        case 2:
            print("Aqui falta Maxima pendiente")


main()
