import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def escolher_pasta_gui():
    return filedialog.askdirectory(title="Escolha a pasta de destino")

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)

        if total:
            progress = int(downloaded / total * 100)
            progresso_var.set(progress)
            janela.update_idletasks()
    elif d['status'] == 'finished':
        progresso_var.set(100)
        status_label.config(text="🛠️ Processando arquivo...", fg="orange")

def baixar():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Erro", "Insira uma URL válida.")
        return

    audio_only = audio_var.get()
    quality = 'bestaudio' if audio_only else 'bestvideo+bestaudio/best'

    if qualidade_custom.get():
        selected_quality = qualidade_escolhida.get()
        if selected_quality:
            quality = selected_quality

    output_path = pasta_var.get().strip()
    if not output_path:
        messagebox.showerror("Erro", "Escolha uma pasta de destino.")
        return

    os.makedirs(output_path, exist_ok=True)

    progresso_var.set(0)
    status_label.config(text="⏬ Baixando...", fg="blue")
    janela.update()

    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestaudio' if audio_only else quality,
        'prefer_ffmpeg': True,
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if audio_only else []
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="✅ Download concluído!", fg="green")
    except Exception as e:
        status_label.config(text=f"❌ Erro: {e}", fg="red")

def escolher_pasta_click():
    pasta = escolher_pasta_gui()
    if pasta:
        pasta_var.set(pasta)

def toggle_dropdown():
    if qualidade_custom.get():
        dropdown_menu.pack()
    else:
        dropdown_menu.pack_forget()

# === GUI ===

janela = tk.Tk()
janela.title("🎬 Downloader de Vídeos")
janela.geometry("500x450")
janela.resizable(False, False)

tk.Label(janela, text="🔗 URL do vídeo:").pack(pady=(10, 0))
url_entry = tk.Entry(janela, width=60)
url_entry.pack()

audio_var = tk.BooleanVar()
tk.Checkbutton(janela, text="🎵 Baixar apenas o áudio (MP3)", variable=audio_var).pack(pady=5)

qualidade_custom = tk.BooleanVar()
tk.Checkbutton(janela, text="⚙️ Usar qualidade personalizada", variable=qualidade_custom, command=toggle_dropdown).pack()

qualidades_opcoes = [
    "bestvideo+bestaudio/best",
    "bestvideo[height<=1080]+bestaudio",
    "bestvideo[height<=720]+bestaudio",
    "best",
    "worst"
]
qualidade_escolhida = tk.StringVar(value=qualidades_opcoes[1]) 
dropdown_menu = tk.OptionMenu(janela, qualidade_escolhida, *qualidades_opcoes)

tk.Label(janela, text="📁 Pasta de destino:").pack(pady=(10, 0))
pasta_var = tk.StringVar(value="./videos")

pasta_frame = tk.Frame(janela)
pasta_frame.pack()
pasta_entry = tk.Entry(pasta_frame, textvariable=pasta_var, width=40)
pasta_entry.pack(side=tk.LEFT, padx=(10, 5), pady=5)
tk.Button(pasta_frame, text="Selecionar", command=escolher_pasta_click).pack(side=tk.LEFT)

tk.Label(janela, text="").pack()

botao_frame = tk.Frame(janela)
botao_frame.pack(pady=5)
tk.Button(botao_frame, text="⬇️ Iniciar Download", command=baixar, bg="#28a745", fg="white", height=2, width=20).pack()

progresso_var = tk.IntVar()
progresso_barra = ttk.Progressbar(janela, orient="horizontal", length=300, mode="determinate", variable=progresso_var)
progresso_barra.pack(pady=10)

status_label = tk.Label(janela, text="", font=("Arial", 10))
status_label.pack()

janela.mainloop()
