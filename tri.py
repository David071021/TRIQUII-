tablero =(
    ['#','#','#'],
    ['#','#','#'], 
    ['#','#','#'], 
 )

def imprimir_tablero(tab):
    print('    0   1   2')
    for i, fila in enumerate (tab):
        print(i, end=' | ')
        for colum in  fila:
            print(colum, end=' | ')
        print(i)
        if i <2:
            print('  -------------')
    print('    0   1   2')    

imprimir_tablero(tablero)    

    