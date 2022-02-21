#ejercicio 1
planetas=['neptuno','venus','tierra','marte','jupiter','saturno','urano','neptuno']
NOplanetas=len(planetas)
print("el numero de planetas es", NOplanetas, "y estos son")
x=0
for x in range (0,NOplanetas):
    print(planetas[x])

planetas.append('pluton')
NOplanetas=len(planetas)
print("\n\n ahora el numero de planetas es ", NOplanetas, "y estos son")
x=0
for x in range (0,NOplanetas):
    print(planetas[x])
    

#ejercicio2
planetas.pop()
p=str(input("escribe un planeta    ")) 
planetas_index=planetas.index(p)
print("los planetas mas cercanos al sol que el ingresado",p, "son")
print(planetas[0:planetas_index])
print("los planetas mas lejanos al sol que el ingresado",p, "son")
print(planetas[planetas_index+1:])