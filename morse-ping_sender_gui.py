import time
import subprocess
import tkinter as tk
from tkinter import messagebox
# Source: https://github.com/zeittresor/py-morse-ping
# Settings for Morse code symbols (in seconds)
dot_delay = 0.2     # Duration for a dot
dash_delay = 0.6    # Duration for a dash
symbol_space = 0.8  # Pause between symbols (dot/dash)
letter_space = 1.5  # Pause between letters

# Morse code alphabet
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

def send_ping(target_ip, duration):
    """Sends a single ping."""
    subprocess.run(["ping", "-c", "1", target_ip])
    time.sleep(duration)

def send_morse_message(message, target_ip):
    """Sends a message in Morse code."""
    for letter in message.upper():
        if letter in morse_code_dict:
            morse_code = morse_code_dict[letter]
            for symbol in morse_code:
                if symbol == '.':
                    send_ping(target_ip, dot_delay)
                elif symbol == '-':
                    send_ping(target_ip, dash_delay)
                time.sleep(symbol_space)
            time.sleep(letter_space)

def on_send_message():
    message = text_entry.get("1.0", tk.END).strip()
    target_ip = ip_entry.get().strip()
    if not message or not target_ip:
        messagebox.showerror("Error", "Please enter message and target IP.")
        return
    send_morse_message(message, target_ip)
    messagebox.showinfo("Sent", "Message sent!")

# Set up the GUI
root = tk.Tk()
root.title("Morse Code Sender")

# Target IP entry
ip_label = tk.Label(root, text="Target IP:")
ip_label.pack()
ip_entry = tk.Entry(root, width=30)
ip_entry.pack()

# Message input field
text_label = tk.Label(root, text="Message:")
text_label.pack()
text_entry = tk.Text(root, width=40, height=10)
text_entry.pack()

# Send button
send_button = tk.Button(root, text="Send Message", command=on_send_message)
send_button.pack()

root.mainloop()
