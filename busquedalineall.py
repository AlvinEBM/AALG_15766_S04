def busquedalineal(lis,busca):
    global ops
    for x in lis:
        ops +=1
        if x == busca:
            return True
    return False
def busquedabinaria(lis,busca):
    pass
ops=0 
a=[1,3,6,9,4]
print(busquedalineal(a,5),ops)
ops=0
print(busquedalineal(a,1),ops)
