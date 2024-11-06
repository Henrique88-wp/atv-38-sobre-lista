#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR
lista =[i for i in range(1,21)]

par = [num for num in lista if num %2 == 0]
impar = [num for num in lista if num % 2 !=0]

print("lista",lista)
print("lista PAR", par)
print("lista impar",impar)