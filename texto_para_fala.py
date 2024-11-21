import os
from PyPDF2 import PdfReader
from gtts import gTTS
from googletrans import Translator

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Solicitar o nome do arquivo PDF
s = input("Digite o nome do arquivo PDF: ")

try:
    text = extract_text_from_pdf(s)
    if not text.strip():
        raise ValueError("O arquivo PDF não contém texto legível.")
except FileNotFoundError:
    print("Arquivo não encontrado. Por favor, verifique o nome do arquivo e tente novamente.")
    print("Arquivos disponíveis no diretório:")
    print(os.listdir())
    exit()
except ValueError as ve:
    print(ve)
    exit()

# Traduzir o texto de inglês para português
translator = Translator()
translated_text = translator.translate(text, src='en', dest='pt').text

# Criar o objeto gTTS com o texto traduzido
obj = gTTS(text=translated_text, lang='pt', slow=False)

# Solicitar o nome do arquivo de áudio
f1 = input("Digite o nome do áudio a ser salvo (sem .mp3): ")
if not f1.endswith('.mp3'):
    f1 += '.mp3'

# Salvar o arquivo de áudio
obj.save(f1)
print(f"Arquivo de áudio '{f1}' salvo com sucesso!")
