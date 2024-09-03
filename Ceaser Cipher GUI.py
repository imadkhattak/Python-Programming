from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Caesar Cipher Encryption")
root.geometry("900x700")
root.configure(bg="#f2f2f2")


font_large = ('Helvetica', 14)
font_title = ('Helvetica', 18, 'bold')


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


title_label = Label(root, text="Caesar Cipher Encryption", font=font_title, bg="#f2f2f2")
title_label.pack(pady=20)


input_frame = Frame(root, bg="#f2f2f2")
input_frame.pack(pady=10, padx=20, fill='x')

output_frame = Frame(root, bg="#f2f2f2")
output_frame.pack(pady=10, padx=20, fill='x')


key_label = Label(input_frame, text="Key:", font=font_large, bg="#f2f2f2")
key_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
key = Entry(input_frame, width=20, borderwidth=2, font=font_large)
key.grid(row=0, column=1, padx=10, pady=10, sticky="w")


sentence_label = Label(input_frame, text="Enter sentence:", font=font_large, bg="#f2f2f2")
sentence_label.grid(row=1, column=0, padx=10, pady=10, sticky="ne")
sentence = Text(input_frame, width=50, height=5, borderwidth=2, font=font_large)
sentence.grid(row=1, column=1, padx=10, pady=10, sticky="nw")


display_label = Label(output_frame, text="Encrypted Text:", font=font_large, bg="#f2f2f2")
display_label.grid(row=0, column=0, padx=10, pady=10, sticky="ne")
output_box = Text(output_frame, width=50, height=5, borderwidth=2, font=font_large, bg="#e6e6e6")
output_box.grid(row=0, column=1, padx=10, pady=10, sticky="nw")


sentence_label_decrypt = Label(output_frame, text="Enter sentence to decrypt:", font=font_large, bg="#f2f2f2")
sentence_label_decrypt.grid(row=1, column=0, padx=10, pady=10, sticky="ne")
sentence_decryp = Text(output_frame, width=50, height=5, borderwidth=2, font=font_large)
sentence_decryp.grid(row=1, column=1, padx=10, pady=10, sticky="nw")


display_label1 = Label(output_frame, text="Decrypted Text:", font=font_large, bg="#f2f2f2")
display_label1.grid(row=2, column=0, padx=10, pady=10, sticky="ne")
output_box1 = Text(output_frame, width=50, height=5, borderwidth=2, font=font_large, bg="#e6e6e6")
output_box1.grid(row=2, column=1, padx=10, pady=10, sticky="nw")


def encryption():
    encrypted_sentence = []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    sentence_val = sentence.get("1.0", "end-1c").lower()

    try:
        key_val = int(key.get())
    except ValueError:
        display_label.config(text="Please enter a valid integer for the key.")
        return

    for s in sentence_val:
        if s in abc:
            index_1 = abc.index(s)
            index_2 = (index_1 + key_val) % 26 
            new_char = abc[index_2]
            encrypted_sentence.append(new_char)
        else:
            encrypted_sentence.append(s)

    encrypted_text = ''.join(encrypted_sentence)
    output_box.delete("1.0", "end") 
    output_box.insert("1.0", encrypted_text) 


def decrypt():
    decrypted_sentence = []
    abc = 'abcdefghijklmnopqrstuvwxyz'
    sentence_val = sentence_decryp.get("1.0", "end-1c").lower()

    try:
        key_val = int(key.get())
    except ValueError:
        display_label.config(text="Please enter a valid integer for the key.")
        return

    for s in sentence_val:
        if s in abc:
            index_1 = abc.index(s)
            index_2 = (index_1 - key_val) % 26
            new_char = abc[index_2]
            decrypted_sentence.append(new_char)
        else:
            decrypted_sentence.append(s)

    decrypted_text = ''.join(decrypted_sentence)
    output_box1.delete("1.0", "end") 
    output_box1.insert("1.0", decrypted_text) 


button_frame = Frame(root, bg="#f2f2f2")
button_frame.pack(pady=20)

encrypt_button = Button(button_frame, text="Encrypt", padx=40, pady=10, command=encryption, font=font_large, bg="#4CAF50", fg="white", borderwidth=0)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = Button(button_frame, text="Decrypt", padx=40, pady=10, command=decrypt, font=font_large, bg="#f44336", fg="white", borderwidth=0)
decrypt_button.grid(row=0, column=1, padx=10)

center_window(root)
root.mainloop()
