from pytube import YouTube
import customtkinter as ctk
from customtkinter import *
import time
import os

DOWNLOAD_DIR = "C:/Users/allys/Downloads"

def download(link, stream_type,text_box):
    yt = YouTube(link)
    print("Titulo:", yt.title)
    
    if stream_type == "video":
        stream = yt.streams.get_highest_resolution()
        download_dir = os.path.join(DOWNLOAD_DIR, "Videos")
    elif stream_type == "audio":
        stream = yt.streams.get_audio_only()
        download_dir = os.path.join(DOWNLOAD_DIR, "Audios")
        
    else:
        print("Tipo de stream inválido!")
        return
    
    if not os.path.isdir(download_dir):
        os.makedirs(download_dir)
    
    stream.download(download_dir)
    print("Baixando...")
    time.sleep(3)
    print("Download concluído com sucesso!")


    text_box.delete(0, END)

def app():
    root = ctk.CTk()
    root.title("TikoTeko")
    root.geometry("500x150")
    root.resizable(width=False, height=False)
    ctk.set_appearance_mode("Dark")
    
    text_box = ctk.CTkEntry(master=root, width=450, height=30, corner_radius=10)
    text_box.place(x=40, y=40)  
    
    message = ctk.CTkLabel(root, text="URL")
    message.place(x=10, y=40)
    message_2 = ctk.CTkLabel(root, text="INSIRA SEU LINK NO ESPAÇO A BAIXO...")
    message_2.place(x=130, y=8)
    
    confirm_button = ctk.CTkButton(master=root, width=5, height=40, text="MP4", corner_radius=50, command=lambda: download(text_box.get(), "video",text_box))
    confirm_button.place(x=160, y=90)
    
    change_button = ctk.CTkButton(master=root, width=5, height=40, text="MP3", corner_radius=50, command=lambda: download(text_box.get(), "audio",text_box))
    change_button.place(x=280, y=90)
    
    root.mainloop()

app()
