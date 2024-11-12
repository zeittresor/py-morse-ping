import time
import subprocess
from datetime import datetime
import tkinter as tk
from threading import Thread
# Source: https://github.com/zeittresor/py-morse-ping
# Settings for Morse code decoding (in seconds)
dot_threshold = 0.3
dash_threshold = 0.7

running = False

# Morse code dictionary for decoding
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '/': ' '
}

def decode_morse(morse_code):
    """Translates a Morse code sequence into a character."""
    return morse_code_dict.get(morse_code, '')  # Returns an empty string if code is not found

def listen_for_pings():
    """Receives pings and records the time intervals, then decodes to text."""
    global running
    previous_time = None
    morse_code = ""
    output_text.delete("1.0", tk.END)  # Clear previous text
    
    while running:
        # Simulated reception of a ping (replace with actual ping listener code)
        subprocess.run(["ping", "-c", "1", "192.168.1.1"])
        current_time = datetime.now()
        
        if previous_time:
            time_diff = (current_time - previous_time).total_seconds()
            if time_diff < dot_threshold:
                morse_code += "."
            elif time_diff < dash_threshold:
                morse_code += "-"
            else:
                # Decode current Morse code to text and display it
                decoded_char = decode_morse(morse_code)
                output_text.insert(tk.END, decoded_char)
                morse_code = ""  # Reset morse code for next character

        previous_time = current_time
        time.sleep(0.1)

def start_listening():
    """Starts listening in a separate thread."""
    global running
    running = True
    listen_thread = Thread(target=listen_for_pings)
    listen_thread.start()

def stop_listening():
    """Stops listening."""
    global running
    running = False

# Set up the GUI
root = tk.Tk()
root.title("Morse Code Receiver")

# Text output for received messages
output_text = tk.Text(root, width=40, height=10)
output_text.pack()

# Start and Stop buttons
listen_button = tk.Button(root, text="Listen for a transmission", command=start_listening)
listen_button.pack()

stop_button = tk.Button(root, text="Stop Listening", command=stop_listening)
stop_button.pack()

root.mainloop()
