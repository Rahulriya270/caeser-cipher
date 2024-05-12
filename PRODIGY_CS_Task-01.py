import tkinter as tk
from tkinter import messagebox
import pyperclip

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 - shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def copy_to_clipboard(text):
    pyperclip.copy(text)
    messagebox.showinfo("Copied", "Encrypted message copied to clipboard")

def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())

    encrypted_message = caesar_cipher_encrypt(message, shift)
    messagebox.showinfo("Encrypted Message", encrypted_message)
    copy_button = tk.Button(root, text="Copy", command=lambda: copy_to_clipboard(encrypted_message))
    copy_button.pack()

def decrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())

    decrypted_message = caesar_cipher_decrypt(message, shift)
    messagebox.showinfo("Decrypted Message", decrypted_message)

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_message = tk.Label(frame, text="Enter Message:")
label_message.grid(row=0, column=0, sticky="w")

entry_message = tk.Entry(frame, width=30)
entry_message.grid(row=0, column=1, padx=10, pady=5)

label_shift = tk.Label(frame, text="Enter Shift Value:")
label_shift.grid(row=1, column=0, sticky="w")

entry_shift = tk.Entry(frame, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

button_encrypt = tk.Button(frame, text="Encrypt", command=encrypt_message)
button_encrypt.grid(row=2, column=0, pady=10)

button_decrypt = tk.Button(frame, text="Decrypt", command=decrypt_message)
button_decrypt.grid(row=2, column=1, pady=10)

root.mainloop()
