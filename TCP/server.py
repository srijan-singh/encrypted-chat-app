# server.py
import time, socket, sys

class Server:

    def set_connection(self, name="Server"):
        print("\nWelcome to Chat Room\n")
        print("Initialising....\n")
        time.sleep(1)
        self.s = socket.socket()
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        port = 1234
        self.s.bind((host, port))
        print(host, "(", ip, ")\n")
        self.name = name

    def find_connection(self):        
        self.s.listen(1)
        print("\nWaiting for incoming connections...\n")
        self.conn, addr = self.s.accept()
        print("Received connection from ", addr[0], "(", addr[1], ")\n")

        self.s_name = self.conn.recv(1024)
        self.s_name = self.s_name.decode()
        print(self.s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
        self.conn.send(self.name.encode())

    def start_chat(self):        
        while True:
            message = input(str("Server : "))
            if message == "[e]":
                message = "Left chat room!"
                self.conn.send(message.encode())
                print("\nServer Left\n")                
                break  

            self.conn.send(message.encode())
            message = self.conn.recv(1024)
            message = message.decode()
            #print(self.s_name, ":", message)

        return False

if __name__ == "__main__":
    s = Server()
    s.set_connection()
    s.find_connection()
    value = s.start_chat()
    print("Value", value)

