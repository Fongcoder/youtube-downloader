import tkinter as tk
from tkinter import messagebox, scrolledtext
import yt_dlp
import threading

DOWNLOAD_PATH = 'C:\\Users\\Albit\\Downloads'

def download_videos(urls, status_text):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{DOWNLOAD_PATH}\\%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                status_text.insert(tk.END, f"Downloading: {url}\n")
                status_text.see(tk.END)
                ydl.download([url])
                status_text.insert(tk.END, "Download completed!\n\n")
            except Exception as e:
                status_text.insert(tk.END, f"Error: {e}\n\n")
            status_text.see(tk.END)

def start_download(urls, status_text):
    if not urls:
        messagebox.showwarning("No URLs", "Please add at least one YouTube URL.")
        return
    threading.Thread(target=download_videos, args=(urls, status_text), daemon=True).start()

def add_url(entry, url_listbox):
    url = entry.get().strip()
    if url:
        url_listbox.insert(tk.END, url)
        entry.delete(0, tk.END)

def remove_selected(url_listbox):
    selected = url_listbox.curselection()
    for i in reversed(selected):
        url_listbox.delete(i)

def main():
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    tk.Label(root, text="YouTube URL:").pack(pady=(10, 0))
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(padx=10, pady=5)

    add_btn = tk.Button(root, text="Add URL", command=lambda: add_url(url_entry, url_listbox))
    add_btn.pack(pady=2)

    url_listbox = tk.Listbox(root, width=60, height=8)
    url_listbox.pack(padx=10, pady=5)

    remove_btn = tk.Button(root, text="Remove Selected", command=lambda: remove_selected(url_listbox))
    remove_btn.pack(pady=2)

    status_text = scrolledtext.ScrolledText(root, width=60, height=10, state='normal')
    status_text.pack(padx=10, pady=10)

    download_btn = tk.Button(
        root,
        text="Download All",
        command=lambda: start_download(list(url_listbox.get(0, tk.END)), status_text)
    )
    download_btn.pack(pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()