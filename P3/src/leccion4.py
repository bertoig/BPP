# Author: Humberto A. Iglesias González
# El programa consiste en la creacion de una clase Calculadora
# con sus respectivos métodos y un mini-código de prueba
# de dicha clase que muestra su uso.


class calculadora:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def getX(self):
        return self.x 
    
    def getY(self):
        return self.y 

    def setX(self, x):
        self.x=x 
    
    def setY(self, y):
        self.y=y

    def sumar(self):
        return self.x+self.y
    
    def restar(self):
        return self.x-self.y

    def multiplicar(self):
        return self.x*self.y

    def dividir(self):
        return self.x/self.y
    
print("Bienvenido al programa de prueba de la calculadora.\n")
print("Para iniciar la calculadora necesitamos dos números. \n")

a=int(input("Introduce el primer numero: "))
b=int(input("Introduce el segundo numero: "))

c=calculadora(a,b)

n=-1

while(n!=0):
    print("Puedes realizar las siguientes tareas:\n")
    print("0- Salir")
    print("1- Cambiar el primer numero")
    print("2- Cambiar el segundo numero")
    print("3- Sumar ambos numeros")
    print("4- Restar ambos numeros")
    print("5- Multiplicar ambos numeros")
    print("6- Dividir ambos numeros")
    print("7- Mostrar los numeros actuales")

    n=int(input("Introduzca la opcion: "))

    if(n==1):
        a=int(input("\nIntroduce el primer numero: "))
        c.setX(a)
        print("\n")
    elif (n==2):
        b=int(input("\nIntroduce el segundo numero: "))
        c.setY(b)
        print("\n")
    elif (n==3):
        print("\nEl resultado de la suma es: ", c.sumar(), "\n")
    elif (n==4):
        print("\nEl resultado de la resta es: ", c.restar(), "\n")
    elif (n==5):
        print("\nEl resultado de la multiplicacion es: ", c.multiplicar(), "\n")
    elif(n==6):
        print("\nEl resultado de la division es: ", c.dividir(), "\n")
    elif(n==0):
        print("\nSaliendo de la calculadora\n")
    elif(n==7):
        print("\n Los numeros actuales son: ", c.getX(), " y ", c.getY(), "\n")
    else:
        print("\nDebes introducir un numero de los mostrados.\n")