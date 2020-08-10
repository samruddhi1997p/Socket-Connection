from socket import socket, AF_INET, SOCK_STREAM
s=socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 6157))
s.getsockname()
server= ('127.0.0.1', 8888)
s.connect(server)
data= s.recv(1024)
print (data.decode())
s.send(b"HELLO prabhulkar.s\n")


def fword(word1, num1):
	while True:
		if (word1=="MATH"):
			d1,operation,d2 = num1.split(" ")
			d1=int(d1)
			d2=int(d2)
			maths(operation, d1, d2)
			return;
		elif (word1=="DONE"):
			print("DONE")	
			return;
			


def maths(operation, d1, d2):
		if (operation == '/'):
			answer= d1/d2;
			info= b"ANSWER "+ str(answer) + b"\n"
			print(info);
			s.send(info)
			return;
	 	
		elif (operation =='*'):
			answer= d1*d2;
			info= b"ANSWER " + str(answer) + b"\n"
			print(info);
			s.send(info)
			
			return;

		elif (operation=='+'):
			answer= d1+d2;
			info= b"ANSWER " + str(answer) + b"\n"
			print(info);
			s.send(info)
			return;

		elif (operation=='-'):
			answer= d1-d2;
			info= b"ANSWER " + str(answer) + b"\n"
			print(info);
			s.send(info)
			return;

while True:
	answ= s.recv(2024)
	print(answ.decode())
	answ= answ.decode()
	if 'DONE' in answ:
		break
	word1, num1= answ.split(" ",1)
	fword(word1, num1)



s.close()


