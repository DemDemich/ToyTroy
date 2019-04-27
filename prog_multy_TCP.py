import socket
import sys
import traceback
import glob
from threading import Thread


def main():
    start_server()


def start_server():
    host = socket.gethostname()
    port = 1337         # arbitrary non-privileged port

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        print(client_input)
        if "--quit--" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        elif("push" in client_input):
            load_file(connection)
            is_active = False
        elif("ls" in client_input):
            g = glob.glob("*")
            print(glob.glob("*"))
            s = ""
            for i in g:
                s += i + '\n'
            connection.sendall(s.encode('utf-8'))
        elif("pull" in client_input):
            name = connection.recv(1024)
            send_file(name, connection)
            is_active = False

def load_file(c):
    print("Receiving...")
    l = c.recv(1024)
    f = open(l,'wb')
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    #c.send(b'Thank you for sending nudes')
    c.close()

def send_file(fname, c):
    f = open(fname,'rb')
    print('Sending...')
    #c.send(fname.encode('utf-8'))
    l = f.read(1024)
    while (l):
        print('Sending...')
        c.send(l)
        l = f.read(1024)
    f.close()
    c.close()
    #c.shutdown(socket.SHUT_WR)
    print("Done Sending")

def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    if(client_input):
        decoded_input = client_input.decode("utf8")
        return decoded_input
    else:
        return ''



if __name__ == "__main__":
    main()