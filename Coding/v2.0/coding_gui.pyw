try:
    from coding import *
except:
    messagebox.showerror("Error", "Coding Library not found")

from tkinter import messagebox
from tkinter.filedialog import askopenfile

from tkinter import *

root = Tk()
root.title("Coding GUI - Undefined Document")
root.geometry("650x380")
root.resizable(False, False)

VERSION_WIN = 1.00

if VERSION < 2.00:
    messagebox.showerror("Error", f"Current version: {VERSION} \nRequired Version: 2.00")
    root.destroy()

menubar = Menu(root, background='#03A9F4', fg='white')
menubar.configure(bg="#00c3ff")
file = Menu(menubar, tearoff=False, background='#E0F7FA')
edit = Menu(menubar, tearoff=False, background='#E0F7FA')
about = Menu(menubar, tearoff=False, background='#E0F7FA')

global name_file
name_file = "file.txt"

def enc_file():
    val = text.get(1.0, END)
    val_enc = code.encoder(val, "s", SELECTED_KEY)
    text.delete(1.0, END)
    text.insert(1.0, val_enc)

def dec_file():
    val = text.get(1.0, END)
    val_dec = code.decoder(val, "s", SELECTED_KEY)
    text.delete(1.0, END)
    text.insert(1.0, val_dec)

def open_txt():
    file_txt = askopenfile()
    file = open(file_txt.name)
    root.title("Coding GUI - "+file.name)
    val = file.read()
    text.delete(1.0, END)
    text.insert(1.0, val)
    file.close()

def open_enc():
    file_txt = askopenfile(filetypes=[("Coding Encode File", "*.cef")])
    file = open(file_txt.name)
    val = file.read()
    text.delete(1.0, END)
    text.insert(1.0, val)
    file.close()
    dec_file()

def save_txt():
    try:
        file_txt = open(name_file, "w")
        root.title("Coding GUI - " +file_txt.name)
        file_txt.write(text.get(1.0,END))
        file_txt.close()
    except:
        messagebox.showerror("Error", "Error")
    
def save_cef():
    try:
        save_txt()
        file_txt_enc = code.encoder(name_file, "f+", SELECTED_KEY)
    except:
        messagebox.showerror("Error", "Error")
    
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side=TOP, fill=BOTH)
scrollbar.config(command=text.yview)

file.add_command(label="New File (.txt)", command=save_txt)
file.add_command(label="New File (.cef)", command=save_cef)
file.add_separator()
file.add_command(label="Encode File", command=enc_file)
file.add_command(label="Decode File", command=dec_file)
file.add_separator()
file.add_command(label="Open (.cef) File", command=open_enc)
file.add_command(label="Open File", command=open_txt)
file.add_separator()
file.add_command(label="Exit", command=root.quit)

mes = f"Coding GUI - Version - {VERSION_WIN} \nCoding Library - Version - {VERSION} \nEncoding created by @GFS-0508, see github and see license, https://github.com/GFS-0508/"

def message():
    messagebox.askokcancel("About", mes)

about.add_command(label="About", command=message)

menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="About", menu=about)
  
root.config(menu=menubar)

root.mainloop()
