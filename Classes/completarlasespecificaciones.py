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