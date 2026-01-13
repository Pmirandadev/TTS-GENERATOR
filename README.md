# 🚀 TTS_GENERATOR

O **TTS_GENERATOR** é um aplicativo desktop em Python que converte textos em áudio utilizando o mecanismo de síntese de voz do **Edge TTS**, com interface gráfica em **CustomTkinter**.

Ele permite transformar qualquer texto digitado ou carregado de arquivos `.txt` em arquivos `.mp3` de forma simples e rápida.

## ✨ Funcionalidades
- 📄 Conversão de texto para áudio (.mp3)
- 🎤 Suporte a vozes em Português Brasil
- 🎚 Ajuste de velocidade da fala
- 📁 Importar arquivos `.txt`
- 🗂 Geração e organização automática dos áudios
- 🔔 Notificações de conclusão ou erros
- 🪟 Interface amigável e intuitiva
- 💾 Abertura automática da pasta de áudios gerados
- 🖥 Compatível somente com Windows atualmente

## 🔊 Vozes disponíveis
- pt-BR-AntonioNeural (Masculina)
- pt-BR-FranciscaNeural (Feminina)
- pt-BR-ThalitaMultilingualNeural (Feminina Multilíngue)

## 📦 Como usar
1. Abra o aplicativo
2. Digite ou importe um texto `.txt`
3. Escolha uma voz
4. Ajuste a velocidade (opcional)
5. Clique em **Gerar Áudio**
6. O arquivo será salvo na pasta `audios/`

## 🛠 Tecnologias utilizadas
- Python 3.11
- CustomTkinter
- Edge TTS API
- PyInstaller (Build)
- Inno Setup (Instalador)

Instale as dependências:
pip install -r requirements.txt

Execute:
python src/Gerador.py

## 📦 Download para usuários finais
Baixe a última versão compilada em:
➡ Release → Instalador_GeradorVoz.exe

## 📂 Estrutura
TTS_GENERATOR/ </br>
 ├── src/</br>
 │    └── Gerador.py</br>
 ├── installer/</br>
 │    └── Gerador.spec</br>
 │    └── setup.iss</br>
 ├── icons/</br>
 │    └── TTS_GENERATOR.ico</br>
 ├── audios/</br>
 ├── requirements.txt</br>
 ├── README.md</br>
 └── LICENSE</br>

## 🧭 Roadmap
- [ ] Suporte a mais idiomas
- [ ] Player interno de áudio
- [ ] Exportar para WAV
- [ ] Histórico de textos
- [ ] Atualizador automático
- [ ] Versão Linux

## 👨‍💻 Autor
**Pmirandadev**

## 📜 Licença
Este projeto pode ser licenciado sob a **MIT License**.  
