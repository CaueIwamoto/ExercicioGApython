//Exercício 1
matriz = []

print("DETERMINANTE:\n")
ordem = int(input("Digite a ordem da matriz (até ordem 3): "))

for n_linhas in range (ordem):
    linha = []
    for n_colunas in range (ordem):
        linha.append (int(input("Digite o elemento {0} {1} da matriz: ".format 
        (n_linhas+1,n_colunas+1) )))
    matriz.append(linha)

if ordem == 1:
    determinante = matriz[0][0];
elif ordem == 2:
    determinante = (matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0])
elif ordem == 3:
    determinante = (matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[1][0]*matriz[2][1]*matriz[0][2]
    + matriz[0][1]*matriz[1][2]*matriz[2][0] - matriz[0][2]*matriz[1][1]*matriz[2][0]
    - matriz[1][2]*matriz[2][1]*matriz[0][0] - matriz[0][1]*matriz[1][0]*matriz[2][2])

if ordem == 1 and matriz[0][0] == 2:
    print("Determinante:  %.1f" %determinante)
else:
    print("Determinante: %.1f" %determinante)
    

//Exercício 2
matriz = []

linhas = int(input("Digite o número de linhas  da matriz M: "))
colunas = int(input("Digite o número de colunas da matriz M: "))

for n_linhas in range (linhas):
    linha = []
    for n_colunas in range (colunas):
        linha.append (int(input("Digite o elemento {0} {1} da matriz: ".format (n_linhas+1,n_colunas+1) )))
    matriz.append(linha)

print("MATRIZ")
for n_linhas in range (linhas):
    for n_colunas in range (colunas):
        print("{0}.0 ".format (matriz[n_linhas][n_colunas]), end="")
    print("")

print("\nMATRIZ TRANSPOSTA:")
for n_colunas in range (colunas):
    for n_linhas in range (linhas):
        print("{0}.0 ".format (matriz[n_linhas][n_colunas]), end="")
    print("")
