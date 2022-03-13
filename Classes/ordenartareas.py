class Ordenartareas:
  def _init_(self, tareas):
    self.tareas = list(tareas)
  
  def ordenacion(self,tareas):
        for i in range(len(self.tareas)-1):
            for a in range(len(self.tareas)-1):
                if self.tareas[a] > self.tareas[a+1]:
                    self.tareas[a], self.tareas[a+1] = self.tareas[a+1], self.tareas[a]
        return self.tareas