#Exercícios no moodle. Três são cálculos (não no algoritmo) e um é em python.
#Feito no dia 8/04/2022

#Exercício 1
from math import sqrt

print("Produto Vetorial - Área:");
v = []
u = []

print("Coordenadas do vetor u:")

for i in range(3):
    print(f"Digite a {i+1}a. coordenada:",end=" ")
    u.append(int(input()))
        
        

print("Coordenadas do vetor v:")

for i in range(3):
    print(f"Digite a {i+1}a. coordenada:",end=" ")
    v.append(int(input()))
    

i = 1*u[1]*v[2]-(1*u[2]*v[1])
j = 1*u[2]*v[0]-(1*u[0]*v[2])
k = 1*u[0]*v[1]-(1*u[1]*v[0])

area = sqrt(i*i+j*j+k*k)

print("A área do paralelogramo formada pelos vetores u e v é: %.2f" % round(area,2))

#Exercício 2
#Resposta da 2: 
Xe = (-3,1,12)

#Exercício 3
#Resposta da 3:
v = (1, raiz de 2, 1)

#Exercício 4
x = (2p, p, -3)
y = (2,0,1)
z = (0,-1,-1)
#Resposta 4:
p = -3/2
