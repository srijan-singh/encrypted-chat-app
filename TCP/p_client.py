# client.py
import time, socket, sys

class Client:

    def set_connection(self, host, name):
        print("\nWelcome to Chat Room\n")
        print("Initialising....\n")
        time.sleep(1)
        self.s = socket.socket()
        self.shost = socket.gethostname()
        ip = socket.gethostbyname(self.shost)
        print(self.shost, "(", ip, ")\n")
        self.host = host
        self.name = name
        port = 1234
        print("\nTrying to connect to ",self.host, "(", port, ")\n")
        time.sleep(1)
        self.s.connect((host, port))
        print("Connected...\n")

        self.s.send(name.encode())
        self.s_name = self.s.recv(1024)
        self.s_name = self.s_name.decode()
        print(self.s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

    def start_chat(self):               
        while True:
            message = self.s.recv(1024)
            message = message.decode()
            #print(self.s_name, ":", message)
            message = input(str("Client : "))
            if message == "[e]":
                message = "Left chat room!"
                self.s.send(message.encode())
                print("\nClient Left\n")
                break

            self.s.send(message.encode())

        return False

if __name__ == "__main__":
    c = Client()
    c.set_connection("192.168.14.103","Client")
    value = c.start_chat()
    print("Value", value)