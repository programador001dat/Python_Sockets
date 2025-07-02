import socket
import threading

def ClientSocket(client):	# ESCOPO, vai ser obrigatorio para criar o objeto socket,
	while True:		# e enviar.
		try:

			data = client.recv(1024).decode()   # Receberemos as mensagens do servidor aqui.
			if data:
				print(f'(!) recebido do servidor:\t {data} \n')
			else:
				break

		except Exception as err:	# não foi possivel estabelecer conexao, pare !
			print('=> first error: ', err)
			break


def main():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ESCOPO. !
	try:
		client.connect(('192.168.15.5', 5000))	# Conectado ao endereço
		print('(+) connection... \n')


	except Exception as err: # pipe broken, passe o erro.
		print('Second error: ', err)
		pass

	threading.Thread(target=ClientSocket, args=(client,), daemon=True).start()
	 # Faça tarefa simultaneamente na CPU.

	while True:
		try:

			chat = str(input('[enviar]: '))
			client.send(chat.encode()) # Use o escopo.

		except Exception as err:
			print(f'Third error: ', err)
			break

	client.close()

if __name__ == '__main__':
	main()

