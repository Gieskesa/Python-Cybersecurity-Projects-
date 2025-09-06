from pynput import keyboard 

def keyPressed(key):
    try:
        print("Alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("Special key {0} pressed".format(key))
                

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()