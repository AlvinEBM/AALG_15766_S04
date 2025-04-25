def busquedabinaria(lista,buscar):
    inicio=0
    final=len(lista)-1
    while inicio<=final:
        medio=(inicio+final)//2
        if lista[medio]==objetivo:
            return medio
        elif  lista[medio]<objetivo:
                inicio = medio +1
        else:fin=medio-1    
    return -1        