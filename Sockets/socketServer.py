import socket
import threading

def ServerSocket(connection): # escopo, vai ser usado para enviar a msg ao cliente na linha 34
	while True:
		try:

			data = connection.recv(1024) # ESCOPO receber dados
			if data:
				print(f'(!) recebido do cliente:\t {data.decode()} \n')
			else:
				break

		except Exception as err:
#			print('=> first error: ', err)
			break

def main():

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# IPv4/TCP
	sock.bind(('192.168.15.5', 5000))	# VINGULAR
	sock.listen(1)		# OUVIR
	print(f'(?) aguardando por conexões... \n')

	connection, addr = sock.accept()	# ESCOPO, RECEBE A CONEXÃO. E addr QUEM É?
	print(f'(!) Connection With: {addr} \n')

	threading.Thread(target=ServerSocket, args=(connection,), daemon=True).start()
	# FACA UMA TAREFA SIMULTANEA NA CPU.

	while True:
		try:

			chat = str(input('[enviar]: '))
			connection.send(chat.encode())	# ESCOPO

		except Exception as err:
			print(f'second error: ', err)
			pass


if __name__ == '__main__':
	main()
