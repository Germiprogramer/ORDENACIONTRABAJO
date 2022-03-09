class dicotomia:
  def __init__(self, tabla):
    self.tabla = list(tabla)
  
  def dicotomia(self, tabla):
    for i in range(len(self.tabla)):
        for r in range(i, len(self.tabla)):
            if self.tabla[i]> self.tabla[r]:
                self.tabla[i], self.tabla[r] = self.tabla[r], self.tabla[i]
                print(self.tabla)
    return self, tabla

if __name__ == ""__main__"" :
  tabla = [1,2,5,3,2,1,4,7]
  ordenacion = dicotomia(tabla)
  print(ordenacion)
