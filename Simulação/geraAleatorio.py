import random

print("Gerador de aleatórios 0-1. Renomeie o arquivo 'aleatorio1.txt' se não quiser que ela seja sobrescrita.")
n = int(input("Número de aleatórios à gerar: "))

file1 = open("aleatorios1.txt","a")

for i in range (0,n):
    file1.write( str(random.random()) + '\n')


