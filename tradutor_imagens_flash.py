import os
from PIL import Image, ImageDraw, ImageFont
import pytesseract
from deep_translator import GoogleTranslator
import numpy as np
from tqdm import tqdm

# Configuração do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para traduzir texto
def traduzir_texto(texto):
    try:
        return GoogleTranslator(source='auto', target='pt').translate(texto)
    except Exception as e:
        print(f"Erro ao traduzir texto: {e}")
        return texto

# Função para detectar a cor média de uma região
def detectar_cor(imagem, bbox):
    region = imagem.crop(bbox)  # Recorta a região do texto
    np_region = np.array(region)  # Converte para array NumPy
    avg_color = np.mean(np_region, axis=(0, 1))  # Calcula a cor média (R, G, B)
    return tuple(map(int, avg_color))  # Converte para inteiro e retorna

# Função para processar uma única imagem
def processar_imagem(input_file, output_folder):
    try:
        imagem = Image.open(input_file).convert("RGB")
        dados = pytesseract.image_to_data(imagem, lang='eng', output_type=pytesseract.Output.DICT)
        
        draw = ImageDraw.Draw(imagem)
        fonte_padrao = ImageFont.load_default()  # Substituir por fontes personalizadas se necessário

        for i in range(len(dados['text'])):
            texto_original = dados['text'][i]
            if not texto_original.strip():
                continue
            
            # Traduz o texto
            texto_traduzido = traduzir_texto(texto_original)

            # Obtém o bounding box
            x, y, w, h = dados['left'][i], dados['top'][i], dados['width'][i], dados['height'][i]
            bbox = (x, y, x + w, y + h)
            
            # Detecta a cor média do texto original
            cor_texto = detectar_cor(imagem, bbox)
            
            # Escreve o texto traduzido
            draw.rectangle(bbox, fill="white")  # Limpa a área do texto original
            draw.text((x, y), texto_traduzido, fill=cor_texto, font=fonte_padrao)

        # Salva a imagem traduzida
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        imagem.save(output_file)
        print(f"Imagem traduzida salva em: {output_file}")
    
    except Exception as e:
        print(f"Erro ao processar imagem {input_file}: {e}")

# Função para processar todas as imagens de uma pasta
def processar_pasta(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    imagens = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for imagem in tqdm(imagens, desc="Traduzindo imagens", unit="imagem"):
        processar_imagem(imagem, output_folder)

# Define as pastas de entrada e saída
input_folder = 'images'  # Pasta com as imagens originais
output_folder = 'images_traduzidas'  # Pasta para salvar as imagens traduzidas

# Inicia o processo
processar_pasta(input_folder, output_folder)
