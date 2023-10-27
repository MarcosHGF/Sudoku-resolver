import random
#main code sudoku resolver
#insert your sudoku in order of lines and use "0" in the blank spaces

#notes:
#sum of all lines and blocks have to be 45


#functions



def create_matriz():#create the sudoku
    #9x9
    matriz = []
    for i in range(9):
        linha = []
        #for j in range(9):
        value = str(input(f"{1+i}: digite em ordem de linha: "))
        #value = random.randint(1,9)
        linha = [int(i) for i in value]
        #print(f"{linha}\n")            
        matriz.append(linha)
    return matriz


def find_in_list(list, value):
    if(value in list):
        return 0
    else:
        return value


def find_values(matriz):#look all lists to find the missing numbers
    missingmatriz = []
    for lists in matriz:
        missinglist = []
        for values in lists:
            x = find_in_list(lists,values)
            missinglist.append(x)
        missingmatriz.append(missinglist)    
    return missingmatriz


matriz = create_matriz()
missing = find_values(matriz)


for list in matriz:
    print(f"{list}\n")

print("-------------------------------------")

for list in missing:
    print(f"{list}\n")

'''
resolvido:
493567182
812439657
657218439
326951874
178324965
945874213
569782341
231645798
784193526

403507080
002009007
050018009
300050004
000000000
900070003
500780040
200600700
080103506


matriztest =([4,0,3,5,0,7,0,8,0],
             [0,0,2,0,0,9,0,0,7],
             [0,5,0,0,1,8,0,0,9],
             [3,0,0,0,5,0,0,0,4],
             [0,0,0,0,0,0,0,0,0],
             [9,0,0,0,7,0,0,0,3],
             [5,0,0,7,8,0,0,4,0],
             [2,0,0,6,0,0,7,0,0],
             [0,8,0,1,0,3,5,0,6])

'''