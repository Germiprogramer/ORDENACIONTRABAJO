class Completarlasespecificaciones:
  def __init__(self, tabla):
    self.tabla = list(tabla)
  
  def elegirsegmento(self, max, min):
    max = int(input("elige el límite menor: "))
    min = int(input("elige el límite mayor: "))
    return max, min
  
  def sacarmaximo(self, tabla, max, min):
    for i in range(min, max):
        maximo = tabla[i] 
        if tabla[i] > maximo:
            maximo = tabla[i]
    return maximo
  