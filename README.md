# Downloader de Vídeos com Tkinter e yt-dlp

Um aplicativo em Python com interface gráfica (Tkinter) para baixar vídeos ou apenas o áudio (MP3) de links suportados pelo [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## Funcionalidades
- Baixar vídeos a partir de uma URL.
- Opção de baixar apenas o áudio em MP3.
- Seleção de qualidade personalizada (1080p, 720p, etc).
- Escolha da pasta de destino para salvar os arquivos.
- Barra de progresso em tempo real.
- Mensagens de status durante o download.

---

## Como usar

### 1. Clone o repositório

### 2. Crie um ambiente virtual e instale as dependências

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install yt-dlp tk

!!!!!!!Para conversão de áudio em MP3, é necessário ter o FFmpeg instalado.

### 3. Execute o programa
python app.py



° Tecnologias utilizadas:

Python 3

Tkinter

yt-dlp

FFmpeg
