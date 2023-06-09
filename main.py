import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

toggle_key = KeyCode(char='e')
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.1)


def toggle_event(key): # будет отслеживать активен ли наш евент и давать возможность преключать состояния
    if key == toggle_key:
        global clicking
        clicking = not clicking


def main():
    clicking_thread = threading.Thread(target=clicker) # поток отслеживает изменения нажатия клавиш на клавиатуре
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener: # поток который занимается кликами
        listener.join() 


if __name__ == '__main__':
    main()