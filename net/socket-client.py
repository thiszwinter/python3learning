import socket

server_addr="127.0.0.1"
server_port=8865

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((server_addr, server_port))
	s.sendall(b"Hello, Ross!")
	data = s.recv(server_port)
	print("Received: ", repr(data))
