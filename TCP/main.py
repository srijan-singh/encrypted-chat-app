# TCP
import time, socket, sys, server, client
# Threading
import threading

class TCP:

    def server(self):
        
        s = server.Server()
        
        s.set_connection()
        s.find_connection()

        server_value = s.start_chat()
        return server_value

    def client(self, address="192.168.10.127"):
        
        c = client.Client()
        c.set_connection(address, "Client")
        client_value = c.start_chat()
        return client_value




if __name__ == "__main__":
    # Note: If Getting Error Check Client's and Server's IP Address
    t = TCP()

    x = threading.Thread(target=t.server)
    x.start()

    server_address = input("Server's address: ") 

    y = threading.Thread(target=t.client, args=(server_address,))    
    y.start()

    