import socket
import datetime
import os
from dateutil import parser
from timeit import default_timer as timer
import time

def serverTimeSynchronization():
 
    server_address = ('192.168.131.130', 8000)         

    # Cria um objeto socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta-se ao servidor
    print('Conectando-se a', server_address)
    sock.connect(server_address)

    #Horario que foi enviado a requisicao
    request_time = timer()
    print('Requisicao feita:', request_time)

    # Envia a mensagem de solicitação de hora para o servidor
    server_time = parser.parse(sock.recv(1024).decode())
    print('Horario do servidor: ', server_time)
    
    #Horario de resposta do servidor
    response_time = timer()
    print('Resposta recebida:', response_time)

    #Calculo da latencia 
    latencia = response_time - request_time
    print('Latencia: ', latencia)

    #Ajustanto o tempo do servidor com a latencia
    server_time_latencia = server_time + datetime.timedelta(seconds = (latencia) / 2)
    print('Hora do servidor corrigida com a latencia: ',server_time_latencia)

    #Horario atual do cliente
    actualTime = datetime.datetime.now()
    print('Horario atual do cliente: ', actualTime)

    #Diferenca entre horario do servidor e cliente
    delta_t = server_time_latencia - actualTime

    #segundos de diferenca
    secondosDiferenca = delta_t.total_seconds()
    print('Diferenca de tempo: ', secondosDiferenca)

    # Altera o horário do cliente (Ubuntu)
    while secondosDiferenca >= 1:
        actualTime2 = datetime.datetime.now()

        hour = actualTime2.hour
        minute = actualTime2.minute
        second = actualTime2.second + 1

        if second == 60:
            second = 00
            minute += 1
        if minute == 60:
            minute = 00
            hour += 1
        
        os.system('sudo date -s {}:{}:{}'.format(hour, minute, second))
        secondosDiferenca -= 1
        time.sleep(10)
        
    while secondosDiferenca <= -1:
        actualTime2 = datetime.datetime.now()

        hour = actualTime2.hour
        minute = actualTime2.minute
        second = actualTime2.second - 1

        if second == -1:
            second = 59
            minute -= 1
        if minute ==-1:
            minute = 59
            hour -= 1
        
        os.system('sudo date -s {}:{}:{}'.format(hour, minute, second))
        secondosDiferenca += 1
        time.sleep(10)

    print('Sincronizacao finalizada')

    # Encerra a conexão
    sock.close()
 
if __name__ == '__main__':
 
    serverTimeSynchronization()