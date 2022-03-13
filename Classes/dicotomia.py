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
