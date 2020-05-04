import socket



ClinetSocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  #1_ipv4 2_TCP
ClinetSocket.connect((socket.gethostname(), 5981))				   #binding IP and port
welcome_msg = ClinetSocket.recv(1024)	
print(welcome_msg.decode("utf-8"))

while True:
	print('operators: ADD  , SUB , DEVIDE , MULTIPY , COT , TAN , SIN , COS')
	print("To use  Calculator , input like :  ")
	print("FOR ADD,SUB,DEVIDE,MULTIPY : $operator$op1$op2$ ex: $ADD$123$2$ \nFOR TAN,COT,SIN,COS : $operator$op1$ ex: $SIN$120$")
	request = input()
	ClinetSocket.send(request.encode())
	finish_msg = ClinetSocket.recv(1024)
	print(finish_msg.decode("utf-8"))
	Data = ClinetSocket.recv(1024).decode()
	print(Data)

	if 'exit' == input('Type "exit" to exit or press ENTER to continue'):
		ClinetSocket.close()
		exit()


