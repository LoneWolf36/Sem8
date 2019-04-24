import random
import socket

server = socket.socket()
PORT = 1234
server.bind(('', PORT))
server.listen(5)
print('Server Started....')
conn, client_address = server.accept()
conn.send('Welcome to Diffi-Hellman Server'.encode())
print('Connected to :', client_address)

p, g, public_client = 0, 0, 0

try:
    msg = conn.recv(1024).decode()
    p, g, public_client = [int(item) for item in msg.split(',')]
except Exception as e:
    print(e)


print('Modulus : ', p, ' received from client')
print('Base : ', g, ' received from client')

# R2 = g^private_number % p
private_number = random.randint(1, g)
print('Private number belonging to server: ', private_number)
public_server = (g**private_number) % p
print('Public Server Key : ', public_server, ' sent to client')

# k = R1^private_number % p
key = (public_client**private_number) % p

# Send R2
conn.send(str(public_server).encode())
print('Public Client Key : ', public_client, ' received from client')
print('Key : ', key)
conn.close()
