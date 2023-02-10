# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="black")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa DIA!")

# Variables dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# frame input 
input_frame = ttk.Frame(window)
# penempatan Gri, Pack , place
input_frame.pack(padx=10,pady=10,fil="x",expand=True)

# kompone-komponen 
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,fil="x",expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fil="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang:")
nama_belakang_label.pack(padx=10,fil="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fil="x",expand=True)
# 5.Tombol
def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    print(NAMA_BELAKANG.get())
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Kamu kereeeeeennnn AbieZZZZZ!"
    showinfo(title="HAIIII!",message=pesan)

tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(padx=10,fil="x",expand=True,pady=10)

# Main Loop Window
window.mainloop()