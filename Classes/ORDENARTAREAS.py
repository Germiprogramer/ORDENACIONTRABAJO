class ordenartareas:
  def _init_(tareas):
    tareas = [tareas]
  
  def ordenartareas(tareas):
    for i in range(len(tareas)):
        for r in range(i, len(tareas)):
            if tabla[i]> tabla[r]:
                tabla[i], tabla[r] = tabla[r], tabla[i]
                print(tabla)