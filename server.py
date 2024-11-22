# Очень увлекательно. Но непонятно как на практике применять то.
# если нет Pycharm Community как запускать как экспериментировать
# Типа впитываешь себе всю эту информацию, а на практике ноль. Страноо. Терпим и учим.
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()