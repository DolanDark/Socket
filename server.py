import socket
import threading

PORT = 5050
#SERVER = "192.168.31.195"
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print(SERVER)
print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #New socket and choosing family of socket, inet ipv4 (family, type)
server.bind(ADDRESS)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "!DISCONNECT":
                connected = False       #break
            print(f"[{addr}], {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")

print("[STARTING] The server is starting...")
start()
