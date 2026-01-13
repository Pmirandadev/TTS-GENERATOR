import edge_tts                         # Serviço online do Edge que permite a conversão de texto em fala diretamente no código
import asyncio                          # Biblioteca para esperar a conversão de texto em fala para depois gerar o audio
import customtkinter as ctk             # Biblioteca para criar a UI de interface
import threading as thd                 # Biblioteca para trabalhar com Threads
import time                             # Biblioteca time
import os                               # Biblioteca para mecher no sistema operacional(criação e afins de pasta e arquivos)
from tkinter import filedialog as fd    # Biblioteca para Selecionar o TXT e carregar
from tkinter import messagebox          # Biblioteca para apresentar mensagens de status

# =======================================================
# VARIAVEIS
# =======================================================
# Vozes masculinas:
voz_antonio = "pt-BR-AntonioNeural"         

# Vozes Femininas:
voz_thalita =   "pt-BR-ThalitaMultilingualNeural"   
voz_francisca = "pt-BR-FranciscaNeural"

# Lista das Vozes
option_list = [voz_antonio, voz_francisca, voz_thalita]

# =======================================================
# FUNCOES
# =======================================================
def carregar_arquivo():
    arquivo = fd.askopenfilename(
        filetypes=[("Arquivos de Texto", "*.txt")]
    )
    if arquivo:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            textbox.delete("1.0", "end")
            textbox.insert("1.0", conteudo)

def get_data_dir():
    base = os.path.join(os.getenv("APPDATA"), "TTS_GENERATOR", "audios")
    os.makedirs(base, exist_ok=True)
    return base

DATA_DIR = get_data_dir()
pasta_aberta = False

def gerar_nome_audio():
    return f"audio_{int(time.time())}.mp3"

def gerar_audio_thread():
    t = thd.Thread(target=lambda: asyncio.run(gerar_audio_ui()))
    t.start()

def update_label(value):
    label_vel.configure(text=f"Velocidade: {int(value)}%")

def abrir_pasta_audios():
    os.startfile(DATA_DIR)

async def gerar_audio_ui():
    global pasta_aberta
    btn_gerar.configure(state="disabled")                       # Desabilitar o Botão para não ter Dublo click
    texto_input = textbox.get("1.0", "end"). strip()
    voz_input = selection_voz.get()
    
    if not text_vazio():
        btn_gerar.configure(state="normal")
        return                                                # Funcao para ver se tem texto para converter

    valor_slider = int(slider_vel.get())                        # Velocidade da voz
    rate = f"{'+' if valor_slider >= 0 else ''}{valor_slider}%"

    progress_bar.set(0.1)                                       # Barra de Porgressão                                              
        
    nome_arquivo = gerar_nome_audio()                           # Gerar Nome do arquivo sem repeticoes
    caminho_arquivo = os.path.join(DATA_DIR, nome_arquivo)      # Pasta gerada para armazenar os audios
    
    communicate = edge_tts.Communicate(
        texto_input,
        voice=voz_input,
        rate=rate
    )

    await communicate.save(caminho_arquivo)                        # Aguarda finalizar a conversão e salva

    progress_bar.set(1.0)                                       

    messagebox.showinfo(
        "Sucesso",
        f"Áudio gerado com sucesso!\nArquivo: {nome_arquivo}"
    )
    btn_gerar.configure(state="normal")

    if not pasta_aberta:
        os.startfile(DATA_DIR)
        pasta_aberta = True

def text_vazio():
    texto_input = textbox.get("1.0", "end"). strip()
    if texto_input == "":
        messagebox.showwarning(
            "Aviso",
            "Você precisa digitar ou carregar um texto antes de gerar o áudio!"
        )
        return False
    return True

# =======================================================
# GERAR A INTERFACE SEM OS BOTOES E LABELS PARA O APP
# =======================================================
ctk.set_appearance_mode("dark")                                             # Colocar uma interface Estilo Dark
ctk.set_default_color_theme("blue")                                         # Cor do Tema Azul

app = ctk.CTk()                                                             # Criação do CTk
app.title("TTS GENERATOR")                                                  # Titulo da Aplicação
app.geometry("720x680")                                                     # Tamanho da Interface
# =======================================================
# UI DA INTERFACE - BOTOES E LABELS
# =======================================================
titulo = ctk.CTkLabel(app, text="TTS GENERATOR", font=("Arial", 26, "bold"))
titulo.pack(pady=10)
label_titulo = ctk.CTkLabel(app, text="ESCREVA NO CAMPO ABAIXO O TEXTO EM QUESTÃO PARA GERAR O AUDIO")
label_titulo.pack(pady=1)

selection_voz = ctk.CTkOptionMenu(app, values=option_list)
selection_voz.pack()

textbox = ctk.CTkTextbox(app, width=680, height=260)
textbox.pack(pady=10)

label_text = ctk.CTkLabel(app, text="Caso já tenha um arquivo txt, selecione ele para Gerar o Audio")
label_text.pack(pady=1)
btn_text = ctk.CTkButton(app, text="Selecionar o Texto", command=carregar_arquivo)
btn_text.pack(pady=5)

btn_gerar = ctk.CTkButton(app, text="Gerar Aúdio", command=gerar_audio_thread)
btn_gerar.pack(pady=5)

progress_bar = ctk.CTkProgressBar(app, width=660, progress_color="green")   # Barra de Progressão
progress_bar.place(x = 30, y = 620)
progress_bar.set(0)
progress_bar.stop()

label_vel = ctk.CTkLabel(app, text="Velocidade do Áudio")
label_vel.pack(pady=5)

slider_vel = ctk.CTkSlider(app, from_=-50, to=50, number_of_steps=100, command=update_label)
slider_vel.pack(pady=5)
slider_vel.set(0)  # 0% como padrão

btn_abrir = ctk.CTkButton(
    app,
    text="📁",
    width=40,
    height=40,
    command=abrir_pasta_audios
)
btn_abrir.place(relx=0.95, rely=0.05, anchor="ne")
# =======================================================
# INICIALIZAÇÃO DO APP
# =======================================================
app.mainloop()