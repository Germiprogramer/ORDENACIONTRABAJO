# ORDENACIONTRABAJO

La direccion github a este repositorio es la siguiente: https://github.com/Germiprogramer/ORDENACIONTRABAJO.git

Se han realizado los ejercicios de ordenacion propuestos.

# Main
    if __name__ == "__main__":
      from Classes.dicotomia import *
      print("Ejercicio 1")
      tabla = [1,2,5,3,2,1,4,7]
      tablaordenada = Dicotomia(tabla)
      print(tablaordenada)

      print("Ejercicio 2")
      from Classes.ordenartareas import *
      tabladetareas = [1,2,5,3,2,1,4,7]
      tareasordenadas = Ordenartareas(tabladetareas)

      print("Ejercicio 3")
      from introducir.entero import *
      from Classes.completarlasespecificaciones import *
      tabla = [1,2,5,3,2,1,4,7]
      max = MAX
      min = MIN

      tablanueva = Completarlasespecificaciones(tabla)
      print(tablanueva)
      
# Ejercicio 1
     class Dicotomia:

      def __init__(self, tabla):
        self.tabla = list(tabla)

      def ordenacion(self, tabla):
        for i in range(len(self.tabla)):
            for r in range(i, len(self.tabla)):
                if self.tabla[i]> self.tabla[r]:
                    self.tabla[i], self.tabla[r] = self.tabla[r], self.tabla[i]
                    print(self.tabla)
        return self, tabla
      
# Ejercicio 2
    class Ordenartareas:
      def _init_(self, tareas):
        self.tareas = list(tareas)

      def ordenacion(self,tareas):
            for i in range(len(self.tareas)-1):
                for a in range(len(self.tareas)-1):
                    if self.tareas[a] > self.tareas[a+1]:
                        self.tareas[a], self.tareas[a+1] = self.tareas[a+1], self.tareas[a]
            return self.tareas
            
# Ejercicio 3
    class Completarlasespecificaciones:
      def __init__(self, tabla):
        self.tabla = list(tabla)

      def elegirsegmento(self, max, min):
        max = int(input("elige el límite menor: "))
        min = int(input("elige el límite mayor: "))
        return max, min

      def sacarmaximo(self, tabla, max, min):
        for i in range(min, max):
            maximo = self.tabla[i] 
            if self.tabla[i] > maximo:
                maximo = self.tabla[i]
        return self.maximo

      def moveralaizquierda(self, tabla, max, min):
        for i in range(min, (max-1)):
          self.tabla[i] = self.tabla[i+1]
        return self.tabla
 

Nota = debe haber un problema a la hora de ejecutar el código.
