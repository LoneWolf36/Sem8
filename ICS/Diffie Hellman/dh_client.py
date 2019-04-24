import socket
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_IP = '127.0.0.1'
PORT = 1234

p = 23
g = 5

# R1 = g^private_number % p

private_number = random.randint(1, p)
public_client = (g**private_number) % p

client.connect((HOST_IP, PORT))
msg = client.recv(2048)
print(msg.decode())

print('Modulus : ', p, ' sent to server')
print('Base : ', g, ' sent to server')

print('Private number belonging to client: ', private_number)
print('Public Client Key : ', public_client, ' sent to server')

msg = ','.join([str(p), str(g), str(public_client)])
client.send(msg.encode())

# Received R2
public_server = int(client.recv(1024).decode())
print('Public Server Key : ', public_server, 'received from server')

# k = R2^private_number % p
key = (public_server**private_number) % p
print('Key : ', key)
client.close()
