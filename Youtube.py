# coding=utf-8

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from turtle import color
from pytube import YouTube
from tkinter import messagebox, filedialog


def Widgets():
    
    link_label = Label(root, text="URL Youtube: ",bg="#DCDCDC")    
    fontExample = tkFont.Font(family="Arial", size=12, weight="bold")
    link_label.configure(font=fontExample)
    link_label.grid(row=1,column=0,pady=5,padx=5)
    
    destination_label = Label(root,text="Salvar no diretório: ", bg="#DCDCDC")
    destination_label.configure(font=fontExample)
    destination_label.grid(row=2,column=0,pady=5,padx=5)

    
    root.linkText = Entry(root,width=55,textvariable=video_Link)
    root.linkText.grid(row=1,column=1,pady=5,columnspan=2)

    root.destinationText = Entry(root,width=40,textvariable=download_Path)
    root.destinationText.grid(row=2,column=1,pady=5,padx=5)

    browse_B = Button(root,text="Procurar",command=Browse,width=10,bg="#DCDCDC")
    browse_B.grid(row=2, column=2,pady=1,padx=1)

    Download_B = Button(root,text="Downdload",command=Downdload,width=20,bg="#DCDCDC")
    Download_B.grid(row=3,column=1,pady=3,padx=3)

def Browse():
  downdload_Directory = filedialog.askdirectory(initialdir="/content/drive/MyDrive/Teste")
  download_Path.set(downdload_Directory)

def Downdload():

  Youtube_link = video_Link.get()

  downdload_Folder = download_Path.get()

  getVideo = YouTube(Youtube_link)
  #mp4files = getVideo.filter('mp4')
  #mp4files[-1].extension,mp4files[-1].resolution
 
  videoStream = getVideo.streams.filter(progressive=True, file_extension='mp4')\
  .order_by('resolution').first()

  videoStream.download(downdload_Folder)

  messagebox.showinfo("SUCESSO","VIDEO BAIXADO E SALVO EM\n" + downdload_Folder)


root = tk.Tk()

root.geometry("640x360")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")

video_Link = StringVar()
download_Path = StringVar()

Widgets()
root.mainloop()