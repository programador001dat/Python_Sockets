TCP(Transmission Controll Protocol)
   É uma camada de tranporte mais segura e garante um conexão dos dois lados, mais lento e seguro.

UDP(User Datagram Protocol)
   Não garante um conexao continua, não garante a entrega dos pacote, não garante o tempo de resposta,
   mais rapido, menos seguro.

Sockets com python, sockets são a comunicão continua ou não.(TCP ou UDP).
Com sockets TCP você consegui estabeler uma conexão entre duas aplicação ou dois processos conectado.
Com sockets UDP você consegui enviar dados, e não garante conexão continua.

requisitos:
   . sockets
   . threading

Biblioteca:
   Threading é uma processo(função) que será executado pelo seu Hardware, CPU eu tenho uma tarefa para você,
   pare oque está fazendo e execute isso primeiro.
   Thread, okay toma CPU, manda para o processador, separa os nucles em tarefa importante e realiza primeiro.

Instalacao:
   pip install threading
   pip install sockets


Conclusão:
   Nosso programa Socket, e um Socket TCP que garante um chat dos dois lados, continuo.
