import socket
import math
import matplotlib.pyplot as plt

def plotter(string,result):
		plt.plot(result, result, color = 'red', marker = "o")  
		plt.title(string)  
		plt.xlabel("X")  
		plt.ylabel("Y")
		plt.show()

serverSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #1_ipv4 2_TCP
serverSocket.bind((socket.gethostname(), 5981)) #binding IP and port
serverSocket.listen(100) #QUEUE
print("Conneciton Started")
clientSocket , address = serverSocket.accept()
print(f"connection from {address} is OK")
clientSocket.send(  bytes("\nWELCOME TO SERVER" , "utf-8")  ) #sent to client
while True:

	Data = clientSocket.recv(1024).decode()	
	Data = Data.split('$')					#$operator$op1$op2$

	operator = Data[1]
	first_oprand = int(Data[2])
	if Data[3] != '' :
		print("NOT FOR SIN-COS-COT-TAN")
		second_oprand = int(Data[3])
	
	if operator == 'ADD' :	
		result = first_oprand + second_oprand
		clientSocket.send(  bytes(f" {first_oprand} + {second_oprand} = " , "utf-8")  )
	elif operator == 'SUB' :
		result = first_oprand - second_oprand
		clientSocket.send(  bytes(f" {first_oprand} - {second_oprand} = " , "utf-8")  )
	elif operator == 'DEVIDE':
		result = first_oprand / second_oprand
		clientSocket.send(  bytes(f" {first_oprand} / {second_oprand} = " , "utf-8")  )
	elif operator == 'MULTIPY':
		result = first_oprand * second_oprand
		clientSocket.send(  bytes(f" {first_oprand} * {second_oprand} = " , "utf-8")  )
	elif operator == 'SIN':
		result = math.sin(first_oprand)
		clientSocket.send(  bytes(f" sin {first_oprand} =  " , "utf-8")  )	
		plotter("SIN",result)
	elif operator == 'COS':
		result = math.cos(first_oprand)
		clientSocket.send(  bytes(f" cos {first_oprand} =  " , "utf-8")  )
		plotter("COS",result)		
	elif operator == 'TAN':
		result = math.tan(first_oprand)
		clientSocket.send(  bytes(f" tan {first_oprand} =  " , "utf-8")  )
		plotter("TAN",result)
	elif operator == 'COT':
		result = (1/math.tan(first_oprand))
		clientSocket.send(  bytes(f" cot {first_oprand} =  " , "utf-8")  )
		plotter("COT",result)
	result = str(result)
	clientSocket.send(result.encode())
	


	



	