from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("400x500")
app.title("Mp3 Downloader")
app.resizable(width=False, height=False)
set_appearance_mode("dark") # Tema

def botaoclick():
    print(entrada_url.get())
    pass

entrada_url = CTkEntry(app, width=350,height=40,placeholder_text='URL...',fg_color='white', text_color='black')
entrada_url.place(relx=0.07,rely=0.6,anchor='w')

# imagem = ''
title_label = CTkLabel(app,width=400,height=90,corner_radius=20,bg_color='transparent',text_color='white',text='MP3 Download', font=('arial', 40)).pack(pady=30)
img_label = CTkLabel(app,text=None,image=None).pack()
button1 = CTkButton(app,width=80,height=40,corner_radius=10,fg_color='red', hover_color='gray',text='Download', command=botaoclick).place(relx=0.07,rely=0.8, anchor='w')



app.mainloop()