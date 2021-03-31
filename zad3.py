def foo(lista, mandaty, prog):
    j = 0
    tab = []
    for komitet in lista:
        p = komitet / sum(lista)

        if (p > prog):
                         
            for i in range(1, mandaty + 1):
                tab.append((j, komitet / i))
        j += 1
 
    l = len(tab)
    for i in range(0, l):
        for j in range(0, l-1):
            a = tab[j]
            b = tab[j+1]
            if(a[1]< b[1]):
                tab[j] = b
                tab[j+1] = a
    for i in range(0, len(lista)):
        count = 0
        for j in range(0,mandaty):
            if(tab[j][0] == i):
                count += 1
            
        print (f'Komitet: {i + 1} Liczba glosow: {count}')


lista = [50, 100, 110, 23, 40, 60]
mandaty = 10
prog = 0.2
foo(lista,mandaty,prog)
