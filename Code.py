#main code sudoku resolver
#insert your sudoku in order of lines and use "0" in the blank spaces

#functions
def create_matriz():
    #9x9
    matriz = []
    for i in range(9):
        linha = []
        for j in range(9):
            value = input("digite em ordem de linha: ")
            linha.append(value)
            linha[j]
        print(f"{linha}\n")            
        matriz += linha
    return matriz


'''
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")
line4 = input("line 4:")
line5 = input("line 5:")
line6 = input("line 6:")
line7 = input("line 7:")
line8 = input("line 8:")
line9 = input("line 9:")
'''

'''
resolvido:
193567128
812439657
657218439
326951874
178324965
945874213
569782341
231645798
784193526
'''

matriz =([4,0,3,5,0,7,0,8,0],
         [0,0,2,0,0,9,0,0,7],
         [0,5,0,0,1,8,0,0,9],
         [3,0,0,0,5,0,0,0,4],
         [0,0,0,0,0,0,0,0,0],
         [9,0,0,0,7,0,0,0,3],
         [5,0,0,7,8,0,0,4,0],
         [2,0,0,6,0,0,7,0,0],
         [0,8,0,1,0,3,5,0,6])
 

dict = {"0": " "}

matriz = create_matriz()


for list in matriz:
    print(f"{list}\n")



