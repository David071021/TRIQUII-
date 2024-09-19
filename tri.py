tablero =(
    ['#','#','#'],
    ['#','#','#'], 
    ['#','#','#'], 
 )

def imprimir_tablero(tab):
    print('    0 1 2')
    for i, fila in enumerate (tab):
        print(i, end=' | ')
        for colum in  fila:
            print(colum, end=' ')
        print('|',i)
    print('    0 1 2')    

        

    
imprimir_tablero(tablero)    

    