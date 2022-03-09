class ordenartareas:
  def _init_(self, tareas):
    self.tareas = list(tareas)
  
  def ordenartareas(tareas):
    for i in range(len(tareas)):
        for r in range(i, len(tareas)):
            if tabla[i]> tabla[r]:
                tabla[i], tabla[r] = tabla[r], tabla[i]
                print(tabla)