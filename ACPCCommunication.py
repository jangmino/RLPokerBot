import socket


class ACPCCommunication:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.name = "ACPCCommunication"
        self.MSGLEN = 1024

    def connect(self, host, port):
        self.sock.connect((host, port))

    def handshake(self):
        self.send_line('VERSION:2.0.0')

    def send_line(self, line):
        totalsent = 0
        msg = line + '\r\n'
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:].encode())
            if sent == 0:
                raise RuntimeError("socket connection broken while sending")
            totalsent = totalsent + sent
        return totalsent

    def get_line(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken while reading")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            if chunk[-2:] == b'\r\n':
                break
        return b''.join(chunks).decode()

    def close(self):
        self.sock.close()



