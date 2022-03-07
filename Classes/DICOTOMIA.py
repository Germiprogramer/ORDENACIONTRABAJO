class dicotomia:
  def dicotomia(tabla):
    for i in range(len(tabla)):
        for r in range(i, len(tabla)):
            if tabla[i]> tabla[r]:
                tabla[i], tabla[r] = tabla[r], tabla[i]
                print(tabla)
    return tabla

