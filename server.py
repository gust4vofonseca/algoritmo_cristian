import socket
import datetime

def startTimeServer():
 
    sock = socket.socket()

    port = 8000
 
    sock.bind(('', port))
      
    sock.listen(5)     
    print("Esperando conexao...")
       
    while True:
       
       connection, address = sock.accept()     
       print('Servidor conectado a: ', address)
       
       connection.send(str(datetime.datetime.now()).encode())
       
       connection.close()
 
 
if __name__ == '__main__':
 
    startTimeServer()