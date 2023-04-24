
import random

# Versión modificada de como se imprime la cantidad de zombies |ACTIVIDAD 2|
def mostrar(zombies): 
  print("----------------")
  print(" S:",zombies[0]," E:",zombies[1])
  print(" M:",zombies[2]," I:",zombies[3])
  print("----------------")
 

print("--Creando los zombies en las ciudades--")

# solicitamos al usuario ingresar la cantidad de zombies en cada ciudad |ACTIVIDAD 1|
numero_sabaneta = int(input("--Ingrese la cantidad de zombies para Sabaneta:"))
numero_envigado = int(input("--Ingrese la cantidad de zombies para Envigado:"))
numero_medellin = int(input("--Ingrese la cantidad de zombies para Medellín:"))
numero_itagui = int(input("--Ingrese la cantidad de zombies para Itagüí:"))

# zombies en Sabaneta, Envigado, Medellín, e Itagüí respectivamente
zombies = [numero_sabaneta,numero_envigado,numero_medellin, numero_itagui]

contadorCiclos = 0 # Inicializamos un contador de ciclos en 0 para la funcion de revivir zombies


def disparar(zombies):
  posicionADisparar = int(input("Ingrese la posición de la ciudad a disparar (0, 1, 2 ó 3): "))
  zombies[posicionADisparar] = zombies[posicionADisparar]-10
  # En la siguiente linea haremos que la cantidad de zombies se iguale a cero en dado caso de que el valor sea negativo |ACTIVIDAD 3|
  if zombies[posicionADisparar] < 0:
    zombies[posicionADisparar] = 0
    
    
def granada(zombies): # |ACTIVIDAD 4|
  posicionALanzarGranda = int(input("Ingrese la posición de la ciudad a la cual se lanzara la granda (0, 1, 2 ó 3): "))
  zombies[posicionALanzarGranda] = int(zombies[posicionALanzarGranda]/2) # al hacer la división entre 2, se va a imprimir un entero
  

def revivir(zombies): #|ACTIVIDAD 5| Rosa de Guadalupe |
  ciudad = random.randint(0,3) # El metodo randint genera un numero aleatorio entre dos valores dados e incluyendo sus limites "0" "3", que serian las posiciones de las ciudades
  zombies[ciudad] += 10 # Se reviven 10 zombies en la ciudad seleccionada 
  print("¡Ha pasado una ventisca que ha revivido 10 zombies en la ciudad ",ciudad,"!")
  
def lluviaAcida(zombies): #|ACTIVIDAD 6| Lluvia acida concentrada |
   posicionAEliminar = int(input("Ingrese la posición de la ciudad a la cual se lanzara lluvia acida (0, 1, 2 ó 3): "))
   zombies[posicionAEliminar] = 0


  

while(True):
  mostrar(zombies)
  
  #|ACTIVIDAD 7| Terminar juego |
  totalZombies = sum(zombies) #Suma todos los zombies que hay en la ciudad
  if totalZombies == 0: #Si no hay zombies en ninguna ciudad se rompe el ciclo
    print("Felicitaciones salvaste el Valle de Aburrá")
    break
  
  
  print("--------------Ingrese el digito 1 para:--------------")
  print("- para disparar a zombies de una ciudad particular (Esto matara 10 zombies)")
  print("--------------Ingrese el digito 2 para:--------------")
  print("- para lanzar granada a zombies de una ciudad particular(La granada matara la mitad de zombies de la ciudad)")
  print("--------------Ingrese el digito 3 para:--------------")
  print("- para lanzar lluvia acida(Matara a todos los zombies existentes)")
 
  
  accion = int(input())
  if(accion == 1):
    disparar(zombies)
   
  elif(accion == 2):
    granada(zombies)
    
  elif(accion == 3):
    lluviaAcida(zombies)
  
  contadorCiclos += 1 # Se incrementa 1 en el contador cada vez que ejecutamos el ciclo
  
  # Condicion que pregunta si el contador de ciclos esta en 3 entonces ejecute la funcion revivir y luego se reinicie el contador de ciclos
  if contadorCiclos == 2:
        revivir(zombies)
        contadorCiclos = 0
    
    

    
    
    
