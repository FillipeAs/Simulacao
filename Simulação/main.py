import random
from queue import Queue
import time
import string


# Parâmetros Globais
servQuant = 1 # Quantidade de servidores
capacidade = 5 # Capacidade
cheg = (2,4) # Chegada
aten = (3,5) # Atendimento
T = 3 # Tempo inicial

# Inicialização da fila
queue = Queue(maxsize = capacidade)

#Abre arquivo com Aleatórios
file1 = open("aleatorios1.txt","r")
rands = []

#Temporização
tPresente = 0.0



def sorteio(a, b): #pega um aleatório da lista invés de gerar um novo cada vez
	rand = (b-a) * rands.pop(0) + a   #random.random() + a
	return rand


def saida(T):
	# Contabiliza o tempo
	tSaida = time.time() - tPresente
	tPresente = time.time()
	
	# Remove requisição da fila
	queue.get() 
	
	#Imprime o estado da fila
	#print("EVENTO - ESTADO - TEMPO")
	print("Chegada	" + len(queue)+ "	" + tSaida)

	if queue.size() >= servQuant: # Se maior ou igual ao número de servidores
		saida(T + sorteio(aten[0], aten[1]))



def chegada(T):
	# Contabiliza o tempo.
	tChegada = time.time() - tPresente
	tPresente = time.time()


	if not queue.full(): # Se a fila não está cheia
		queue.put(1) # Adiciona a requisição na fila

		#Imprime o estado da fila
		#print("EVENTO - ESTADO - TEMPO")
		print("Chegada	" + len(queue)+ "	" + tChegada)

		if queue.qsize() <= servQuant: # Se menor ou igual ao número de servidores
			saida(T + sorteio(aten[0], aten[1]))
	
	chegada(T + sorteio(cheg[0], cheg[1]))



if __name__ == "__main__":
	print("Simulador de fila de atendimento. Parâmetros padrão G/G/1/5, tempo de chegada 2..4, tempo de atendimento 3..5, tempo de chegada do primeiro em 3s.")
	if "s" == input("Alterar parâmetros? s/n: "):
		servQuant = int(input("Quantidade de servidores: ")) 
		capacidade = int(input("capacidade: ")) 
		c =  string.split( input("Chegada. Ex 2-7: "), "-")
		cheg = (int(c[0]), int(c[1]))
		a =  string.split( input("Atendimento. Ex 5-13: "), "-")
		aten = (int(a[0]), int(a[1]))
		T = int(input("Tempo inicial: "))
	
	#inicializa a lista de aleatórios com o conteúdo do arquivo
	lines = file1.readlines()
	for i in range(0, len(lines)):
		rands += [float(lines[i])]

	#Cabeçalho da exibição da simulação
	print("EVENTO - ESTADO - TEMPO")
	print("  -		0		0.0000")

	#inicia simulação
		#time.time() - tPresente retorna um float de quantos segundos se passaram entre a atribuição do tempo atual para tPresente e o tempo atual retornado por time.time()
		#rands.pop(0) retorna o primeiro elemento da lista de aleatórios e remove ele da lista. Quando ela estiver vazia, encerra simulação.
	tPresente = time.time()
	while len(rands)>0:
		if T < time.time() - tPresente: #Se já passou o tempo inicial, inicia a simulação
			chegada(T) #+ sorteio(cheg[0], cheg[1]))

